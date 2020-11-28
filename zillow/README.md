# scrapers

Zillow scraper template that can be used to scrape listings from zillow.com
Currently set to Miami 
You can change location by changing the URL and raw_data in the utils.py files

Instructions

1. Go to Zillow.com and enter the city your looking for houses in
2. Click search
3. Right click and go down to inspect
4. Go to Network, General, copy the Request URL

 <a href="https://gyazo.com/734372791e1dfaebfc609ac36398f539"><img src="https://i.gyazo.com/734372791e1dfaebfc609ac36398f539.png" alt="Image from Gyazo" width="559"/></a>
 
 5. Go to Request Headers, and copy the cookie
 
 <a href="https://gyazo.com/69ecab3e34eed8a1ccf9610f14ace75b"><img src="https://i.gyazo.com/69ecab3e34eed8a1ccf9610f14ace75b.png" alt="Image from Gyazo" width="565"/></a>
 
6. Paste the above url in the 'URL variable in the utils.py as a string
 
7. Paste the cookie above in the 'raw_data' variable as a sring
