import requests
import json
import datetime

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def getFairs(cabins, name):
    for cabin in cabins:
        if cabin["cabinName"] == name:
            return cabin
    return {}


months = [{"start": "05-01", "end": "05-31"},
          {"start": "06-01", "end": "06-30"},
          {"start": "07-01", "end": "07-31"},
          {"start": "08-01", "end": "08-31"},
          {"start": "09-01", "end": "09-30"},
          {"start": "10-01", "end": "10-31"},
          {"start": "11-01", "end": "11-30"},
          {"start": "12-01", "end": "12-31"},
        ]

def connect_mongo():
    uri = "mongodb://jens:test@localhost/norse"
    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client["norse"]

def is_token_timeout(payload):
    if 'errors' in jsn:
        token_errors = [error for error in jsn['errors'] if error['code'] == 'core:Token:Timeout']
        if len(token_errors) > 0:
            print("Token timeout")
            return True
    return False

def create_token():
    ''''''
    url = "https://services.flynorse.com/api/v1/token"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "cookie": "ARRAffinity=aa8e1fc94231a6616d9c9cf9d19a69c2456023250690611bf27c09279050ef5d; ARRAffinitySameSite=aa8e1fc94231a6616d9c9cf9d19a69c2456023250690611bf27c09279050ef5d; _ga_LELRJSCXE1=GS1.1.1716305177.1.1.1716305303.60.0.0; _ga_XXXXXXXXXX=GS1.1.1716305147.12.1.1716305303.0.0.126804701; _hjSessionUser_3855766=eyJpZCI6IjdjYjE3NTQwLWIzOWMtNTNlZC1hYTA2LTZkODlhYmVjMTlkOCIsImNyZWF0ZWQiOjE3MTYzMDUzMDQwNjUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3855766=eyJpZCI6ImQ3ZjU3MzcwLTg4OWMtNGI0ZS04NzYyLWRkY2NkMDg3ZTk0OCIsImMiOjE3MTYzMDUzMDQwNjYsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; FPID=FPID2.2.sa6z3ZtB%2FonPtDqVw%2Beicfh6MQZAccVU6h0LNh92lTo%3D.1716305177; FPLC=coQYWZVI5a5B45hobmS%2FRLx5alIzKdVyU1rJXYj21eHvNQCb0w8%2BIyMeU%2Bud4NT0bdBDAM6YD0EgyExMOC%2Fe0vVtrPxf3LFiQXSHdxTzE%2BoJBenixZnEYIT7VqZAdw%3D%3D; rl_anonymous_id=RS_ENC_v3_IjkwNzc2MDVjLWU5ZDItNDBjZC04NjNmLWMyMmJkYjM1N2Q4YyI%3D; rl_page_init_referrer=RS_ENC_v3_Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIg%3D%3D; rl_page_init_referring_domain=RS_ENC_v3_Ind3dy5nb29nbGUuY29tIg%3D%3D; rl_session=RS_ENC_v3_eyJpZCI6MTcxNjMwNTE3MTc5MywiZXhwaXJlc0F0IjoxNzE2MzA3MTA0MTc4LCJ0aW1lb3V0IjoxODAwMDAwLCJzZXNzaW9uU3RhcnQiOmZhbHNlLCJhdXRvVHJhY2siOnRydWV9; _wt.mode-2383362=WT3biDSRGyvbyE~; _wt.user-2383362=WT3-rTLRTPNE8SMSeTrW41IUhXOjBnmocQJIgPqcEsh8DOqs8B_Ui0qj0GoyHud0-PbJtuaImDWb3MGb5AylwE1wDivdV_srupxvUi5wmVrslg~",
        "Referer": "https://flynorse.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    body = {"PlatformType" : "Web"}
    token_rsp = requests.post(url, data = json.dumps(body), headers = headers)

    jsn = json.loads(token_rsp.content.decode("utf-8"))

    print(jsn)

    return jsn

