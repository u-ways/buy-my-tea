import sys
import time
import logging
from utils import select, decrypt_message
from os import environ
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from constant import IG_LOGIN_ENDPOINT, IG_COOKIE_BTN, IG_USERNAME_INPUT, IG_PASSWORD_INPUT, IG_LOGIN_BTN, \
    IG_TARGET_USER_ENV, IG_DONT_SAVE_LOGIN_BTN, TEN_SECONDS, IG_USERNAME_ENV, IG_TARGET_USER_WEBSITE, IG_PASSWORD_ENV, \
    FULL_NAME_ENV, DELIVERY_ADDRESS_ENV, FORM_PG2_NAME_INPUT, FORM_PG2_MOBILE_INPUT, FORM_PG2_DELIVERY_ADDRESS_INPUT, \
    FORM_PG1_CHOICE_MILK, FORM_PG1_CHOICE_MILK_AMOUNT_1, FORM_PG1_NEXT_PG_BTN, FORM_PG2_SUBMIT_BTN, MOBILE_ENV

# Environment variables (Stored in dictionary as calling environ is expensive)
ENV = dict(environ)

# Setting up our Logger
logging.basicConfig(filename=time.strftime("%Y-%m-%d") + ".log", level=logging.INFO)

"""
0. Initiate the webdriver that we will use to drive our browser
NOTE: If you don't have a webdriver installed, execute:
      sudo apt-get install chromium-chromedriver
      See: https://sites.google.com/a/chromium.org/chromedriver/home
"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)

"""
1. Login to our IG account.
"""
driver.get(IG_LOGIN_ENDPOINT)

select(using=driver, xpath=IG_COOKIE_BTN).click()
select(using=driver, xpath=IG_USERNAME_INPUT).send_keys(ENV.get(IG_USERNAME_ENV))
select(using=driver, xpath=IG_PASSWORD_INPUT).send_keys(decrypt_message(ENV.get(IG_PASSWORD_ENV)))
select(using=driver, xpath=IG_LOGIN_BTN).click()
select(using=driver, xpath=IG_DONT_SAVE_LOGIN_BTN).click()

"""
2. Go to our target's profile
"""
open_shop = False
open_shop_timeout = TEN_SECONDS * 60  # 1 hour timeout

while open_shop_timeout <= 0 or not open_shop:
    try:
        driver.get(ENV.get(IG_TARGET_USER_ENV))
        select(using=driver, xpath=IG_TARGET_USER_WEBSITE).click()
        open_shop = True
    except TimeoutException:
        open_shop_timeout -= 1
        time.sleep(TEN_SECONDS)  # Be a nice netizen, delay before trying again.

if open_shop_timeout <= 0:
    logging.info(time.strftime("%Y-%m-%d:%H-%M: ") + "Timed out on target profile's URL access. Perhaps the shop was "
                                                     "closed today. (The pre-order URL was not available within "
                                                     "script's activation timeline)")
    sys.exit()

"""
3. Fill the form with our usual choice, delivery details, and submit.
"""
try:
    select(using=driver, xpath=FORM_PG1_CHOICE_MILK).click()
    select(using=driver, xpath=FORM_PG1_CHOICE_MILK_AMOUNT_1).click()

    select(using=driver, xpath=FORM_PG1_NEXT_PG_BTN).click()

    select(using=driver, xpath=FORM_PG2_NAME_INPUT).send_keys(ENV.get(FULL_NAME_ENV))
    select(using=driver, xpath=FORM_PG2_MOBILE_INPUT).send_keys(ENV.get(MOBILE_ENV))
    select(using=driver, xpath=FORM_PG2_DELIVERY_ADDRESS_INPUT).send_keys(ENV.get(DELIVERY_ADDRESS_ENV))

    select(using=driver, xpath=FORM_PG2_SUBMIT_BTN).click()
except TimeoutException:
    logging.info(time.strftime("%Y-%m-%d:%H-%M: ") + "Timed out while trying to fill the order details. "
                                                     "Perhaps the shop was sold out?")

driver.close()
