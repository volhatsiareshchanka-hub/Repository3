# 4. Enum окружений и маппинг на URL

from enum import Enum

class Environment(Enum):
    DEV = "https://dev.example.com"
    STAGE = "https://stage.example.com"
    PROD = "https://example.com"

def get_base_url(url):
    if url == Environment.DEV:
        return Environment.DEV
    elif url == Environment.PROD:
        return Environment.PROD

print(get_base_url(Environment.DEV)) # https://dev.example.com
print(get_base_url(Environment.PROD)) # https://prod.example.com

