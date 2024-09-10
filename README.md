# MassMail-Marketing-Experiment

## Overview
The **MassMail-Marketing-Experiment** project is designed to send bulk emails to a list of students, promoting Microsoft Learn resources. The tool utilizes Python's `smtplib` to send emails while ensuring that each email is unique to reduce the chances of being marked as spam only for fun purposes.

## Features
- Sends personalized emails to a specified range of student email addresses.
- Randomly selects greetings for each email to enhance uniqueness.
- Configurable email content and subject.
- Implements delays between emails to avoid triggering spam filters.

## Requirements
- Python 3.x
- Required libraries:
  - `smtplib`
  - `email`
  - `time`
  - `random`

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MassMail-Marketing-Experiment.git
   cd MassMail-Marketing-Experiment
   ```

2. Update the `config.py` file with the starting and ending roll numbers:
   ```python
   starting_roll_number
   ending_roll_number
   ```

3. Update the email account credentials in `main.py`:
   ```python
   sender_email = "your_email@gmail.com"
   password = "your_password"
   ```

4. Ensure you have allowed "Less secure app access" in your Gmail account settings if using Gmail.

## Usage
To send emails, run the `main.py` script:
