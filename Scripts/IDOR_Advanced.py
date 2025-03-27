import requests
import itertools
from time import sleep

# Configuration
TARGET_URL = "https://example.com/api" #Insert URL containing API endpoints here.
HEADERS = {'Authorization': 'Bearer YOUR_TOKEN'}
USER_PAYLOADS = ['admin', 'manager', 'developer']
ORDER_PAYLOADS = ['order123', 'order456', 'order789']
PARAMS = ['user_id', 'order_id', 'cart_id']

def test_idor(target_url, param, payload):
    """Test for potential IDOR by replacing parameter with payload."""
    url = f"{target_url}?{param}={payload}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200 and 'admin' in response.text:
        print(f"[+] Potential IDOR found on {param}={payload} with status code {response.status_code}")
    else:
        print(f"[-] No IDOR found on {param}={payload} with status code {response.status_code}")

def advanced_scan():
    """Run advanced scan with brute force for hidden parameters."""
    print("[*] Starting Advanced IDOR Scan (Very High Security)")
    for param, payload in itertools.product(PARAMS, USER_PAYLOADS + ORDER_PAYLOADS):
        test_idor(TARGET_URL, param, payload)
        sleep(2)  # Slow down the requests for high security targets

if __name__ == "__main__":
    advanced_scan()
