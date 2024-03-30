from proxu import lfproxies
import requests
from logger import error_log, logging
from requests.exceptions import ConnectTimeout

error_log(f"Starting proxy check", log_level=logging.DEBUG)

def check_proxies(proxies):
    alive_proxies = []
    for proxy in proxies:
        try:
            # Include your IP address in the proxy URL
            proxy_with_auth = f'http://161.0.159.104@{proxy}'  # Replace '161.0.159.104' with your actual IP
            
            # Create a session with a rotating proxy
            session = requests.Session()
            session.proxies = {'http': proxy_with_auth, 'https': proxy_with_auth}

            # Perform a request with the session
            response = session.get('https://www.google.com', timeout=8)

            if response.status_code == 200:
                print(f'Proxy {proxy} is alive.')
                alive_proxies.append(proxy)
                error_log(f"Proxy {proxy} is alive. HTTP {response.status_code}", log_level=logging.INFO)
            else:
                error_log(f"There was an error using the proxy {proxy}. HTTP {response.status_code}", log_level=logging.WARNING)
                print(f'Proxy {proxy} returned a non-200 status code.')
        except requests.RequestException as e:
            error_log(f'Error with proxy {proxy}: {e}\n', log_level=logging.ERROR)
            print(f'Error with proxy {proxy}: {e}\n')
            continue  # Continue with the next proxy if an error occurs

    return alive_proxies




