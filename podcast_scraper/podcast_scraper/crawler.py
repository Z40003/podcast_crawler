from importlib.resources import contents
import requests


url = "https://api.omny.fm/orgs/e73c998e-6e60-432f-8610-ae210140c5b1/clips/e1022bce-b9fc-4ad7-9e5f-b34a01884f5e/transcript?format=JSON&speakers=true"

headers = {
    "User-Agent" : ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/139.0.0.0 Safari/537.36"),
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "referer" : "https://omny.fm/",
    "Connection" : "keep-alive",
}

cookies = {
    "geo": "F1=1",
    "media-user-token": "AinXyR7BohUF/BpnkK3rS1vtHjJJyC4yIbkUz9XSKlYP8bdZehQ15sn1Ri19YUeJfGQvAYwwnWjPoW1IaDd64dx/GvspFIzV1+pknW+j+8243+55+w/ldOp2IOeFreeHKtjY4OuUzhqnQZZeEWgxNX/kJvSxJi1b4SP/PXZjVNHNHOzo34aAkkRq6vS+M3Orz2PCgdF8Qg64++QGvATtN3sjkphUVsf1aPIpz5khkIflNoBwUQ==",
}

proxies = {
    "http" : "http://127.0.0.1:7897",
    "https" : "http://127.0.0.1:7897",
}

response = requests.get(url, headers=headers, cookies=cookies, proxies=proxies, timeout=30, verify=False)


