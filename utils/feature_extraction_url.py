import re
import pandas as pd
from urllib.parse import urlparse
from .load_top_domains import load_top_domains

TOP_DOMAINS = load_top_domains("tranco_8L2QV.csv")

def extract_features(url):
    features = []

    # Parse the URL
    parsed = urlparse(url)
    hostname = parsed.netloc.lower()
    scheme = parsed.scheme.lower()

    # Basic length-based features
    features.append(len(url))                  # Full URL length
    features.append(len(parsed.netloc))        # Domain length
    features.append(len(parsed.path))          # Path length

    # Special character counts
    special_chars = ['@', '?', '-', '=', '.', '#', '%', '+', '$', '!', '*', ',', '&']
    features.extend([url.count(c) for c in special_chars])

    # Malicious keyword indicators
    keywords = ['alert', 'script', 'onerror', 'onload', 'select', 'drop', 'union', '--', 'insert']
    features.extend([1 if kw in url.lower() else 0 for kw in keywords])

    features.append(sum(c.isdigit() for c in url))
    features.append(sum(c.isupper() for c in url))

    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    features.append(1 if ip_pattern.fullmatch(hostname) else 0)

    features.append(hostname.count('.'))

    features.append(1 if scheme == 'https' else 0)

    root_domain = hostname.split(':')[0]
    if root_domain.startswith("www."):
        root_domain = root_domain[4:]
    features.append(1 if root_domain in TOP_DOMAINS else 0)

    return features