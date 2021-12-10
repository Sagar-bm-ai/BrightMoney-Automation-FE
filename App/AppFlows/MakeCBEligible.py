import requests
import json
from resources import headers,body
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AppFlows.FindBUID import get_bright_uid

def makeUserCBEligible(url,data,headers):

    URL  = url
    payload = json.dumps(data)
    header = headers
    response = requests.request("POST",URL,headers=header,data=payload)
    assert response.status_code == 200 , "API failed to execute"

    result = response.json()
    if(result["is_eligible"]==True & result["mle_split"]==True):
        return True
    else:
        return response.text



phone_num="+11399315571"
buid = get_bright_uid(phone_num)
url = body["MAKE_CB_ELIGIBLE"]["url"]

payload = body["MAKE_CB_ELIGIBLE"]["data"]
payload["bright_uid"]=buid

header = {
   'Content-Type': 'application/json'
 }

d= makeUserCBEligible(url,payload,headers)
print(d)
