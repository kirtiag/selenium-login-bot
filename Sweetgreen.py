import requests,json,csv
from bs4 import BeautifulSoup

Retailer = 'Sweetgreen'

url = "https://www.sweetgreen.com/locations"

payload = {}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'en-GB,en;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': 'OptanonAlertBoxClosed=2024-02-05T04:20:20.218Z; ab.storage.deviceId.768c4c20-e064-4ca5-b8cf-5616c9e7b783=%7B%22g%22%3A%22d69fadf1-0578-f647-ffbc-825898cb32c4%22%2C%22c%22%3A1707106898172%2C%22l%22%3A1707106898172%7D; mp_bdd660181917ff27581ff08ac4dd8d3c_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18d777fe9de1389-00760fd0192a24-26001851-100200-18d777fe9de1389%22%2C%22%24device_id%22%3A%20%2218d777fe9de1389-00760fd0192a24-26001851-100200-18d777fe9de1389%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22platform%22%3A%20%22web%22%7D; OptanonConsent=isIABGlobal=false&datestamp=Mon+Feb+05+2024+09%3A55%3A03+GMT%2B0530+(India+Standard+Time)&version=6.10.0&hosts=&consentId=216f9781-15cf-4c5a-85b1-ca2918c3d356&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0005%3A1%2CC0004%3A1%2CC0003%3A1&geolocation=US%3BWA&AwaitingReconsent=false',
  'Referer': 'https://www.sweetgreen.com/',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)

soup     = BeautifulSoup(response.text,'lxml')

