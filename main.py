from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from aliveornotproxu import check_proxies
from proxu import lfproxies
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


alive_PROXY = check_proxies(lfproxies)

def find_element_with_retry(driver, by, value, max_retries=3):
    for _ in range(max_retries):
        try:
            element = driver.find_element(by=by, value=value)
            return element
        except NoSuchElementException:
            print("Element not found. Retrying with a different proxy.")
            return None

if alive_PROXY:
    for working_proxy in alive_PROXY:
        # Set up Chrome options with proxy and headers
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server={working_proxy}')

        # Add headers to mimic a real browser
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0")

# Set headers to mimic a typical browser request
        chrome_options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
        chrome_options.add_argument("accept-language=en-US,en;q=0.9")
        chrome_options.add_argument("referer=https://zap.gg/blox-fruits-stock?__cf_chl_tk=RSAivI0BP2GlFn86cEwwdhk7oTEUNkBEyXdo1vOO9DY-1706878701-0-gaNycGzNEpA")

# my headers to mimic human-like behavior
        chrome_options.add_argument("upgrade-insecure-requests=1")
        chrome_options.add_argument("sec-fetch-mode=navigate")
        chrome_options.add_argument("sec-fetch-site=same-origin")
        chrome_options.add_argument("sec-fetch-user=?1")
        chrome_options.add_argument("sec-fetch-dest=document")

        # Create the Chrome WebDriver instance with the configured options
        driver = webdriver.Chrome(options=chrome_options)

        try:

            driver.get('https://zap.gg')
            time.sleep(5)

            print(f'\033[91m🔵🔵🔵🔵Successfully bypassed CloudFlare Bot Detection with proxy:\033[0m', working_proxy)

            # Use the custom find_element_with_retry function
            dot = find_element_with_retry(driver, By.XPATH, '/html/body/div[2]/header/div[1]/div[1]/nav/div[1]/ul/li[4]/button')
            xlo = find_element_with_retry(driver, By.XPATH, '/html/body/div[2]/header/div[1]/div[1]/nav/div[2]/div/div/ul/li[2]/a')
            if dot:
                dot.click()
            elif xlo:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[1]/div[1]/nav/div[2]/div/div/ul/li[2]/a')))
                xlo.click()


            time.sleep(500)
        except Exception as e:
            print(f"Error with proxy {working_proxy}: {e}")
        finally:
            driver.quit()
    else:
        print("No working proxies found.")