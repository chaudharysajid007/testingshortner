async def get_shortlink(chat_id, link):
    settings = await get_settings(chat_id) #fetching settings for group
    if 'shortlink' in settings.keys():
        URL = settings['shortlink']
        API = settings['shortlink_api']
    else:
        URL = SHORTLINK_URL
        API = SHORTLINK_API
    if URL.startswith("shorturllink") or URL.startswith("terabox.in") or URL.startswith("urlshorten.in"):
        URL = SHORTLINK_URL
        API = SHORTLINK_API
    if URL == "api.shareus.io":
        # method 1:
        # https = link.split(":")[0] #splitting https or http from link
        # if "http" == https: #if https == "http":
        #     https = "https"
        #     link = link.replace("http", https) #replacing http to https
        # conn = http.client.HTTPSConnection("api.shareus.io")
        # payload = json.dumps({
        #   "api_key": "4c1YTBacB6PTuwogBiEIFvZN5TI3",
        #   "monetization": True,
        #   "destination": link,
        #   "ad_page": 3,
        #   "category": "Entertainment",
        #   "tags": ["trendinglinks"],
        #   "monetize_with_money": False,
        #   "price": 0,
        #   "currency": "INR",
        #   "purchase_note":""
        
        # })
        # headers = {
        #   'Keep-Alive': '',
        #   'Content-Type': 'application/json'
        # }
        # conn.request("POST", "/generate_link", payload, headers)
        # res = conn.getresponse()
        # data = res.read().decode("utf-8")
        # parsed_data = json.loads(data)
        # if parsed_data["status"] == "success":
        #   return parsed_data["link"]
    #method 2
        url = f'https://{URL}/easy_api'
        params = {
            "key": API,
            "link": link,
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                    data = await response.text()
                    return data
        except Exception as e:
            logger.error(e)
            return link
    else:
        shortzy = Shortzy(api_key=API, base_site=URL)
        link = await shortzy.convert(link)
        return link
