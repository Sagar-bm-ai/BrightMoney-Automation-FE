import requests
import json
from resources import headers,collection,extras
from FindBUID import get_access_code,get_bright_uid

def linkCheckingAccount(PHONE_NUMBER):
    # call signin first

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Length": ""
    }

    payload = collection['LOGIN_EVENT']['payload']    
    payload['data']['event_data']['phone_number'] =  PHONE_NUMBER
    # if(payload['data']['event_data']['survey'] ==None):
    #     payload['data']['event_data']['survey'] = extras['survey']   
    payload['data']['event_data']["presell_version"] = 'v1'
    login_response = requests.request("POST", collection['LOGIN_EVENT']['url'] , headers=headers, data=json.dumps(payload))
    assert login_response.status_code == 200 , 'Gateway is down, LOGIN_EVENT Failed'          
    login_result = login_response.json()   
    
    access_code = login_result['data']['action_data'].get('access')
    # bm_session_id = extras['bm_session_id']                  ## hard coded from extras
    # headers['Authorization'] = 'Bearer ' + access_code

    headers = {
        "Authorization":'Bearer ' + access_code,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Content-Length": ""
    }

    
    bright_uid = login_result['data']['action_data'].get('bright_uid')       #### from db login event
    

    payload={}
    payload["meta"]=extras["meta"]
    if(payload['meta']!=None):
        payload['meta']['bright_uid']=bright_uid
        # payload['meta']['bm_session_id']=bm_session_id

    payload['data'] = collection['ADD_ACCOUNT_EVENT']['data']
    add_account_response = requests.request("POST", collection['ADD_ACCOUNT_EVENT']['url'] , headers=headers, data=json.dumps(payload))
    assert add_account_response.status_code == 200 , 'Gateway is down, LOGIN_EVENT Failed'          
    add_account_result = add_account_response.json()
    print(f'ADD_ACCOUNT_EVENT:\n{add_account_result}')

    payload['data'] = collection['ALSM_SESSION_START_EVENT']['data']
    response = requests.request('POST',collection['ALSM_SESSION_START_EVENT']['url'],headers=headers,data=json.dumps(payload))
    assert response.status_code == 200 , 'Gateway is down, LOGIN_EVENT Failed'          
    ALSM_SESSION_START_EVENT_result = response.json()
    print(f'ALSM_SESSION_START_EVENT:\n{ALSM_SESSION_START_EVENT_result}')
    linking_session_id=ALSM_SESSION_START_EVENT_result['data'].get('linking_session_id')


    payload['data'] = collection['INITIATE_ACCOUNT_LINKING_EVENT']['data']
    payload['data']['event_data']['linking_session_pid']=linking_session_id
    response = requests.request('POST',collection['INITIATE_ACCOUNT_LINKING_EVENT']['url'],headers=headers,data=json.dumps(payload))
    print(response.request.body)
    # assert response.status_code == 200 , 'Gateway is down, LOGIN_EVENT Failed'          
    print(response.status_code)
    result = response.json()
    print(f'INITIATE_ACCOUNT_LINKING_EVENT:\n{result}')

    public_token_request={}
    public_token_request=collection['GET_PUBLIC_TOKEN_EVENT']['data']
    response = requests.request('POST',collection['GET_PUBLIC_TOKEN_EVENT']['url'],headers=headers,data=json.dumps(public_token_request))
    print(response.request.body)
    assert response.status_code == 200 , 'Gateway is down, LOGIN_EVENT Failed'          
    result = response.json()
    print(f'GET_PUBLIC_TOKEN_EVENT:\n{result}')
    public_token=result.get('public_token')

    payload['data']=collection['ALSM_LINKING_SUCCESS_EVENT']['data']
    payload['data']['linking_session_id'] =linking_session_id
    payload['data']['event_data']['response']['public_token'] =public_token
    response=requests.request('POST',collection['ALSM_LINKING_SUCCESS_EVENT']['url'],headers=headers,data=json.dumps(payload))
    linking_sucess_result=response.json()
    print(f'ALSM_LINKING_SUCCESS_EVENT:\n{linking_sucess_result}')
    
    payload['data']=collection['LINKING_SESSION_SUCCEEDED_EVENT']['data']
    payload['data']['event_data']['linking_session_pid']=linking_session_id
    response = requests.request('POST',collection['LINKING_SESSION_SUCCEEDED_EVENT']['url'],headers=headers,data=json.dumps(payload))
    assert response.status_code == 200 , 'Gateway is down, LOGIN_EVENT Failed'          
    result = response.json()
    print(f'LINKING_SESSION_SUCCEEDED_EVENT:\n{result}')



##linking_session_pid
##ACCOUNTS_CREATED_IN_UNIFIED_APP_EVENT in db not in automation
##ALSM_LINKING_SUCCESS_EVENT not in db





# linkCheckingAccount('+19211296625')


    