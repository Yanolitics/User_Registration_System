# 🔐 Python User Registration & Audit System

---

Welcome to my Python user registration project! This repository contains a simple script I built in **Python 3** to handle registering new users safely and tracking bad registration attempts.

As a self-taught aspiring data practitioner operating under the moniker **Yanolitics**, I built this project to show how raw user inputs can be cleaned, checked against strict rules, and properly stored or flagged if something goes wrong.

---

## 🗺️ How It Works

The script follows a simple 3-step path: **Take in User Details → Clean & Check Rules → Save Valid Users or Log Errors**.

---

## 🛠️ Step-by-Step Breakdown

### 1. Getting the User Data

* **Purpose:** Collects the user's information (`Name`, `Email`, and `Password`).
* **First Cleaning Step:** Automatically trims extra spaces and turns all emails into lowercase right away. This prevents simple typos from causing bugs later on.

### 2. Checking the Rules

* **Purpose:** Acts as a quality check so bad or incomplete data doesn't get saved.
* **The Rules:**
  * **Name Check:** Needs to be at least 3 characters long.
  * **Email Check:** Must have an `@` symbol and a domain dot `.`.
  * **Password Check:** Must be at least 8 characters long, use both UPPER and lowercase letters, and include at least one special character (like `!` or `@`).

### 3. Saving Valid Users

* **Purpose:** Stores good, unique user accounts.
* **Storage:** Saves records as simple Python dictionaries inside a list (`registered_users`).
* **Duplicate Check:** Quickly scans existing emails before saving. If an email is already registered, it stops immediately so the same email can't be used twice.

### 4. Logging Failed Attempts

* **Purpose:** Keeps track of registration attempts that were rejected.
* **Storage:** Saves failed attempts into a separate list (`failed_registrations`).
* **Information Saved:** Stores the user's details along with the exact reason why they were rejected (like `"Duplicate email"` or `"Invalid user data"`).


### OUTPUT
<img width="766" height="400" alt="Screenshot 2026-08-14 084325" src="https://github.com/user-attachments/assets/cd5bcb7a-e27b-4811-b403-e65c94ee2c78" />


---

## ⚡ Tech Stack & Core Concepts Demonstrated

* **Language:** Python 3
* **Core Paradigms:** Functional Decomposition, Modular Architecture, Procedural Orchestration.
* **Data Engineering Concepts:** Ingestion Pipeline Design, Input Sanitization, Schema Standardization, Short-Circuit Evaluation (`any()`), and Audit Logging / Dead-Letter Quarantining.
* **Data Structures:** Dictionaries, List Collections, and Generator Expressions.

---

## 👨‍💻 About the Developer

I’m Timothy, a former banking documentation analyst who spent three years managing rigid data compliance and structure. I chose to pivot into the tech sector because I love building systems, wrestling with technical tools, and mastering business intelligence.

I am entirely self-taught through dedicated, project-driven bootcamps and courses. While I am still navigating the earlier stages of my career, I bring a high tolerance for debugging, a sharp eye for detail from my banking days, and a commitment to writing clean, reliable code.
