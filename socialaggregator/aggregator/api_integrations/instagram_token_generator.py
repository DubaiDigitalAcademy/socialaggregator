import requests, datetime, json

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class InstagramBasicTokenGenerator():
    APP_ID = "312396031338333"
    APP_SECRET = "5c34cc26e0e9aae35356b87d47b15b86"
    REDIRECT_URI = "https://github.com/DubaiDigitalAcademy/socialaggregator"
    AUTHENTICATION_CODE = "AQAkViPH5h_HQxZVIjhcLHwCHq8OKUwFG5oB5CHsUiALO-HRTwH_RFhHPKu39zYCg9UlJhtUtiFBpBt3El2uaxKmsefa_PWpxDel1S8sp_aKbXWNkybrAIVfevj-C3-VPmRL0e7TjigL1oI6qqlVQfpvDmR0m9ZKq-H71f2b2Jg0aXDKjAtReEDjqDMCa6Wk0XWtjCBfSbB0SwIQIjzGWCIZS-mqDKGuZjMrBsfKBSzOpQ"
    SHORT_LIFE_TOKEN = "IGQWROMEhxWlFhN1FWWkg1R2p6YXRQLWFvclI5YjBMV1FVWUl1ajhKbS1zc0h2Mkl4NW9LYUZABQW1wb0pfTVJaOXI5cDJHQTl0Mk5vaEVsS29wVE83d19fNWQ0RGttdENWaUZAXOTVMSWpUSDdhSUo4UVNVMDFzV0o5dUtwdGZAaN1NmdwZDZD"
    LONG_LIFE_TOKEN = "IGQWRPdENlY0o4UG5CZAmw4S05ncGR6bGdpaW9VMWRfRVFTSmQzSEIya1BPUnpIT19OUzRrYzd6SF94NmRRaGViOVRUZATJWT183SUwtbEVVLTRXdG9fYm5sOVhtcG1STVVmdUJNWW56UXlydwZDZD"
    USER_ID_NUM = "6709081349147497"
    # CODE_GENERATION_DATE = datetime(2023, 9, 18)

    def getUserIdNumber(self) -> str:
        response = requests.post(
            url = "https://api.instagram.com/oauth/access_token",
            data = {
                "client_id" : InstagramBasicTokenGenerator.APP_ID,
                "client_secret" : InstagramBasicTokenGenerator.APP_SECRET,
                "grant_type" : "authorization_code",
                "redirect_uri" : InstagramBasicTokenGenerator.REDIRECT_URI,
                "code" : InstagramBasicTokenGenerator.AUTHENTICATION_CODE
            }
        )

        json_response = json.loads(response.text)
        print(json_response)
        # InstagramBasicTokenGenerator.USER_ID_NUM = json_response["user_id"]

    def swapShortLifeCodeForToken(self) -> None:
        response = requests.post(
            url = "https://api.instagram.com/oauth/access_token",
            data = {
                "client_id" : InstagramBasicTokenGenerator.APP_ID,
                "client_secret" : InstagramBasicTokenGenerator.APP_SECRET,
                "grant_type" : "authorization_code",
                "redirect_uri" : InstagramBasicTokenGenerator.REDIRECT_URI,
                "code" : InstagramBasicTokenGenerator.AUTHENTICATION_CODE
            }
        )
        json_response = json.loads(response.text)
        InstagramBasicTokenGenerator.SHORT_LIFE_TOKEN = json_response["access_token"]


    def generateInitialLongLifeCode(self) -> any:
        response = requests.get(
        url = "https://graph.instagram.com/access_token?grant_type=ig_exchange_token&client_secret=5c34cc26e0e9aae35356b87d47b15b86&access_token=%s" % InstagramBasicTokenGenerator.SHORT_LIFE_TOKEN
    )
        json_response = json.loads(response.text)
        # print(json_response)
        InstagramBasicTokenGenerator.LONG_LIFE_TOKEN = json_response["access_token"]
    
    def refreshLongLivedToken(self) -> any:
        response = requests.get(
            url = "https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=IGQWRQWG5CMDAwa1V5RGgwOVpRd3FTRHRZANHdGMy0tcC1CN1E4MWw3N216Tmd2cjYxXzY1bXFZAakhlakdrZA1ZAQbi0tOU1hb3kwMTUtRkwtSkw5UGk5WjVKTDhiZA0Q1cllSOW15SDdoX05nQQZDZD",
        )

        return response.json
    
    def getLongLivedToken(self) -> str:
        return InstagramBasicTokenGenerator.LONG_LIFE_CODE
    
    def getDateLongLifeTokenGenerated(self) -> datetime:
        return InstagramBasicTokenGenerator.CODE_GENERATION_DATE
    
# igtg = InstagramBasicTokenGenerator()

# igtg.swapShortLifeCodeForToken()

# igtg.generateInitialLongLifeCode()

# print(igtg.LONG_LIFE_TOKEN)

# igtg.getUserIdNumber()
# print(igtg.USER_ID_NUM)
    


# igtg = InstagramTokenGenerator()

# igtg.generateInitialLongLifeCode()
    
    # //BUG: Fix datetime object for generated date - errors upon initialisation
    # //TODO: Handle refreshing the long lived token after 58 days
    # //TODO: Import and export of token plus generation date to file - shouldn't be hardcoded
    # //TODO: Current methods only return raw JSON. Data needs to be extracted properly