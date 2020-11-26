from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

#URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22miami%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.40698408056639%2C%22east%22%3A-80.08769391943358%2C%22south%22%3A25.669669887897506%2C%22north%22%3A25.875577798211303%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22]}&requestId=2'

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22miami%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.52062391210936%2C%22east%22%3A-79.97405408789061%2C%22south%22%3A25.58020849837098%2C%22north%22%3A25.964816872741405%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22]}&requestId=5'

raw_data = 'zguid=23|%24febee9ba-a5ce-497d-8290-4a836f11a712; zgsession=1|95e5b9b4-2a0c-4942-95b0-753637eba0cc; zjs_user_id=null; _ga=GA1.2.1238956647.1606174713; _gid=GA1.2.390997415.1606174713; zjs_anonymous_id=%22febee9ba-a5ce-497d-8290-4a836f11a712%22; JSESSIONID=CA68D5549CF9761580E4CB71D3D7E36D; _gcl_au=1.1.918243037.1606174713; KruxPixel=true; DoubleClickSession=true; _pxvid=ffac4e95-2de4-11eb-bb8d-0242ac120018; _fbp=fb.1.1606174713491.664261961; _derived_epik=dj0yJnU9aWQwcFczV05iMWpUSGNqRTdXZmNEd1YtY0d2V1dkYXEmbj1sYnJyTEJFLWwzbTZQVDFCdzZCVFhnJm09MSZ0PUFBQUFBRi04Ul9rJnJtPTEmcnQ9QUFBQUFGLThSX2s; _pin_unauth=dWlkPVkyRmhNelZpWXpNdFkyVTJNaTAwTkRBMExUazNNV1F0TlRNNE1XVTRaR0ZsTURneg; g_state={"i_p":1606181915831,"i_l":1}; KruxAddition=true; G_ENABLED_IDPS=google; search=6|1608766886804%7Crect%3D25.875577798211303%252C-80.08769391943358%252C25.669669887897506%252C-80.40698408056639%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0912700%09%09%09%09%09%09; _px3=faaa4cfccde7e0078882220ea33c3fa46371dd318f06f20011bc1f1ded58f665:M4+N0GAmfRfOocWQb0wvl/KkLWf+dhlN+XYtP/rk+l65cDST5Od088esnDsezu9bNBLyRAPHN/LrvPtpypjzpA==:1000:25rEi1RqPRtECxQI479GtT+/QbCEClxoLQv8iHcFrKqSTzKRFNI6f4nHySc1Hx9INxVOVz4jhjmLG4E1ZS14nMYibd03w551wW42mhimDSyuSyK2n8WziyEtVozRYSXhgUgbal7CuT5stXnz5xRyQRDg584pddn0tQgrk0VW0aU=; AWSALB=lhheVgbwDc+kiM0irSdBgA36kDuPfpym/CTX/zWlwcyanEkfUZiES4acXfWyEaWopRXp0hRb4grs3a6kpGhgm+AXdWJwY/yfk5lw/u83J+fF9YPdPyvON9U/Wb/M; AWSALBCORS=lhheVgbwDc+kiM0irSdBgA36kDuPfpym/CTX/zWlwcyanEkfUZiES4acXfWyEaWopRXp0hRb4grs3a6kpGhgm+AXdWJwY/yfk5lw/u83J+fF9YPdPyvON9U/Wb/M; _uetsid=ffd964e02de411eba72a1323390b2ede; _uetvid=ffd983902de411eba06d5dfa1b54b008; _gat=1'


cookie = SimpleCookie() #takes raw cookie object and turns it to dict
cookie.load(raw_data)
cookies = {}
for key, morsel in cookie.items():
    cookies[key] = morsel.value

new_cookie = cookies

def parse_url(url, page_number):
    url_parsed = urlparse(url) #parses the url and access the specific value you want as a string
    query_string = parse_qs(url_parsed.query) # takes parsed url and converts it to a list
    search_query_state = json.loads(query_string.get('searchQueryState')[0]) #converts to dict
    search_query_state['pagination'] = {'currentPage': page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    encode_qs = urlencode(query_string, doseq=1)
    new_url = f'https://www.zillow.com/search/GetSearchPageState.htm?{encode_qs}'
    return new_url

