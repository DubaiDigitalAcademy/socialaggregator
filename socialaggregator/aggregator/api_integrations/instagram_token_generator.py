import requests, datetime

class InstagramTokenGenerator():
    CLIENT_ID = "312396031338333"
    CLIENT_SECRET = "5c34cc26e0e9aae35356b87d47b15b86"
    REDIRECT_URI = "https://github.com/DubaiDigitalAcademy/socialaggregator"
    SHORT_LIFE_CODE = "AQBs6l07saU08fOHeiyY3rlZJ3mB1-7pZbjmuSuxyMliROtFVPSXMSG5fD7fGiVuRyVUFm8NSkCTLt8AoYWg_aGXMSnZSIBA0hXFhc3K4Xq4dluXk2cbibFrmX_Ip16HxHx3qr-VMAafWz0gpswZ8sUS3Knw6nvVXmcwG3efpqwc1QB73ZfPs5lVY9zmbPPIrODMNDbJKk0Cq7J5WTJu8I3WXyaMQS1qk0zMzhnNIVT_8w"
    LONG_LIFE_CODE = "IGQWRQWG5CMDAwa1V5RGgwOVpRd3FTRHRZANHdGMy0tcC1CN1E4MWw3N216Tmd2cjYxXzY1bXFZAakhlakdrZA1ZAQbi0tOU1hb3kwMTUtRkwtSkw5UGk5WjVKTDhiZA0Q1cllSOW15SDdoX05nQQZDZD"
    CODE_GENERATION_DATE = datetime(2023, 9, 18)


    def generateInitialLongLifeCode(self) -> any:
        response = requests.get(
        url = "https://graph.instagram.com/access_token?grant_type=ig_exchange_token&client_secret=5c34cc26e0e9aae35356b87d47b15b86&access_token=IGQWRObG85bE5acF95Yk1ZANXVVWWhYVzd1TkNhUF9BdS12LXBZAeFliZA2tUTUFkVWtlX3psUUtjQnA2R2diZAzVqTWJFZAGpEQ2UxN1I3SHRzeV9OOF9kaWlwRmYxbVlKcy04QTR6VllwTzlETFdxdXdBRmdTWTZAoNms4NzZAENEl3aGwxZAwZDZD"
    )
        return response.json
    
    def refreshLongLivedToken(self) -> any:
        response = requests.get(
            url = "https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=IGQWRQWG5CMDAwa1V5RGgwOVpRd3FTRHRZANHdGMy0tcC1CN1E4MWw3N216Tmd2cjYxXzY1bXFZAakhlakdrZA1ZAQbi0tOU1hb3kwMTUtRkwtSkw5UGk5WjVKTDhiZA0Q1cllSOW15SDdoX05nQQZDZD",
        )

        return response.json
    
    def getLongLivedToken(self) -> str:
        return InstagramTokenGenerator.LONG_LIFE_CODE
    
    def getDateLongLifeTokenGenerated(self) -> datetime:
        return InstagramTokenGenerator.CODE_GENERATION_DATE
    
    # //TODO: Handle refreshing the long lived token after 58 days
    # //TODO: Import and export of token plus generation date to file - shouldn't be hardcoded
    # //TODO: Current methods only return raw JSON. Data needs to be extracted properly