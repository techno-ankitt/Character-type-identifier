fucntion add krn hai kal, aur ek one liner description bhi , okkkkk Doneee bhayi


# Character Type Checker

A lightweight Python utility to determine the category of any single character input. This script uses ASCII range comparisons to categorize characters efficiently.

## 🚀 Features----
- **Uppercase Detection:** Recognizes 'A' through 'Z'.
- **Lowercase Detection:** Recognizes 'a' through 'z'.
- **Digit Identification:** Recognizes numbers from '0' through '9'.
- **Special Character Support:** Identifies symbols like `@`, `#`, `$`, `%`, etc.
- **Input Validation:** Ensures the user enters exactly one character.

## 🛠️ How it Works----
The program checks the input against three main conditions using conditional logic:
1. **Alphabetic Check:** Using range comparison for both cases.
2. **Numeric Check:** Using digit range comparison.
3. **Fallback:** Any character that doesn't fit the above is classified as a Special Character.

## 💻 Usage----
1. Run the script using Python:
   ```bash
   python main.py
