# Password Strength Checker (Python)

## 📌 Overview <br>
Python based Password Checker that validates user passwords against common security rules and blocks commonly used weak passwords.  
Designed as a beginner to intermediate cybersecurity project.

## 🔐 Features <br>
- Minimum password length enforcement (10 characters)  
- Requires:  
  - At least one uppercase letter  
  - At least one lowercase letter  
  - At least one digit  
  - At least one special character  
- Blocks common passwords using an external text file  
- Case insensitive common password checking  
- Ignores empty lines and comments in the password list  

## 📂 Project Structure <br>
<pre>
password_strength_checker/
│
├── main.py
├── common_pw.txt
└── README.md
</pre>

## ▶️ How to Run <br>
1. Install Python 3  
2. Place `main.py` and `common_pw.txt` in the same directory  
3. Run the program:  
<pre><code>python main.py</code></pre>

## 📚 Learning Outcomes <br>
- File handling in Python  
- Set data structures for quick lookups  
- String manipulation and validation  
- Basic cybersecurity password policies  
