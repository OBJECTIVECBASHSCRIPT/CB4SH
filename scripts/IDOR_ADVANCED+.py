import requests
import itertools
from time import sleep

# Configuration
TARGET_URL = "https://example.com/api"
HEADERS = {'Authorization': 'Bearer YOUR_TOKEN'}
PAYLOADS = ['admin', 'root', 'user', 'testuser', '12345', 'invalid']
PARAMS = ['user_id', 'product_id', 'order_id']

def test_idor(target_url, param, payload):
    """Test for potential IDOR by replacing parameter with payload."""
    url = f"{target_url}?{param}={payload}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print(f"[+] Potential IDOR found on {param}={payload} with status code {response.status_code}")
    else:
        print(f"[-] No IDOR found on {param}={payload} with status code {response.status_code}")

def advanced_scan():
    """Run advanced scan with multiple payloads and parameters."""
    print("[*] Starting Advanced+ IDOR Scan (Maximum Security)")
    for param, payload in itertools.product(PARAMS, PAYLOADS):
        test_idor(TARGET_URL, param, payload)
        sleep(1)  # To prevent rate limiting

if __name__ == "__main__":
    advanced_scan()
