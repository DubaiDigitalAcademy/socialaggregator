import requests

from instagram_token_generator import InstagramTokenGenerator

class InstagramSearch():
    TOKEN_GENERATOR = InstagramTokenGenerator()
    ACCESS_TOKEN = "IGQWRNSHYxSHNhTzlmTmx0cTRNMWdaazV2Skt4cUYxOEMtUEJibXE1MFdvVWlycngyVjU5ZAURsX1dsTjZADMGRTSzhQREpqcTZA2Mnl6X280ZAFpUTnpFdnU4NVV2b1oyQ05oRld2cjRyVjRGQQZDZD"
    EXISTING_HASHTAG_DICT = {}
    USER_ID = "10104352665136583"

    def retrieve_hashtag_id(self, term) -> str:
        if self.lookup_existing_hashtag_dict(term):
            return InstagramSearch.EXISTING_HASHTAG_DICT[term]
        else:
            new_key = self.get_hashtag_from_insta_api(term)
            self.add_term_to_hashtag_dict(term, new_key)
            return InstagramSearch.EXISTING_HASHTAG_DICT[term]

    def lookup_existing_hashtag_dict(self, term) -> bool:
        try:
            value = InstagramSearch.EXISTING_HASHTAG_DICT[term]
            return True
        except KeyError as e:
            return False

    def add_term_to_hashtag_dict(self, term, value) -> bool:
        InstagramSearch.EXISTING_HASHTAG_DICT.update({term : value})

    def get_hashtag_from_insta_api(self, term) -> str:
        # request = requests.get(
        #     url= ("https://graph.facebook.com/v18.0/ig_hashtag_search?user_id=%s&q=%s&access_token=%s" % ( InstagramSearch.USER_ID, term, InstagramSearch.ACCESS_TOKEN)),
        # )
        request = requests.get(
            url = "https://graph.facebook.com/v18.0/ig_hashtag_search",
            params = {
                "user_id" : InstagramSearch.USER_ID,
                "q" : term,
                "access_token" : InstagramSearch.ACCESS_TOKEN,
            }
        )
        print(request.url)
        print(request.reason)
        print(request.text)



igs = InstagramSearch()

igs.get_hashtag_from_insta_api("dubai")












# request = requests.get(
#     url = 'https://graph.facebook.com/',
#     data = {
#         "fields" : "id, name, top_media",
#         "access_token" : access_token
#     }
# )

# print(request.json)