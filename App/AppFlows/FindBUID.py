import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
load_dotenv() 
DB_HOST = os.getenv('DB_HOST')
DB_NAME =os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

def get_bright_uid(PHONE_NUMBER):
    try :   
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()
        cur.execute("SELECT bright_user_id FROM bm_users_userprofile WHERE primary_phonenum = %s;",(PHONE_NUMBER,))
        bright_user_id = cur.fetchone()[0]
        if bright_user_id != None:            
            cur.execute("SELECT bright_uid FROM bm_users_brightuser WHERE id =%s;",(str(bright_user_id),))          
            bright_uid = cur.fetchone()[0]
            # print(type(bright_uid))
            return bright_uid
        else:
            return False       
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return False

# b_id=get_bright_uid('+11399315565')
# print(b_id)

def get_access_code(PHONE_NUMBER):
    try:
        conn=psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur=conn.cursor()
        cur.execute("SELECT bright_user_id FROM bm_users_userprofile WHERE primary_phonenum = %s;",(str(PHONE_NUMBER),))
        bright_user_id = cur.fetchone()[0]
        if bright_user_id != None:            
            cur.execute("SELECT id FROM bm_users_userstate WHERE user_id=%s;",(str(bright_user_id),))          
            state_id = cur.fetchone()[0]
            if state_id !=None:
                cur.execute("SELECT response FROM bm_users_userstateeventdata WHERE user_state_id=%s AND event_name='LOGIN_EVENT';",(str(state_id),))
                response=cur.fetchone()[0]
                return(response['action_data']['access'])
            else:
                return False
        else:
            return False
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return False

# r=get_access_code('+19211295590')
# print(type(r['action_data']['access']))



