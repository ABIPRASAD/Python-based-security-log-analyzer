# Python Security Log Analyzer

A Python-based cybersecurity project that analyzes authentication logs, identifies failed login events, counts failed attempts, summarizes usernames, and exports reports in CSV and JSON formats.

## Features

- Reads authentication log files
- Filters failed login events
- Counts failed login attempts
- Summarizes usernames associated with failed events
- Exports reports to CSV and JSON
- Handles common file-reading errors

## Technologies Used

- Python
- File handling and `pathlib`
- CSV and JSON modules
- Exception handling
- Git and GitHub

## Project Structure

python-security-log-analyzer/

├── log_analyzer.py

├── security.log

├── security_report.csv

├── security_report.json

├── README.md

└── .gitignore


## How to Run

1. Install Python 3 if it is not already installed.
2. Open a terminal in the project directory.
3. Run:

bash
python log_analyzer.py


The script reads `security.log`, analyzes failed login events, and generates CSV and JSON reports.

## Sample Data

This project uses fictional authentication log entries for educational purposes.

## Limitations

The script assumes a specific log format and extracts the username from the final whitespace-separated field of a failed login entry. It is intended for learning and demonstration, not production security monitoring.

## Purpose

Built to strengthen Python programming, file handling, log analysis, and cybersecurity automation skills.
