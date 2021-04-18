TEN_SECONDS = 10

DEFAULT_KEY_FILENAME = "secret.key"
DEFAULT_PASSWORD_FILENAME = "encrypted.password"

IG_USERNAME_ENV = "IG_USERNAME"
IG_PASSWORD_ENV = "IG_PASSWORD"
IG_TARGET_USER_ENV = "IG_TARGET_USER"

IG_ENDPOINT = "https://www.instagram.com/"
IG_LOGIN_ENDPOINT = IG_ENDPOINT + "accounts/login/"
IG_COOKIE_BTN = '/html/body/div[2]/div/div/div/div[2]/button[1]'
IG_USERNAME_INPUT = '//*[@id="loginForm"]/div/div[1]/div/label/input'
IG_PASSWORD_INPUT = '//*[@id="loginForm"]/div/div[2]/div/label/input'
IG_LOGIN_BTN = '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button'
IG_DONT_SAVE_LOGIN_BTN = '//*[@id="react-root"]/section/main/div/div/div/div/button'
IG_TARGET_USER_WEBSITE = '//*[@id="react-root"]/section/main/div/header/section/div[2]/a'
