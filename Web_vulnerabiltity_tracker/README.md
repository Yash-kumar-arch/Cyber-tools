# Web Security Header Scanner

A Python-based tool for analyzing HTTP response headers to detect common web security misconfigurations.
This project focuses on evaluating the `X-Frame-Options` header to identify clickjacking protection issues.

---

## Overview
This tool sends an HTTP request to a target URL and analyzes the response headers.
It checks whether the `X-Frame-Options` header is properly configured and classifies the security status based on its value.

---

## Features
- Checks for `X-Frame-Options` header presence
- Classifies security status:
  - **OK**: Properly configured (`DENY` / `SAMEORIGIN`)
  - **WEAK**: Header exists but has weak or non-standard value
  - **MISSING**: Header is not present
- Provides structured output including:
  - Header name
  - Status
  - Severity level
  - Descriptive message

---

## How to run
python web_security_scanner.py

---

## Requirements
- Python 3.x
- requests library — pip install requests

---

## Skills used
Python, HTTP Requests, Web Security, Header Analysis

Install dependencies:

```bash
pip install requests