def get_fairs(start, end, token, origin, destination):
    url = "https://services.flynorse.com/api/v1/availability/lowfare"
    
    token_str = token['data']['token']

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "cookie": "ARRAffinity=aa8e1fc94231a6616d9c9cf9d19a69c2456023250690611bf27c09279050ef5d; ARRAffinitySameSite=aa8e1fc94231a6616d9c9cf9d19a69c2456023250690611bf27c09279050ef5d; _hjSessionUser_3855766=eyJpZCI6IjdjYjE3NTQwLWIzOWMtNTNlZC1hYTA2LTZkODlhYmVjMTlkOCIsImNyZWF0ZWQiOjE3MTYzMDUzMDQwNjUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3855766=eyJpZCI6ImQ3ZjU3MzcwLTg4OWMtNGI0ZS04NzYyLWRkY2NkMDg3ZTk0OCIsImMiOjE3MTYzMDUzMDQwNjYsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; FPID=FPID2.2.sa6z3ZtB%2FonPtDqVw%2Beicfh6MQZAccVU6h0LNh92lTo%3D.1716305177; FPLC=coQYWZVI5a5B45hobmS%2FRLx5alIzKdVyU1rJXYj21eHvNQCb0w8%2BIyMeU%2Bud4NT0bdBDAM6YD0EgyExMOC%2Fe0vVtrPxf3LFiQXSHdxTzE%2BoJBenixZnEYIT7VqZAdw%3D%3D; rl_anonymous_id=RS_ENC_v3_IjkwNzc2MDVjLWU5ZDItNDBjZC04NjNmLWMyMmJkYjM1N2Q4YyI%3D; rl_page_init_referrer=RS_ENC_v3_Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIg%3D%3D; rl_page_init_referring_domain=RS_ENC_v3_Ind3dy5nb29nbGUuY29tIg%3D%3D; _wt.mode-2383362=WT3biDSRGyvbyE~; _wt.user-2383362=WT3-rTLRTPNE8SMSeTrW41IUhXOjBnmocQJIgPqcEsh8DOqs8B_Ui0qj0GoyHud0-PbJtuaImDWb3MGb5AylwE1wDivdV_srupxvUi5wmVrslg~;  _clck=1nndw61%7C2%7Cfly%7C0%7C1602; _clsk=1ubgeon%7C1716305307018%7C1%7C1%7Cw.clarity.ms%2Fcollect; _gcl_au=1.1.1186909415.1716305313; _ga=GA1.1.1234196441.1716305313; _scid=708a4ea3-0cf1-4024-b883-3bf672ee1eca; _scid_r=708a4ea3-0cf1-4024-b883-3bf672ee1eca; _ga_LELRJSCXE1=GS1.1.1716305313.1.0.1716305313.60.0.0; _uetsid=663045d0178611efbdae352520153a0c; _uetvid=267561e0182711eeae9a9ba488361b37; _rdt_uuid=1716305313451.1586f309-0f20-4777-ad92-ffba5a191bcc; _ga_XXXXXXXXXX=GS1.1.1716305147.12.1.1716305313.0.0.126804701; mf_8c9a42b5-3bf8-4b15-8edf-911b272553e4=||1716305313484||0||||0|0|94.92248; _tt_enable_cookie=1; _ttp=vgWpWQ7DdRJ0Rt7m_jyRQB8aIZ3; _fbp=fb.1.1716305313636.1436252198; rl_session=RS_ENC_v3_eyJpZCI6MTcxNjMwNTE3MTc5MywiZXhwaXJlc0F0IjoxNzE2MzA3NTg5Njc0LCJ0aW1lb3V0IjoxODAwMDAwLCJzZXNzaW9uU3RhcnQiOmZhbHNlLCJhdXRvVHJhY2siOnRydWV9;",
        "Referer": "https://flynorse.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    } 
    access_token = "X-Access-Token=" + token_str
    headers["cookie"] = headers["cookie"] + " " + access_token

    payload = {"childDobs":[],"infantDobs":[],"criteria":[{"origin":"OSL","destination":"BKK","beginDate":start,"endDate":end}],"passengers":[{"type":"ADT","count":1}],"currencyCode":"NOK","promotionCode":"","clearBooking":False}

    r = requests.post(url, data = json.dumps(payload), headers = headers)

    jsn = json.loads(r.content.decode("utf-8"))


    jsn["query_date"] = datetime.datetime.now(tz=datetime.timezone.utc)
    jsn["start"] = start
    jsn["end"] = end

    return jsn

def fetch(origin, destination, prices, token):
    query_time = datetime.datetime.now(tz=datetime.timezone.utc)
    update_operations = []
    for month in months:
        start = "2024-"+month["start"]
        end = "2024-"+month["end"]

        fairs = get_fairs(start, end, token, origin, destination)

        if fairs["errors"] != None:
            print(fairs["errors"])
            return

        jsn_doc = {}

        economy_fairs = fairs["data"][0]["cabins"]

        economy = getFairs(economy_fairs, "Economy")

        for fare in economy["lowFareAmounts"]:
            departure_date = fare["departureDate"]
            fare["timestamp"] = query_time

            jsn_doc["origin"] = origin
            jsn_doc["destination"] = destination
            jsn_doc["date"] = departure_date

            current = prices.find_one({"origin": origin, "destination" : destination, "date": departure_date})

            new_price = False

            if current != None:
                prices_size = str(len(current["prices"]) -1)
                if current["prices"][-1]["economy"]["fareTotal"] == fare["fareTotal"]:
                    print("Same price, just updating the current row")
                    prices.update_one({"origin" : origin, "destination" : destination, "date" : departure_date}, {"$set" : {"prices." + prices_size : {"collection_time": query_time, "economy" : fare}}}, upsert=True)
                else:
                    new_price = True
            else:
                new_price = True
            
            if new_price:
                print("New price addign entry")
                prices.update_one(
                        { "origin": origin, "destination" : destination, "date": departure_date},
                        {
                            "$push": {
                                "prices": {
                                    "collection_time": query_time,
                                    "economy" : fare,
                                }
                            }
                        },
                        upsert=True)

def main():
    db = connect_mongo()

    token = create_token()

    prices = db["prices"]

    fetch("BKK", "OSL", prices, token)
    fetch("OSL", "BKK", prices, token)

if __name__ == '__main__':
    main()
