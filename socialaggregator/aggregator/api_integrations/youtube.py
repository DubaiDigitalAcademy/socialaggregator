import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class YouTubeSearch():

    DEVELOPER_KEY = 'AIzaSyCn3__0ruqiUKPpe078KcsQBLtdNoC2ma0'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    def __init__(self) -> None:
        self.youtube = build(YouTubeSearch.YOUTUBE_API_SERVICE_NAME, YouTubeSearch.YOUTUBE_API_VERSION, developerKey = YouTubeSearch.DEVELOPER_KEY)
        self.args = None
        self.response = []

    def buildArgsParser(self, searchTerm) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        parser.add_argument('--q', help='Search term', default=searchTerm)
        parser.add_argument('--max-results', help='Max results', default=25)
        return parser
    
    def generateArgs(self, searchTerm="Testing") -> bool:
        parser = self.buildArgsParser(searchTerm)
        try:
            self.args = parser.parse_args()
            return True
        except e:
            print("GENERATE ARGS ERROR")
            print(e.resp.status)
            print(e.content)
            return False
        
    def extractDataFromSearchResults(self, result, result_type) -> list:
        result_data = [ 
            result['snippet']['title'],
            result['snippet']['description'],
            result['snippet']['thumbnails']['high']['url'],
            result['snippet']['publishedAt'],
        ]

        if result_type == 'video':
            result_data.append( result['id']['videoId'] )
        elif result_type == 'channel':
            result_data.append( result['id']['channelId'])
        else:
            result_data.append( result['id']['playlistId'] )

        return result_data
    
    def assembleResults(self, results_obj) -> list:
        videos = []
        channels = []
        playlists = []

        for result in results_obj.get('items', []):
            if result['id']['kind'] == "youtube#video":
                result_data = self.extractDataFromSearchResults(result, 'video')
                videos.append(result_data)

            elif result['id']['kind'] == 'youtube#channel':
                result_data = self.extractDataFromSearchResults(result, 'channel')
                channels.append(result_data)

            elif result['id']['kind'] == 'youtube#playlist':
                result_data = self.extractDataFromSearchResults(result, 'playlist')
                playlists.append(result_data)

        extracted_search_results = [ videos, channels, playlists]

        return extracted_search_results

    def performSearch(self, searchTerm) -> any:
        self.generateArgs(searchTerm)

        try:
            search_response = self.youtube.search().list(
                q = self.args.q,
                part = 'id, snippet',
                maxResults = self.args.max_results
            ).execute()
            return search_response
        except HttpError as e:
            print("SEARCH HTTP ERROR")
            print('An HTTP error %d occured:\n%s' % (e.resp.status, e.content))

    def getOrganisedSearchResults(self, searchTerm) -> list:
        search_results = self.performSearch(searchTerm)
        organisedSearchResults = self.assembleResults(search_results)

        return organisedSearchResults


# USAGE EXAMPLE:

# searcherObject = YouTubeSearch()

# full_results = searcherObject.getOrganisedSearchResults("Tom Pemberton")

# videoList = full_results[0]
# channelList = full_results[1]
# playlistList = full_results[2]

# print("VIDEOS:\n")

# for video in videoList:
#     print('%s, %s (%s)\n' % (video[0], video[3], video[4]))
#     print('%s\n' % video[1])
#     print('%s\n\n' % video[2])

# print("CHANNELS:\n")

# for channel in channelList:
#     print('%s, %s (%s)\n' % (channel[0], channel[3], channel[4]))
#     print('%s\n' % channel[1])
#     print('%s\n\n' % channel[2])

# print("PLAYLISTS:\n")

# for playlist in playlistList:
#     print('%s, %s (%s)\n' % (playlist[0], playlist[3], playlist[4]))
#     print('%s\n' % playlist[1])
#     print('%s\n\n' % playlist[2])

# print("COMPLETE")