import requests, datetime, json

class InstagramTokenGenerator():
    APP_ID = "312396031338333"
    APP_SECRET = "5c34cc26e0e9aae35356b87d47b15b86"
    REDIRECT_URI = "https://github.com/DubaiDigitalAcademy/socialaggregator"
    AUTHENTICATION_CODE = "AQCMVp36vH3fMceLMa_nvocj33JtBdHuKRMpc2TMw4HfNgfiuL5fsp8lt_jccyjsKrwiEXdHQboTJx5HPJ6ORNqLEGezM7b19GB8i8k7XddK_kh0u2RDxzIsPF50ZKILwULgpPyNVONujHID_Ci7d4hwKZhAcUTLl-CWUwUgiuWbL1p6P5r_xfuB0y7_LzF7gpJjLFnMAKRk1So_qX951I2rluIuFPdcmw5Eu2jLvsfToQ"
    SHORT_LIFE_TOKEN = "IGQWROMEhxWlFhN1FWWkg1R2p6YXRQLWFvclI5YjBMV1FVWUl1ajhKbS1zc0h2Mkl4NW9LYUZABQW1wb0pfTVJaOXI5cDJHQTl0Mk5vaEVsS29wVE83d19fNWQ0RGttdENWaUZAXOTVMSWpUSDdhSUo4UVNVMDFzV0o5dUtwdGZAaN1NmdwZDZD"
    LONG_LIFE_TOKEN = "IGQWRPUXRtNUx2eUdsRHZACLXVOdG5fU3JINERUU0hTTXJkWEw2d1ZAoMEpORkpVWml1dUZA5ZAzBYZAmVjMkRMOEFYcDlBUVExclhVRkVOQmJuVHdNam1vbktnQkFMUmt5SlRVUEJVMVc1eFNRdwZDZD"
    # CODE_GENERATION_DATE = datetime(2023, 9, 18)


    def swapShortLifeCodeForToken(self) -> None:
        response = requests.post(
            url = "https://api.instagram.com/oauth/access_token",
            data = {
                "client_id" : InstagramTokenGenerator.APP_ID,
                "client_secret" : InstagramTokenGenerator.APP_SECRET,
                "grant_type" : "authorization_code",
                "redirect_uri" : InstagramTokenGenerator.REDIRECT_URI,
                "code" : InstagramTokenGenerator.AUTHENTICATION_CODE
            }
        )
        json_response = json.loads(response.text)
        InstagramTokenGenerator.SHORT_LIFE_TOKEN = json_response["access_token"]


    def generateInitialLongLifeCode(self) -> any:
        response = requests.get(
        url = "https://graph.instagram.com/access_token?grant_type=ig_exchange_token&client_secret=5c34cc26e0e9aae35356b87d47b15b86&access_token=%s" % InstagramTokenGenerator.SHORT_LIFE_TOKEN
    )
        json_response = json.loads(response.text)
        # print(json_response)
        InstagramTokenGenerator.LONG_LIFE_TOKEN = json_response["access_token"]
    
    def refreshLongLivedToken(self) -> any:
        response = requests.get(
            url = "https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=IGQWRQWG5CMDAwa1V5RGgwOVpRd3FTRHRZANHdGMy0tcC1CN1E4MWw3N216Tmd2cjYxXzY1bXFZAakhlakdrZA1ZAQbi0tOU1hb3kwMTUtRkwtSkw5UGk5WjVKTDhiZA0Q1cllSOW15SDdoX05nQQZDZD",
        )

        return response.json
    
    def getLongLivedToken(self) -> str:
        return InstagramTokenGenerator.LONG_LIFE_CODE
    
    def getDateLongLifeTokenGenerated(self) -> datetime:
        return InstagramTokenGenerator.CODE_GENERATION_DATE
    
# igtg = InstagramTokenGenerator()

# igtg.swapShortLifeCodeForToken()

# igtg.generateInitialLongLifeCode()

# print(igtg.LONG_LIFE_TOKEN)
    


# igtg = InstagramTokenGenerator()

# igtg.generateInitialLongLifeCode()
    
    # //BUG: Fix datetime object for generated date - errors upon initialisation
    # //TODO: Handle refreshing the long lived token after 58 days
    # //TODO: Import and export of token plus generation date to file - shouldn't be hardcoded
    # //TODO: Current methods only return raw JSON. Data needs to be extracted properly