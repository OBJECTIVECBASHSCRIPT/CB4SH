import requests
from bs4 import BeautifulSoup
import re

# Replace with your actual live domains or load from file
TARGETS = [
    "https://www.kinder.com",
    "https://www.halotop.com",
    "https://dev.halotop.com",
    "https://www.bluebunny.com",
    "https://dev.bluebunny.com",
    "https://www.babyruth.com"
]

def extract_js_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    script_tags = soup.find_all("script", src=True)
    js_urls = []

    for tag in script_tags:
        src = tag['src']
        if src.startswith("http"):
            js_urls.append(src)
        elif src.startswith("/"):
            js_urls.append(base_url + src)

    return js_urls

def extract_endpoints_from_js(js_text):
    # Regex to find URL-like strings
    patterns = [
        r'\/[a-zA-Z0-9\/\-\._]+\.php',
        r'\/[a-zA-Z0-9\/\-\._]+\.json',
        r'\/[a-zA-Z0-9\/\-\._]+',
    ]
    found = set()
    for pattern in patterns:
        found.update(re.findall(pattern, js_text))
    return list(found)

def main():
    for target in TARGETS:
        print(f"\n[INFO] Crawling {target}")
        try:
            res = requests.get(target, timeout=10)
            js_links = extract_js_links(res.text, base_url=target)
            print(f"  [FOUND] {len(js_links)} JS files")

            for js_url in js_links:
                try:
                    js_res = requests.get(js_url, timeout=10)
                    endpoints = extract_endpoints_from_js(js_res.text)
                    if endpoints:
                        print(f"    [FOUND] {len(endpoints)} endpoints in {js_url}")
                        for ep in endpoints:
                            print(f"      {ep}")
                except:
                    print(f"    [ERROR] Failed to fetch {js_url}")
        except:
            print(f"[ERROR] Failed to fetch {target}")

if __name__ == "__main__":
    main()
