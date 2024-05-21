import requests
import json
import datetime

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def getFairs(cabins, name):
    for cabin in cabins:
        print("\n\n\n")
        print(cabin)
        if cabin["cabinName"] == name:
            return cabin
    return {}

'''
Database:

Distance: OSL-BKK
    -> Price data


curl 'https://services.flynorse.com/api/v1/token' \
  -H 'authority: services.flynorse.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'cookie: _hjSessionUser_3855766=eyJpZCI6ImViMDczNDA5LWU5MmYtNWUzNy05NGZkLTkxMTc4NDcwMTFlYiIsImNyZWF0ZWQiOjE3MTQ3Mjc2MDY2MzMsImV4aXN0aW5nIjp0cnVlfQ==; _wt.user-2383362=WT3L2VoFN-bydulG8YzHfd3XufwNM_uiArSFuByO0JJC0LlkxuDwbCfMg22cKi11v3hwp68sYEEw7_9thuyTN7pdKjzPJAtzYeUQl7sNJsuhBk~; rl_anonymous_id=RS_ENC_v3_IjkxNjFlY2EyLTMzYjEtNDY0Ni1hYmNiLTMzYzZhYzNiNDQ2NyI%3D; rl_page_init_referrer=RS_ENC_v3_IiRkaXJlY3Qi; _gcl_au=1.1.1526897012.1714727614; _ga=GA1.1.1644183499.1714727614; _scid=0c935b58-e289-4619-9285-57a82e08e30b; _tt_enable_cookie=1; _ttp=9d3AtWnbQ4uZJePDsPb7blmx8IN; FPID=FPID2.2.AZahdnLfwxHt0%2B%2BNUaQTZ92ntxmnJaFWwx3WO%2FB0ZNI%3D.1714727614; _fbp=fb.1.1714727869764.1097292469; ARRAffinity=1126f8913d8e3f0ad6200b0ed68ff383e852f8c2c11952a490e484488dbfc120; ARRAffinitySameSite=1126f8913d8e3f0ad6200b0ed68ff383e852f8c2c11952a490e484488dbfc120; _wt.mode-2383362=WT3biDSRGyvbyE~; X-Access-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJVbmtub3duIiwianRpIjoiMzM3MGUzZDAtNmNjYS0zOTcwLTlhZmUtMjY3NTRmNzQwMDI4IiwiaXNzIjoiZG90UkVaIEFQSSJ9.asLfUJIAUeeCerlKICgyM3PDukdxNaQJQ9I9Ko_e1Xw; mf_8c9a42b5-3bf8-4b15-8edf-911b272553e4=||1715776203168||0||||0|0|85.44261; _clck=1wa6rrj%7C2%7Cflt%7C0%7C1584; FPLC=oqJ6aOTC1cm4X4BhQeSluV%2F8fHdcWQ9HpPk98cC9lwyycerDEeddL1NpQllvHrTYFq1naLj%2FB5X7uqHwCPRGmhBwMNmqOS5V9hwTYT5QLYYHOOU%2BNhVGtgAsD5UUfw%3D%3D; _uetsid=da23772012b611ef8b1b3f4e7df6e5ea; _uetvid=9a1c6980ea7611edb85acfd2f94be7f8; _scid_r=0c935b58-e289-4619-9285-57a82e08e30b; _rdt_uuid=1714727614097.8cb30550-0e79-4e55-9711-1209d3a4f847; _hjSession_3855766=eyJpZCI6IjVmMTA1YzAyLWY0YTQtNDI0OC04ZDlkLTcxNTQ3MDdmMDY3MyIsImMiOjE3MTU4NTUyODMyMzIsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _clsk=w3dgyg%7C1715856292834%7C2%7C1%7Cr.clarity.ms%2Fcollect; rl_session=RS_ENC_v3_eyJpZCI6MTcxNTg1NjMwMTY4OCwiZXhwaXJlc0F0IjoxNzE1ODU4MTI4MDI2LCJ0aW1lb3V0IjoxODAwMDAwLCJzZXNzaW9uU3RhcnQiOmZhbHNlLCJhdXRvVHJhY2siOnRydWV9; _ga_LELRJSCXE1=GS1.1.1715856328.6.0.1715856328.60.0.0; _ga_XXXXXXXXXX=GS1.1.1715856328.6.0.1715856328.0.0.70190530' \
  -H 'origin: https://flynorse.com' \
  -H 'pragma: no-cache' \
  -H 'referer: https://flynorse.com/' \
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Chromium";v="118"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36' \
  --compressed



curl 'https://services.flynorse.com/api/v1/availability/lowfare' \
  -H 'authority: services.flynorse.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: _hjSessionUser_3855766=eyJpZCI6ImViMDczNDA5LWU5MmYtNWUzNy05NGZkLTkxMTc4NDcwMTFlYiIsImNyZWF0ZWQiOjE3MTQ3Mjc2MDY2MzMsImV4aXN0aW5nIjp0cnVlfQ==; _wt.user-2383362=WT3L2VoFN-bydulG8YzHfd3XufwNM_uiArSFuByO0JJC0LlkxuDwbCfMg22cKi11v3hwp68sYEEw7_9thuyTN7pdKjzPJAtzYeUQl7sNJsuhBk~; rl_anonymous_id=RS_ENC_v3_IjkxNjFlY2EyLTMzYjEtNDY0Ni1hYmNiLTMzYzZhYzNiNDQ2NyI%3D; rl_page_init_referrer=RS_ENC_v3_IiRkaXJlY3Qi; _gcl_au=1.1.1526897012.1714727614; _ga=GA1.1.1644183499.1714727614; _scid=0c935b58-e289-4619-9285-57a82e08e30b; _tt_enable_cookie=1; _ttp=9d3AtWnbQ4uZJePDsPb7blmx8IN; FPID=FPID2.2.AZahdnLfwxHt0%2B%2BNUaQTZ92ntxmnJaFWwx3WO%2FB0ZNI%3D.1714727614; _fbp=fb.1.1714727869764.1097292469; ARRAffinity=1126f8913d8e3f0ad6200b0ed68ff383e852f8c2c11952a490e484488dbfc120; ARRAffinitySameSite=1126f8913d8e3f0ad6200b0ed68ff383e852f8c2c11952a490e484488dbfc120; _wt.mode-2383362=WT3biDSRGyvbyE~; X-Access-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJVbmtub3duIiwianRpIjoiMzM3MGUzZDAtNmNjYS0zOTcwLTlhZmUtMjY3NTRmNzQwMDI4IiwiaXNzIjoiZG90UkVaIEFQSSJ9.asLfUJIAUeeCerlKICgyM3PDukdxNaQJQ9I9Ko_e1Xw; mf_8c9a42b5-3bf8-4b15-8edf-911b272553e4=||1715776203168||0||||0|0|85.44261; _clck=1wa6rrj%7C2%7Cflt%7C0%7C1584; _hjSession_3855766=eyJpZCI6IjBlOTRjNjE5LWEzNTYtNGU5ZC1iMTk3LTdlYmRlYzkzZTAyMyIsImMiOjE3MTU4NDk3MDI0MDUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; FPLC=oqJ6aOTC1cm4X4BhQeSluV%2F8fHdcWQ9HpPk98cC9lwyycerDEeddL1NpQllvHrTYFq1naLj%2FB5X7uqHwCPRGmhBwMNmqOS5V9hwTYT5QLYYHOOU%2BNhVGtgAsD5UUfw%3D%3D; _clsk=1uvw6u6%7C1715849715099%7C2%7C1%7Cr.clarity.ms%2Fcollect; _uetsid=da23772012b611ef8b1b3f4e7df6e5ea; _uetvid=9a1c6980ea7611edb85acfd2f94be7f8; _ga_XXXXXXXXXX=GS1.1.1715849713.5.1.1715849717.0.0.2119742147; _ga_LELRJSCXE1=GS1.1.1715849713.5.1.1715849717.56.0.0; _scid_r=0c935b58-e289-4619-9285-57a82e08e30b; _rdt_uuid=1714727614097.8cb30550-0e79-4e55-9711-1209d3a4f847; rl_session=RS_ENC_v3_eyJpZCI6MTcxNTg0OTcwNDAyNSwiZXhwaXJlc0F0IjoxNzE1ODUxNTI0MDEyLCJ0aW1lb3V0IjoxODAwMDAwLCJzZXNzaW9uU3RhcnQiOmZhbHNlLCJhdXRvVHJhY2siOnRydWV9' \
  -H 'origin: https://flynorse.com' \
  -H 'referer: https://flynorse.com/' \
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Chromium";v="118"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36' \
  --data-raw '{"criteria":[{"origin":"OSL","destination":"BKK","beginDate":"2024-07-01","endDate":"2024-07-31"}],"passengers":[{"type":"ADT","count":1}],"currencyCode":"NOK","promotionCode":"","clearBooking":false,"childDobs":[],"infantDobs":[]}' \
--compressed


curl 'https://services.flynorse.com/api/v1/availability/lowfare' \
  -H 'authority: services.flynorse.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: _hjSessionUser_3855766=eyJpZCI6ImViMDczNDA5LWU5MmYtNWUzNy05NGZkLTkxMTc4NDcwMTFlYiIsImNyZWF0ZWQiOjE3MTQ3Mjc2MDY2MzMsImV4aXN0aW5nIjp0cnVlfQ==; _wt.user-2383362=WT3L2VoFN-bydulG8YzHfd3XufwNM_uiArSFuByO0JJC0LlkxuDwbCfMg22cKi11v3hwp68sYEEw7_9thuyTN7pdKjzPJAtzYeUQl7sNJsuhBk~; rl_anonymous_id=RS_ENC_v3_IjkxNjFlY2EyLTMzYjEtNDY0Ni1hYmNiLTMzYzZhYzNiNDQ2NyI%3D; rl_page_init_referrer=RS_ENC_v3_IiRkaXJlY3Qi; _gcl_au=1.1.1526897012.1714727614; _ga=GA1.1.1644183499.1714727614; _scid=0c935b58-e289-4619-9285-57a82e08e30b; _tt_enable_cookie=1; _ttp=9d3AtWnbQ4uZJePDsPb7blmx8IN; FPID=FPID2.2.AZahdnLfwxHt0%2B%2BNUaQTZ92ntxmnJaFWwx3WO%2FB0ZNI%3D.1714727614; _fbp=fb.1.1714727869764.1097292469; _clck=1wa6rrj%7C2%7Cflt%7C0%7C1584; FPLC=oqJ6aOTC1cm4X4BhQeSluV%2F8fHdcWQ9HpPk98cC9lwyycerDEeddL1NpQllvHrTYFq1naLj%2FB5X7uqHwCPRGmhBwMNmqOS5V9hwTYT5QLYYHOOU%2BNhVGtgAsD5UUfw%3D%3D; ARRAffinity=1126f8913d8e3f0ad6200b0ed68ff383e852f8c2c11952a490e484488dbfc120; ARRAffinitySameSite=1126f8913d8e3f0ad6200b0ed68ff383e852f8c2c11952a490e484488dbfc120; _wt.mode-2383362=WT3biDSRGyvbyE~; X-Access-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJVbmtub3duIiwianRpIjoiZDlhMjlkYWUtZjRkZC05OTRkLWVjN2UtZGUzZWY0YjEzNjcxIiwiaXNzIjoiZG90UkVaIEFQSSJ9.5rs_skE5qMiLosDPs96d8P6QzhabV0FemM0_a8uImNM; _rdt_uuid=1714727614097.8cb30550-0e79-4e55-9711-1209d3a4f847; mf_8c9a42b5-3bf8-4b15-8edf-911b272553e4=||1715863098069||0||||0|0|98.89565; _scid_r=0c935b58-e289-4619-9285-57a82e08e30b; _ga_XXXXXXXXXX=GS1.1.1715863097.7.1.1715863105.0.0.331557997; _ga_LELRJSCXE1=GS1.1.1715863098.7.1.1715863105.53.0.0; _uetsid=da23772012b611ef8b1b3f4e7df6e5ea; _uetvid=9a1c6980ea7611edb85acfd2f94be7f8; _hjSession_3855766=eyJpZCI6IjI4ZWE5NGI1LTRhMDgtNGM0Ny04YTgyLTFjZGIyN2QzNWVmYSIsImMiOjE3MTU4NjMwOTcxMDcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _clsk=1d19ls3%7C1715863105910%7C2%7C1%7Ca.clarity.ms%2Fcollect; rl_session=RS_ENC_v3_eyJpZCI6MTcxNTg2MzA5NzI4MCwiZXhwaXJlc0F0IjoxNzE1ODY0OTE3NTg5LCJ0aW1lb3V0IjoxODAwMDAwLCJzZXNzaW9uU3RhcnQiOmZhbHNlLCJhdXRvVHJhY2siOnRydWV9' \
  -H 'origin: https://flynorse.com' \
  -H 'referer: https://flynorse.com/' \
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Chromium";v="118"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36' \
  --data-raw '{"criteria":[{"origin":"OSL","destination":"BKK","beginDate":"2024-07-01","endDate":"2024-07-31"}],"passengers":[{"type":"ADT","count":1}],"currencyCode":"NOK","promotionCode":"","clearBooking":false,"childDobs":[],"infantDobs":[]}' \
  --compressed



jensharaldsete

YkgooBjaCsfyOjfa



'''

