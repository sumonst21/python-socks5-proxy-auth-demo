# python-socks5-proxy-auth-demo

## SOCKS5 Proxy Authentication Demo

This script demonstrates how to test a SOCKS5 proxy with a username and password using the `requests` library.

### Dependencies
The script requires the following libraries:
- `requests`: For making HTTP requests.
- `dotenv` and `os`: For loading environment variables.
- `pathlib`: For working with file paths.
- `httpbin`: For testing the proxy connection.

### Usage

1. **Install the required packages:**

   ```bash
   pip install requests requests[socks] python-dotenv
   ```

2. **Set up your proxy environment variables:**

   Create a file named `proxy.env` in the same directory as the script with the following variables:

   ```
   PROXY_TYPE=socks5
   PROXY_HOST=123.456.789.012
   PROXY_PORT=1080
   PROXY_USER=username
   PROXY_PASS=password
   ```

3. **Run the script:**

   ```bash
   python socks5_proxy_auth_test.py
   ```

4. **Check the output:**
   The output will display the IP address before and after the request, allowing you to verify if the proxy is functioning correctly.

### Compatibility

Tested with:
- Python 3.8.0
- Python 3.12.1

### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

### Author
Sumon Islam  
<sumonst21@gmail.com>

### Date
2024-09-21
