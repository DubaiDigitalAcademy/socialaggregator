from io import BytesIO
from urllib.parse import urlencode

import certifi
import pycurl

file = open('curloutput.md', 'wb')

curlobj = pycurl.Curl()
curlobj.setopt(curlobj.URL, 'https://api.instagram.com/oauth/access_token')
post_data = {
    'client_id' : '312396031338333',
    'client_secret' : '5c34cc26e0e9aae35356b87d47b15b86',
    'grant_type' : 'authorization_code',
    'redirect_uri' : 'https://github.com/DubaiDigitalAcademy/socialaggregator',
    'code' : 'AQCn42QaAM8OGMUOcO0Tp-f-WxeP0H6JXFoRx8iRyxayHUGz0d1HlhlmVnazDtaNxDOXbVvm7D1uk6eaLBsTvAEllx_daclN7E-BfYkoyD4LDWlxT9IFI9NqjwHvv6uxTu52L4qoNPveCl_J5yIq5S-HOjoH5U73H06HhXkYVVT8VieYzR4yyIyecQrvpor-gDaK__WdHLVlZ-H91ZveJVeqwlYxBfUMUe88AY3R4j9K0A',
}
post_fields = urlencode(post_data)
curlobj.setopt(curlobj.POSTFIELDS, post_fields)
curlobj.setopt(curlobj.WRITEDATA, file)
curlobj.setopt(curlobj.CAINFO, certifi.where())
curlobj.perform()
curlobj.close()