url = 'https://services.flynorse.com/api/v1/availability/lowfare'

headers = {        'authority': 'services.flynorse.com',
                   'accept': 'application/json, text/plain, */*',
                   'accept-language': 'en-US,en;q=0.9',
                   'content-type': 'application/json',
                   'cookie': '_hjSessionUser_3855766=eyJpZCI6ImViMDczNDA5LWU5MmYtNWUzNy05NGZkLTkxMTc4NDcwMTFlYiIsImNyZWF0ZWQiOjE3MTQ3Mjc2MDY2MzMsImV4aXN0aW5nIjp0cnVlfQ==; _wt.user-2383362=WT3L2VoFN-bydulG8YzHfd3XufwNM_uiArSFuByO0JJC0LlkxuDwbCfMg22cKi11v3hwp68sYEEw7_9thuyTN7pdKjzPJAtzYeUQl7sNJsuhBk~; rl_anonymous_id=RS_ENC_v3_IjkxNjFlY2EyLTMzYjEtNDY0Ni1hYmNiLTMzYzZhYzNiNDQ2NyI%3D; rl_page_init_referrer=RS_ENC_v3_IiRkaXJlY3Qi; _gcl_au=1.1.1526897012.1714727614; _ga=GA1.1.1644183499.1714727614; _scid=0c935b58-e289-4619-9285-57a82e08e30b; _tt_enable_cookie=1; _ttp=9d3AtWnbQ4uZJePDsPb7blmx8IN; FPID=FPID2.2.AZahdnLfwxHt0%2B%2BNUaQTZ92ntxmnJaFWwx3WO%2FB0ZNI%3D.1714727614; _fbp=fb.1.1714727869764.1097292469; _clck=1wa6rrj%7C2%7Cflt%7C0%7C1584; FPLC=oqJ6aOTC1cm4X4BhQeSluV%2F8fHdcWQ9HpPk98cC9lwyycerDEeddL1NpQllvHrTYFq1naLj%2FB5X7uqHwCPRGmhBwMNmqOS5V9hwTYT5QLYYHOOU%2BNhVGtgAsD5UUfw%3D%3D; ARRAffinity=1126f8913d8e3f0ad6200b0ed68ff383e852f8c2c11952a490e484488dbfc120; ARRAffinitySameSite=1126f8913d8e3f0ad6200b0ed68ff383e852f8c2c11952a490e484488dbfc120; _wt.mode-2383362=WT3biDSRGyvbyE~; X-Access-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJVbmtub3duIiwianRpIjoiZDlhMjlkYWUtZjRkZC05OTRkLWVjN2UtZGUzZWY0YjEzNjcxIiwiaXNzIjoiZG90UkVaIEFQSSJ9.5rs_skE5qMiLosDPs96d8P6QzhabV0FemM0_a8uImNM; _rdt_uuid=1714727614097.8cb30550-0e79-4e55-9711-1209d3a4f847; mf_8c9a42b5-3bf8-4b15-8edf-911b272553e4=||1715863098069||0||||0|0|98.89565; _scid_r=0c935b58-e289-4619-9285-57a82e08e30b; _ga_XXXXXXXXXX=GS1.1.1715863097.7.1.1715863105.0.0.331557997; _ga_LELRJSCXE1=GS1.1.1715863098.7.1.1715863105.53.0.0; _uetsid=da23772012b611ef8b1b3f4e7df6e5ea; _uetvid=9a1c6980ea7611edb85acfd2f94be7f8; _hjSession_3855766=eyJpZCI6IjI4ZWE5NGI1LTRhMDgtNGM0Ny04YTgyLTFjZGIyN2QzNWVmYSIsImMiOjE3MTU4NjMwOTcxMDcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _clsk=1d19ls3%7C1715863105910%7C2%7C1%7Ca.clarity.ms%2Fcollect; rl_session=RS_ENC_v3_eyJpZCI6MTcxNTg2MzA5NzI4MCwiZXhwaXJlc0F0IjoxNzE1ODY0OTE3NTg5LCJ0aW1lb3V0IjoxODAwMDAwLCJzZXNzaW9uU3RhcnQiOmZhbHNlLCJhdXRvVHJhY2siOnRydWV9',
                   'origin': 'https://flynorse.com',
                   'referer': 'https://flynorse.com/',
                   'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                   'sec-ch-ua-mobile': '?0',
                   'sec-ch-ua-platform': '"Linux"',
                   'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-site',
                   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

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

    col = client["norse"]["norsedata"]
    return col

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

def main():
    col = connect_mongo()

    token = create_token()

    origin = "OSL"
    destination = "BKK"

    db_coll = origin + destination

    db_fair = col[db_coll]

    query_time = datetime.datetime.now(tz=datetime.timezone.utc)
    for month in months:
        start = "2024-"+month["start"]
        end = "2024-"+month["end"]

        fairs = get_fairs(start, end, token, origin, destination)

        if fairs["errors"] != None:
            print(fairs["errors"])
            return


        economy_fairs = fairs["data"][0]["cabins"]

        economy = getFairs(economy_fairs, "Economy")
        #premium = getFairs(fairs["data"][0], "Premium")

        db_economy = db_fair["economy"]
        for fare in economy["lowFareAmounts"]:
            departure_date = fare["departureDate"]
            db_departure_date = db_economy[departure_date]

            fare["timestamp"] = query_time
            db_departure_date.insert_one(fare)
        



if __name__ == '__main__':
    main()
