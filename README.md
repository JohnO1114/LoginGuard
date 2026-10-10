LoginGuard — Security Log Analyzer
Overview

LoginGuard is a beginner Python cybersecurity project that analyzes login records and detects repeated failed login attempts.
Features

    Reads login records from login.log
    Counts successful and failed logins
    Skips malformed log entries
    Flags IP addresses with three or more failed attempts
    Generates a security report

Technologies

    Python 3
    collections.Counter
    File handling and string processing

How to Run

    Place analyzer.py and login.log in the same directory.
    Open a terminal in that directory.
    Run python3 analyzer.py.

Detection Rule

An alert is generated when an IP address has at least three failed login attempts.
Limitations

This is a beginner learning project using supplied log data. Repeated failed attempts may be suspicious but do not prove an attack. The program does not monitor live network traffic.

Status: Initial version completed.
