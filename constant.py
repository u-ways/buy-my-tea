TEN_SECONDS = 10

DEFAULT_KEY_FILENAME = "secret.key"
DEFAULT_PASSWORD_FILENAME = "encrypted.password"

# IG PERSONAL DETAILS
IG_USERNAME_ENV = "IG_USERNAME"
IG_PASSWORD_ENV = "IG_PASSWORD"
# IG TARGET (SHOP) PROFILE
IG_TARGET_USER_ENV = "IG_TARGET_USER"
# REQUIRED DELIVERY DETAILS
FULL_NAME_ENV = "FULL_NAME"
MOBILE_ENV = "MOBILE"
DELIVERY_ADDRESS_ENV = "DELIVERY_ADDRESS"

# IG FLOW TO ACCESS TARGET USER WEBSITE URL (A Google form in our case)
IG_ENDPOINT = "https://www.instagram.com/"
IG_LOGIN_ENDPOINT = IG_ENDPOINT + "accounts/login/"
IG_COOKIE_BTN = '/html/body/div[2]/div/div/div/div[2]/button[1]'
IG_USERNAME_INPUT = '//*[@id="loginForm"]/div/div[1]/div/label/input'
IG_PASSWORD_INPUT = '//*[@id="loginForm"]/div/div[2]/div/label/input'
IG_LOGIN_BTN = '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button'
IG_DONT_SAVE_LOGIN_BTN = '//*[@id="react-root"]/section/main/div/div/div/div/button'
IG_TARGET_USER_WEBSITE = '//*[@id="react-root"]/section/main/div/header/section/div[2]/a'

# PAGE ONE (TEA SELECTION)
# Milk tea
FORM_PG1_CHOICE_MILK = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]'
FORM_PG1_CHOICE_MILK_AMOUNT_1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]'
# Chocolate hazelnut tea
FORM_PG1_CHOICE_HAZELNUT = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]'
FORM_PG1_CHOICE_HAZELNUT_AMOUNT_1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]'
# Mango matcha green tea
FORM_PG1_CHOICE_MANGO = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]'
FORM_PG1_CHOICE_MANGO_AMOUNT_1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]'
# Lychee jasmine green tea
FORM_PG1_CHOICE_LYCHEE = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]'
FORM_PG1_CHOICE_LYCHEE_AMOUNT_1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[3]'
# Creamy grass jelly tea
FORM_PG1_CHOICE_CREAMY = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]'
FORM_PG1_CHOICE_CREAMY_AMOUNT_1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[2]/div[3]'

FORM_PG1_NEXT_PG_BTN = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span'

# PAGE TWO (DELIVERY DETAILS)
FORM_PG2_NAME_INPUT = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
FORM_PG2_MOBILE_INPUT = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
FORM_PG2_DELIVERY_ADDRESS_INPUT = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
FORM_PG2_SUBMIT_BTN = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span'
