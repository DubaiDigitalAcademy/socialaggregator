import requests

from instagram_token_generator import InstagramBasicTokenGenerator

class InstagramSearch():
    TOKEN_GENERATOR = InstagramBasicTokenGenerator()
    EXISTING_HASHTAG_DICT = {}

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
                "user_id" : InstagramSearch.TOKEN_GENERATOR.USER_ID_NUM,
                "q" : term,
                "access_token" : "EABhUnLscUK8BOwz56zTJw157bKp6KL8ZAVNByDNsNsE4WbJQ29coKT3LhRNjKLj2CExbLBUGJ5iSxqersZAfP20RpAzC3NPNP6mWZAKQMrXqX7h8UYyhwKl3J4sVen0ObC6V5fE7pki3cxypGJ1mfb4lQ04G7bACp9xj7bDx8otKEvQLB33k47B6b3CZAWXXRefAoWrZCHUkTPYUZD",
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