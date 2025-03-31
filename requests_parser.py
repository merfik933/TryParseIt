import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9"
}

def try_parse(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        print(f"Successfully fetched {url} using requests.")
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None