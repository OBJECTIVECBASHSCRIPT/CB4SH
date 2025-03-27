import requests
import json

# Configuration
TARGET_URL = "https://example.com/api" #Insert URL containing API endpoints here.
HEADERS = {'Authorization': 'Bearer YOUR_TOKEN'}
USER_IDS = ['1', '2', '3', '9999', '10000']
ORDER_IDS = ['123', '234', '345', '9999']
PARAMS = ['user_id', 'order_id']

def test_idor(target_url, param, payload):
    """Test for IDOR vulnerability."""
    url = f"{target_url}?{param}={payload}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200 and "forbidden" not in response.text.lower():
        print(f"[+] Potential IDOR found: {url}")
    else:
        print(f"[-] No IDOR found: {url}")

def deep_scan():
    """Run a deep scan with a combination of user and order IDs."""
    print("[*] Starting DeepScan IDOR Scan (High Security)")
    for param in PARAMS:
        for payload in USER_IDS + ORDER_IDS:
            test_idor(TARGET_URL, param, payload)

if __name__ == "__main__":
    deep_scan()
