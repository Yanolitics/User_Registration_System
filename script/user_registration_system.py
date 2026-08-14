#Part 1: Database Simulation

# Stores successful user registration records as dictionaries
# Schema: {"name": str, "email": str, "password": str}
registered_users = []

# Audit log storing failed registration metadata and reason for failure
# Schema: {"name": str, "email": str, "password": str, "reason": str}
failed_registrations = []


#Part 2: Validation Functions

# Validates that user name contains at least 3 non-whitespace characters
def valid_name(name):
    return len(name.strip()) >= 3


# Checks for basic email structural requirements (@ symbol and domain dot)
def valid_email(email):
    cleaned_email = email.strip().lower()
    if "@" not in cleaned_email or "." not in cleaned_email:
        return False
    return True


# Enforces password complexity rules: 8+ chars, mixed casing, and 1+ special char
def valid_password(password):
    # Rule 1: Minimum length requirement
    if len(password) < 8:
        return False
    
    # Rule 2: Must contain both upper and lower case letters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if not (has_upper and has_lower):
        return False
    
    # Rule 3: Must include at least one special (non-alphanumeric) character
    if password.isalnum():
        return False
        
    return True


#Part 3: Main Validation Orchestrator

# Coordinates individual validation rules and prints specific error feedback
def validate_user_data(user_name, user_email, user_password):
    is_all_data_valid = True
    
    if not valid_name(user_name):
        print("❌ Name must be at least 3 characters long.")
        is_all_data_valid = False

    if not valid_email(user_email):
        print("❌ Email must contain '@' and '.'.")
        is_all_data_valid = False

    if not valid_password(user_password):
        print("❌ Password must be 8+ chars, have mixed casing, and include a special character.")
        is_all_data_valid = False

    # Returns True only if all validation checks pass
    return is_all_data_valid


#Part 4: Registration Function

# Processes registration requests: validates input, checks duplicates, and updates database
def create_user_account(user_name, user_email, user_password):
    # Normalize input early to ensure consistent email formatting
    clean_email = user_email.strip().lower()
    
    # Step 1: Validate input fields against business rules
    if not validate_user_data(user_name, clean_email, user_password):
        # Audit log entry for bad input data
        failed_registrations.append({
            "name": user_name,
            "email": clean_email,
            "password": user_password,
            "reason": "Invalid user data"
        })
        print("❌ Failed to create user account.")
        return None

    # Step 2: Ensure unique email constraint (stops on first match using generator expression)
    if any(user["email"] == clean_email for user in registered_users):
        # Audit log entry for duplicate email collision
        failed_registrations.append({
            "name": user_name,
            "email": clean_email,
            "password": user_password,
            "reason": "Duplicate email"
        })
        print("❌ User account with this email already exists.")
        return None

    # Step 3: Persistence - Append clean, unique user record to database
    registered_users.append({
        "name": user_name.strip(),
        "email": clean_email,
        "password": user_password
    })
    print("✅ User account created successfully!")
    return registered_users


#Part 5: Test Cases

# Test Case 1: Valid User Registration (Expected: Success)
print(create_user_account("Alice", "alice@example.com", "SecurePass123!"))

# Test Case 2: Duplicate Email Registration (Expected: Reject & Log "Duplicate email")
print(create_user_account("Bob", "alice@example.com", "AnotherPass456!"))

# Test Case 3: Invalid Name (Expected: Reject & Log "Invalid user data")
print(create_user_account("Al", "charlie@example.com", "SecurePass123!"))

# Test Case 4: Invalid Email (Expected: Reject & Log "Invalid user data")
print(create_user_account("David", "davidexample.com", "SecurePass123!"))

# Test Case 5: Invalid Password (Expected: Reject & Log "Invalid user data")
print(create_user_account("Eve", "eve@example.com", "weakpassword"))

# Print complete audit trail of rejected registration attempts
print("\n--- Failed Registrations Audit Log ---")
print(failed_registrations)
