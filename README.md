# Ransomware Demonstration in Python

## Overview

This Python script serves as an educational demonstration of how ransomware operates. It should be noted that the purpose of this script is purely educational and should never be used for malicious purposes.

## Functionality

- The script utilizes the **Fernet library** to perform encryption and decryption operations.
- It lists all files in the project's root directory, excluding the files that are part of the program itself.
- After listing the files, it generates an encryption key and encrypts all identified files, making them inaccessible.
- The program then asks the user a question. If answered correctly, the files are decrypted using the previously generated key.

## Important Notice

<span style="color:red; font-size:1.2em;">**WARNING:** This script should only be run in a controlled environment. It is advisable to use a virtual machine or a directory that does not contain important files. Misuse of this script can lead to irreversible data loss. Please exercise extreme caution.</span>

## Educational Purpose

The intention of this demonstration is to illustrate the potential harm of ransomware and to emphasize the importance of cybersecurity measures. It is a valuable tool for understanding the mechanisms of malicious software and enhancing defense strategies against cyber threats.

## Prerequisites

- Python 3.0

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/davidcastagnetoa/malo_malisimo.git
   cd malo_malisimo
   ```

2. **Set up a virtual environment** (optional, but recommended):

   ```bash
   python -m venv venv
   ```

   - On Unix-based systems (Linux/macOS):

     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     source ./venv/Scripts/activate
     ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Execution

<span style="color:red; font-size:1em;">Please!, do not forget to take extreme precautions before running it.</span> Once everything is set up, you can run the application with:

```bash
python main.py
```

If you want to create a .exe file run the next command.

```bash
python setup.py bdist_msi
```
