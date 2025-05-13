import requests

BASE_URL = "https://www.vodafone.om/index.php?page="

for page_id in range(1, 11):
    url = BASE_URL + str(page_id)
    print(f"Testing URL: {url}")

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response Length: {len(response.text)}\n")
