import requests

TARGET_URL = "https://example.com/api" #Insert URL containing API endpoints here.
HEADERS = {'Authorization': 'Bearer YOUR_TOKEN'}
COMMON_PAYLOADS = ['user1', 'user2', 'guest', 'admin']
ORDER_PAYLOADS = ['order123', 'order456']
PARAMS = ['user_id', 'order_id', 'session_id']

def test_idor(target_url, param, payload):
    """Test for potential IDOR."""
    url = f"{target_url}?{param}={payload}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print(f"[+] Potential IDOR found on {param}={payload}")
    else:
        print(f"[-] No IDOR found on {param}={payload}")

def regular_scan():
    """Run a regular scan for IDOR vulnerabilities."""
    print("[*] Starting RegularScan IDOR Scan (Medium Security)")
    for param in PARAMS:
        for payload in COMMON_PAYLOADS + ORDER_PAYLOADS:
            test_idor(TARGET_URL, param, payload)

if __name__ == "__main__":
    regular_scan()
