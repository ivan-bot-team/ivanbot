import requests


async def load_config(url):
    config = requests.get(f'{url}/api/v1/bot/config').json()['data']
    return config
