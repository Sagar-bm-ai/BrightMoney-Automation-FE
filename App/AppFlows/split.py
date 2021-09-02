import requests
import pickle
import json
import os

from dotenv import load_dotenv
load_dotenv() 

WORKSPACEID= os.getenv('WORKSPACEID')
ENVID = os.getenv('ENVID')
APITOKEN = os.getenv('APITOKEN')

headers = {
  'Authorization':'Bearer '+ str(APITOKEN),
  'Content-Type': 'application/json',
}


def get_split_details(split_name):
    split_data = {}
    try:
        url = "https://api.split.io/internal/api/v2/splits/ws/" + WORKSPACEID + "/" + str(split_name) + "/environments/" + ENVID          
        response = requests.get(url,headers=headers)   
        split_data = response.json()       
        assert response.status_code == 200    
    except :
        assert False , 'unable to update the split change , getting wrong url or payload or treatment_name'      
    return split_data

# get_split_details('flow_experiment')

def change_split(usm_ucb):
    file = open("LaunchAppSplit.txt", "wb")
  
    my_dict= {"usm_ucb_experiment": "on",
            "flow_experiment": "4",
            "target_card_in_funnel_experiment": "on",}

    
    # serializing dictionary 
    pickle.dump(my_dict, file)
    
    # closing the file
    file.close()
    
        
    # reading the data from the file
    with open('LaunchAppSplit.txt', 'rb') as handle:
        data = handle.read()
    
    print("Data type before reconstruction : ", type(data))
    # reconstructing the data as dictionary
    d = pickle.loads(data)
    
    print("Data type after reconstruction : ", type(d))
         

    
    for split_name in d:
        split=get_split_details(split_name) 
        if(split.get('name')=="usm_ucb_experiment"):
            if(split.get('defaultRule')!=[]):
                split.get('defaultRule').clear()
            print(split.get('defaultRule'))
            split.get('defaultRule').append({'treatment':usm_ucb,'size':100})
            print(split.get('defaultRule'))
        # elif(split.get('name')=="flow_experiment"):
            # if
        print(split)
        url = "https://api.split.io/internal/api/v2/splits/ws/" + WORKSPACEID + "/" + str(split_name) + "/environments/" + ENVID 
        payload =  [{'op': 'replace', 'path': '/defaultRule', 'value': [{'treatment': usm_ucb, 'size': 100}]}]       
        response = requests.patch(url,headers=headers,data=json.dumps(payload))   
        result = response.json()
        print(result)
        split_after=get_split_details(split_name)
        print(split_after.get('defaultRule'))
        break
    
# change_split("off")
def whitelist_user(split_name, bright_uid, treatment):            
    try:
        url = "https://api.split.io/internal/api/v2/splits/ws/" + WORKSPACEID + "/" + str(split_name) + "/environments/" + ENVID 
        data = get_split_details(split_name)          
        for tr in data.get('treatments'):            
            if tr.get('name') == treatment:
                if tr.get('keys') != None:
                    tr['keys'].append(bright_uid)                
                    break   
                else:
                    keys = [bright_uid]             
                    tr['keys'] = keys      
        payload = [{'op': 'replace', 'path': '/treatments', 'value': data.get('treatments')}]       
        response = requests.patch(url,headers=headers,data=json.dumps(payload))   
        result = response.json()
        assert_statement = f'getting {response.status_code}, unable to whitelist the user in {split_name} for {treatment} '   
        assert response.status_code == 200 , assert_statement        
    except :
        assert False , 'unable to update the split change , getting wrong url or payload or treatment_name'  

def delete_bright_uid_from_whitelist(split_name, bright_uid, treatment):     
    try:
        url = "https://api.split.io/internal/api/v2/splits/ws/" + WORKSPACEID + "/" + str(split_name) + "/environments/" + ENVID   
        data = get_split_details(split_name)         
        for tr in data.get('treatments'):
            if tr.get('name') == treatment:
                if tr.get('keys') != None:
                    for key in tr['keys']:
                        if key == bright_uid  :
                            tr['keys'].remove(key)              
                            break                       
        payload = [{'op': 'replace', 'path': '/treatments', 'value': data.get('treatments')}]       
        response = requests.patch(url,headers=headers,data=json.dumps(payload))   
        result = response.json()
        assert_statement = f'getting {response.status_code}, unable to update {split_name} for {treatment} '         
    except :
        assert False , 'unable to update the split change , getting wrong url or payload or treatment_name'        

