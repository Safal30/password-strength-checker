📌 Overview
Python based Password Checker that validates user passwords against common security rules and blocks commonly used weak passwords.
Designed as a beginner to intermediate cybersecurity project.

🔐 Features
Minimum password length enforcement (10 characters)
Requires: 
    At least one uppercase letter
    At least one lowercase letter
    At least one digit
    At least one special characters

Blocks common passwords using an external text file
Case insensitive common password checking
Ignores empty lines and comments in the password list

📂 Project Structure
password_strength_checker/
│
├── main.py
├── common_pw.txt
└── README.md

▶️ How to Run
1. Install python 3
2. Place main.py and common_pw.txt in the same directory
3. Run the program:
``$$
`python main.py```
$$

📚 Learning Outcomes
File handling in Python
Set data structures for quick lookups
String manipulation and validation
Basic cybersecurity password policies