
import requests
import json
CLIENT_ID = '1000.F2C214BXMYDJWE2DJEW65UUZFY629Q'
CLIENT_SECRET = 'e284d583a16400a2978265722afad4e195ef28dbfc'
ReFreshToken = "1000.61f26005e0677dc36256ab0386c975fb.9169528e740d0072f87e117bb6d7f9d4"

def refresh_auth():

 url = "https://accounts.zoho.com/oauth/v2/token?refresh_token="+ReFreshToken+"&client_id="+CLIENT_ID+"&client_secret="+CLIENT_SECRET+"&grant_type=refresh_token"
 r = requests.post(url)
 data = json.loads(r.text)
 resu =r.content
 if 'access_token' in data:
    resu=  data['access_token']
  
    return resu
 
access_token = refresh_auth()
print(access_token)

oauth_token = "1000.61f26005e0677dc36256ab0386c975fb.9169528e740d0072f87e117bb6d7f9d4"
portal_id = "803380973"
department_id = "828679000000365029"

# api endpoint
URL = "https://desk.zoho.com/api/v1/tickets"

# response header
headers = {
        'Authorization': f'Zoho-oauthtoken {oauth_token}'
     }

# ticket data
data = {
        "subject": "test Data",
        "departmentId": department_id,
        "contactId": "828679000001676093",
        "description": "The customer is facing an issue with the product. Needs urgent attention.",
        "priority": "High",
        "status": "Open",
        "email": "customer@example.com",
        "phone": "1234567890",
        "dueDate": "2024-05-20T16:00:00Z"
}

# convert response to json
json_data = json.dumps(data)

# send POST request
response = requests.post(URL, headers=headers, data=json_data)

# Output
print(f'Status Code: {response.status_code}')
print(response.json())



