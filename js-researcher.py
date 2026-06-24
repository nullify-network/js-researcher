import requests
import sys
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urljoin
from colorama import init, Fore

init(autoreset=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
TIMEOUT = 15

print("\n [<3] JS Researcher.\n [<3] Coded by nullify-network\n")


def get_sources(url):
    try:
        if not urlparse(url).scheme:
            url = "https://" + url

        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if response.status_code != 200:
            print(" [-] Failed to retrieve page. Status code:", response.status_code)
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        sources = set()
        for script in soup.find_all("script", src=True):
            src = script.get("src")
            if re.search(r"\.js(\?|$)", src):
                sources.add(urljoin(url, src))
        for link in soup.find_all(href=True):
            href = link.get("href")
            if re.search(r"\.js(\?|$)", href):
                sources.add(urljoin(url, href))
        return sources
    except Exception as e:
        print("An error occurred:", str(e))
        return None


def find_endpoints_in_js(js_url):
    try:
        response = requests.get(js_url, headers=HEADERS, timeout=TIMEOUT)
        if response.status_code != 200:
            print(" [-] Failed to retrieve JS file:", Fore.RED + js_url,
                  "Status code:", response.status_code)
            return None

        endpoints = set()
        for match in re.findall(r"""["'](/[a-zA-Z0-9_\-./?=&%]+)["']""", response.text):
            endpoints.add(match)
        return endpoints
    except Exception as e:
        print(" [-] An error occurred while processing JS file:",
              Fore.RED + js_url, str(e))
        return None


def clean_url(url):
    return url.rstrip("/")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 js-researcher.py <target>")
        sys.exit(1)

    target_url = clean_url(sys.argv[1])
    sources = get_sources(target_url)
    if sources:
        print(" [+] Sources found on", Fore.BLUE + target_url, ":")
        for source in sources:
            print("  [+] Checking ", Fore.GREEN + source, ":")
            endpoints = find_endpoints_in_js(source)
            if endpoints:
                for endpoint in sorted(endpoints):
                    print(Fore.YELLOW + "   [+]> " + endpoint)
            else:
                print("  [-] No endpoints found in", Fore.RED + source)
    else:
        print("  [-] No sources found on", Fore.BLUE + target_url)
