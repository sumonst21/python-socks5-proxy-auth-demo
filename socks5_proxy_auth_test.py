"""Script to test SOCKS5 proxy with username and password using requests library.

Test SOCKS5 proxy with username and password

This script demonstrates how to test a SOCKS5 proxy with username and password using the requests library.

Utilizes the following:
- requests: For making HTTP requests
- dotenv & os: For loading environment variables
- pathlib: For working with file paths
- httpbin: For testing the proxy

Usage:
    1. Install the required packages: pip install requests python-dotenv
    2. Create a proxy.env file with the following variables:
        PROXY_TYPE=socks5
        PROXY_HOST=123.456.789.012
        PROXY_PORT=1080
        PROXY_USER=username
        PROXY_PASS=password
    3. Run the script: python test_socks5_proxy.py
    4. Check the output for the IP address before and after the request

Tested with Python 3.8.0 & Python 3.12.1

Author: Sumon Islam <sumonst21@gmail.com>
Date: 2024-09-21
"""
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(Path(__file__).parent, "proxy.env")
load_dotenv(dotenv_path=dotenv_path)

# Get proxy settings from environment variables
type = os.getenv("PROXY_TYPE") # socks5
host = os.getenv("PROXY_HOST")
port = os.getenv("PROXY_PORT")
#proxy = os.getenv("PROXY")
proxy = f"{host}:{port}"
username = os.getenv("PROXY_USER")
password = os.getenv("PROXY_PASS")

proxy = {
    #"http": "socks5://username:password@123.456.789.012:1080",
    #"https": "socks5://username:password@123.456.789.012:1080"
    "http": f"{type}://{username}:{password}@{proxy}",
    "https": f"{type}://{username}:{password}@{proxy}"
}

try:
    print(f"Original IP: {requests.get('http://httpbin.org/ip').json()}")
    print(f"Proxied IP: {requests.get('http://httpbin.org/ip', proxies=proxy).json()}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
