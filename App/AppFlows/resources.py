headers = {
  "Authorization":"",
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Content-Length": ""
}
extras = {
  "meta": {
    "bm_request_id": "068f1313-87ff-436a-a9fa-477c754085b4",
    "app_version": "1.3.10-1-v629",
    "client_source": "android",
    "client_source_meta": "android",
    "bm_session_id": "4c6a421e-a00c-11ea-be57-0ace1771e734",
    "bright_uid": "ec43d221-c417-4bae-ab80-86f0b9e7366f"
  },
  "survey": {
      "type": "pre_sell", 
      "response": {
          "total_debt": {"max": 5000, "min": 0}, 
          "savings_fund": {"max": 1000, "min": 1000}, 
          "annual_income": {"max": 50000, "min": 35000}, 
          "financial_plan": "Never", 
          "home_importance": "Not important", 
          "target_net_worth": {"max": 500000, "min": 100000}, 
          "home_target_value": {"max": 500000, "min": 100000}
      }
  },

}
collection={  
  "LOGIN_EVENT": {
    "url": "http://gateway-dev.brightmoney.co/api/v1/users/usm/signin/",
    "payload": {
      "data": {
        "event_data": {
          "utm": {},
          "fb_data": {},
          "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkOGM3OTdlMDQ5YWFkZWViOWM5M2RiZGU3ZDAwMzJmNjk3NjYwYmQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYnJpZ2h0Y2FwaXRhbGFwcC1kZXYiLCJhdWQiOiJicmlnaHRjYXBpdGFsYXBwLWRldiIsImF1dGhfdGltZSI6MTYxNzg5NDE2NiwidXNlcl9pZCI6ImJIRWRRa0c5ZWhjWGxZRVZ6RkpKSEpZM0EwUDIiLCJzdWIiOiJiSEVkUWtHOWVoY1hsWUVWekZKSkhKWTNBMFAyIiwiaWF0IjoxNjE3ODk0MTY2LCJleHAiOjE2MTc4OTc3NjYsInBob25lX251bWJlciI6IisxMzQ3NjgyNzgzNCIsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsicGhvbmUiOlsiKzEzNDc2ODI3ODM0Il19LCJzaWduX2luX3Byb3ZpZGVyIjoicGhvbmUifX0.fpHsw1lgnbffbEiY6PN8d27N5wna7oFIeF-ExRExHajaCEGYgzdqy7rGtFLJ1m39SyPLFNfEtq0W5WFzPdu-Mzrs_WLzfq99jNS2NuMthOgznO0bnUSIh0AabfLcZHo9znT8ICdVF1qz8-JzKzWR_XiufvLqP_x3L8mpOC7pW2nxhg_j5mtgGZztgvFGdsRAWPRiKLE1GrxeZ1kH6xm6nWGnD4EtQFjQa5OBkHKT5EToEYhhzXTSXzXjv0uvWPQSROjE65X45qoW1T17gDt3hbFB2j99LmZDo6XwWZQmeZfjn3Fm2DCXiAQO2iazMRxy-wOSlIysz9ikGZMGhfvXPA",
          "fcm_token": "cF4kRoY_T-qnkzEtk5jOr6:APA91bFWZR4BamLoYEZhYeV_Wf31uGY3L9fAum5UAu1S_AGZabKrig0yGq7PhV97tT88UqCXmJghL3IZ591xKgIexRWMG5fVZ2tWpt6YlyXn1Og-X5UqDMUEk_FovR7LTMW0Yv7LPfJq",
          "phone_uid": "bHEdQkG9ehcXlYEVzFJJHJY3A0P2",
          "apns_token": None,
          "auth_signals": {},
          "phone_number": "",
          "funnel_variation": "4",
          "segment_anonymous_id": "6fd6654b-7f30-44a7-a41e-6b6dea73f422"
        },
        "event_name": "LOGIN_EVENT"
      },
      "meta": {
        "app_version": "1.3.10-1-v629",
        "bm_request_id": "2b1de781-9bc8-40a7-b629-265b6acedf1e",
        "bm_session_id": "0f54eeb0-3373-4e00-ab67-7828d6ea659f",
        "client_source": "android",
        "client_source_meta": "android"
      }
    }
  },
  "ADD_ACCOUNT_EVENT": {    
    "url": "http://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",
    "data": {
        "event_name": "ADD_ACCOUNT_EVENT",
        "event_data": {
          "linking_for": "CHECKING",
          "linking_flow": "ADD",
          "flow_type": "ONBOARDING"
        }      
    }
  },
  "ALSM_SESSION_START_EVENT": {
    "url": "http://gateway-dev.brightmoney.co/api/v1/fusion/alsm/session/start/",
    "data": {
        "linking_for": "CHECKING",
        "linking_flow": "ADD",
        "flow_type": "ONBOARDING"      
    }
  },
  "INITIATE_ACCOUNT_LINKING_EVENT": {
    "url": "http://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",
    "data": {
        "event_data": {
          "linking_session_pid": ""
        },
        "event_name": "INITIATE_ACCOUNT_LINKING_EVENT"      
    }
  },
  "GET_PUBLIC_TOKEN_EVENT": {
    "url": "https://sandbox.plaid.com/link/item/create",
    "data": {
      "credentials": {
          "username": "user_good",
          "password": "pass_good"
      },
      "initial_products": [
          "transactions"
      ],
      "institution_id": "ins_35",
      "display_language": "en",
      "options": {
          "webhook": "http://3cbe3d264b17.ngrok.io/api/v0/plaid/webhook/"
      },
      "public_key": "b566e5e558542013455f5cb2f1fc15"
    }
  },
  "ALSM_LINKING_SUCCESS_EVENT": {
    "url": "http://gateway-dev.brightmoney.co/api/v1/fusion/alsm/trigger/",   
    "data": {
        "linking_session_id": "",
        "event_name": "LINKING_SUCCESS_EVENT",
        "event_data": {
          "linking_client": "PLAID",
          "response": {
            "institution": {
              "institution_id": "ins_35",
              "name": "XYZ"
            },
            "public_token": ""
          }        
      }
    }
  },
  "LINKING_SESSION_SUCCEEDED_EVENT": {
    "url": "http://gateway-dev.brightmoney.co/api/v1/users/usm/trigger/",    
    "data": {
        "event_data": {
          "flow_type": "ONBOARDING",
          "linking_for": "CHECKING",
          "linking_flow": "ADD",
          "linking_session_pid": ""
        },
        "event_name": "LINKING_SESSION_SUCCEEDED_EVENT"      
    }
  },
}