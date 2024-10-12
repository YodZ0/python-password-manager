# Password Manager Application

This is a simple password manager application built with DearPyGui and SQLite. It allows you to view, add, and generate secure passwords, and all data is stored locally in a SQLite database.

## Features

The application consists of three main tabs:

### 1. Passwords (Tab 1 - Passwords)
- **View Resources:** Displays a table containing the saved resources, including:
  - `Source` (website or app name)
  - `Login` (username or email)
  - `Password`
- **Copy Password to Clipboard:** Clicking on a row in the table automatically copies the password from that row to the clipboard for easy use.

### 2. Create a New Record (Tab 2 - Create)
- **Add New Record:** This tab contains a form with fields to add a new entry:
  - `Source` (e.g., website or app name)
  - `Login` (username or email)
  - `Password`
- **Automatic Table Update:** Once a new entry is added using the form, the password table on the `Passwords` tab updates automatically to include the new record.

### 3. Password Generator (Tab 3 - Generate)
- **Generate a Secure Password:** This tab provides a form to generate a random and secure password with customizable options:
  - Four checkboxes to include/exclude specific character types (e.g., uppercase, lowercase, numbers, special characters).
  - A slider to adjust the length of the generated password.
- **Generated Password:** The generated password can be copied to the clipboard for immediate use.

## Additional Features
- **Local Database:** The application uses a local SQLite database to store all password entries. The database is automatically created when you run the application for the first time if it does not already exist.

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Required Python packages:
  - `dearpygui`
  - `sqlite3`
  - `pyperclip`

You can install the necessary packages using pip:
```bash
pip install dearpygui pyperclip
