import requests


def get_crypto_prices(crypto_ids):
    #get_crypto_prices(["bitcoin", "ethereum"])
    ids_string = ",".join(crypto_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids_string}&vs_currencies=brl"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return{}
    except requests.RequestException:
        return{}
  