# 🔐 Password Security Analyzer

**Password Security Analyzer** is a Streamlit-based web app that helps users check the strength of their passwords, 
detect if they’ve been leaked in data breaches, and generate secure hash versions of the password using popular algorithms.

--

## 🚀 Features

- ✅ **Password Strength Analysis**  
  Evaluates complexity, length, and character diversity (uppercase, digits, symbols, etc.).

- 🔍 **Breach Check**  
  Uses the [HaveIBeenPwned](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange) API to see if your password appears in known breaches using k-anonymity (partial SHA-1).

- 🔐 **Hash Generator**  
  Converts password into multiple secure hash formats: `MD5`, `SHA-1`, `SHA-256`, `SHA-512`.

- 🌐 **User Interface**  
  Built with [Streamlit](https://streamlit.io/) for a responsive and interactive web interface.

---

## 📦 Installation

### 💻 Local Setup

---
# Clone the repository
~~~
git clone https://github.com/passhunter/password-analyzer.git
cd password-analyzer 
~~~
# (Optional) Create a virtual environment
~~~
python -m venv .venv
source .venv/Scripts/activate # Windows
~~~ 
# Install dependencies
~~~
pip install -r requirements.txt
~~~
# Run the app
~~~
streamlit run gui_app.py
~~~

📄 Requirements
Python 3.8+
streamlit
requests

📜 License
MIT License © 2025 Ayush Madavi

🙋‍♂️ Author
Ayush Madavi
🎯 Cybersecurity Enthusiast | Password Hunter
🔗 GitHub: passhunter




