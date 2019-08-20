import requests


def make_request():
    r = requests.get("https://httpbin.org/get")
    r.raise_for_status()
