import requests

# Configuration
TARGET_URL = "https://example.com/api"
HEADERS = {'Authorization': 'Bearer YOUR_TOKEN'}
PAYLOADS = ['1', '2', '3', 'test', 'admin']
PARAMS = ['user_id', 'product_id']

def test_idor(target_url, param, payload):
    """Test for potential IDOR."""
    url = f"{target_url}?{param}={payload}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print(f"[+] Potential IDOR found on {param}={payload}")
    else:
        print(f"[-] No IDOR found on {param}={payload}")

def quick_scan():
    """Run a quick scan with limited payloads."""
    print("[*] Starting QuickScan IDOR Scan (Lowest Security)")
    for param in PARAMS:
        for payload in PAYLOADS:
            test_idor(TARGET_URL, param, payload)

if __name__ == "__main__":
    quick_scan()