all_loc = soup.find_all('div',{'class':'card__text'})
csv_data = {} 
for loc in all_loc[:]:
    urls = loc.find_all('a')
    for ul in urls:
        try:
            if "/" in ul['href'][-1]:
                storeid = ul['href'].split('/')[-2]
            else:
                storeid = ul['href'].split('/')[-1]
            
            print(storeid)
            
            url = "https://order.sweetgreen.com/graphql"
    
            payload = json.dumps({
            "query": "query Restaurant($id: ID!) {\n  restaurant(id: $id) {\n    ...RestaurantMenu\n    __typename\n  }\n}\n\nfragment RestaurantMenu on Restaurant {\n  id\n  slug\n  name\n  city\n  state\n  zipCode\n  address\n  phone\n  isOutpost\n  hours {\n    formatted\n    __typename\n  }\n  isAcceptingOrders\n  notAcceptingOrdersReason\n  deliveryFee\n  flexMessage\n  menu {\n    id\n    categories {\n      ...Category\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment Category on MenuCategory {\n  id\n  name\n  isCustom\n  products {\n    ...CategoryProduct\n    __typename\n  }\n  __typename\n}\n\nfragment CategoryProduct on Product {\n  asset {\n    url\n    __typename\n  }\n  calories\n  categoryId\n  cost\n  description\n  id\n  ingredients {\n    asset {\n      url\n      __typename\n    }\n    id\n    name\n    __typename\n  }\n  isModifiable\n  isCustom\n  customType\n  isSalad\n  label {\n    id\n    name\n    __typename\n  }\n  dietaryProperties {\n    id\n    name\n    __typename\n  }\n  name\n  outOfStock\n  restaurantId\n  slug\n  throttleItem\n  __typename\n}",
            "operationName": "Restaurant",
            "variables": {
                "id": storeid
            }
            })
            headers = {
            'accept': 'application/graphql-response+json, application/graphql+json, application/json, text/event-stream, multipart/mixed',
            'accept-language': 'en-US,en;q=0.9',
            'apollographql-client-name': 'sweetgreen',
            'apollographql-client-version': '6.348.1-d8817dd9',
            'content-type': 'application/json',
            'origin': 'https://order.sweetgreen.com',
            'priority': 'u=1, i',
            'referer': 'https://order.sweetgreen.com/hyde-park/menu',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'traceparent': '00-0000000000000000b544283b4f96239b-1e137b7dcb9258f5-01',
            'tracestate': 'dd=s:1;o:rum',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'x-csrf-token': 'n2ZKOgowO8lZKrytczkJV+jfL/lYVqaAPWZRgnROrRw=',
            'x-datadog-origin': 'rum',
            'x-datadog-parent-id': '2167211625911834869',
            'x-datadog-sampling-priority': '1',
            'x-datadog-trace-id': '13061609054484702107',
            'Cookie': '_gid=GA1.2.683052292.1752313385; _gcl_au=1.1.57392843.1752313385; _scid=RABtLd_VntRsZACUYRO7IGwVKazaFzOT; _fbp=fb.1.1752313385632.846761235952668002; _ScCbts=%5B%5D; _sctr=1%7C1752258600000; OptanonAlertBoxClosed=2025-07-12T09:43:08.351Z; _gat_UA-8921332-1=1; _gat_UA-8921332-9=1; _session_id=47e8925b3107e34645d761ccddf581c8; tfpsi=077fccb3-46d4-4a12-8162-38069c650ca0; __adroll_fpc=127de1cf19953b3d5b24a36b101dcd91-1752315249701; ndp_session_id=d25c63d3-de4e-4209-bfde-b4baa1a9f8dd; __stripe_mid=8a4372d5-7668-426e-98f6-5103d57fe3449546fd; __stripe_sid=7c74ffdc-7bee-4740-9d6c-718865d590749733f2; ab.storage.deviceId.768c4c20-e064-4ca5-b8cf-5616c9e7b783=g%3A171674db-821b-217b-8a87-ca3faa945f44%7Ce%3Aundefined%7Cc%3A1752315266248%7Cl%3A1752315266248; mp_bdd660181917ff27581ff08ac4dd8d3c_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A197fe20bfb1d4b-067c0582bb90f6-26011151-144000-197fe20bfb1d4b%22%2C%22%24device_id%22%3A%20%22197fe20bfb1d4b-067c0582bb90f6-26011151-144000-197fe20bfb1d4b%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.sweetgreen.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.sweetgreen.com%22%2C%22platform%22%3A%20%22web%22%7D; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jul+12+2025+15%3A44%3A41+GMT%2B0530+(India+Standard+Time)&version=6.10.0&hosts=&consentId=524c6ed4-78d7-4071-82e7-4ea644ace769&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0005%3A1%2CC0004%3A1%2CC0003%3A1&geolocation=IN%3BUP&AwaitingReconsent=false; _scid_r=UIBtLd_VntRsZACUYRO7IGwVKazaFzOTLAvIYg; _ga=GA1.1.418034226.1752313385; _ga_P05WD8BPE0=GS2.2.s1752315249$o1$g1$t1752315281$j28$l0$h0; _ga_8KEGP05HL9=GS2.1.s1752313385$o1$g1$t1752315281$j9$l0$h0; __ar_v4=GJ3QDOLBO5ESDOEWHOQDW6%3A20250711%3A2%7C3UGJTKNTKFHGFBO7NVZOT7%3A20250711%3A2%7CWXDD6ZQMFZBQFNG5ZSA56A%3A20250711%3A2; _dd_s=aid=fd45a85a-5113-4c73-89f2-0e3605cc4b27&rum=1&id=892247e8-e8c9-4af3-9075-98a1d738eaee&created=1752315248475&expire=1752316180639&logs=1'
            }
    
            response = requests.request("POST", url, headers=headers, data=payload)
            
            if '{"data":{"restaurant":null}}' in response.text:
                continue
            js = json.loads(response.text)['data']['restaurant']
            
            store_id = js['id']
            
            csv_data[store_id] = {
                "Retailer": Retailer,
                "StoreID": store_id,
                "Name": js['name'],
                "Address": js['address'],
                "City": js['city'],
                "State": js['state'],
                "Zipcode": js['zipCode'],
                "Phone": js.get('phone', '')
            }
        except Exception as e:
            print(f"Error in store: {ul['href']}")
            print(f" ---> {str(e)}")
            continue    
        finally:
            with open('sweetgreen_locations.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ["Retailer", "StoreID", "Name", "Address", "City", "State", "Zipcode", "Phone"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for store in csv_data.values():
                    writer.writerow(store)

            print(f"\n {len(csv_data)} unique locations saved to sweetgreen_locations.csv")