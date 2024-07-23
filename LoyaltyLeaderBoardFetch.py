import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your app's credentials
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8000/callback'

# Step 1: Authorization
auth_url = 'https://streamlabs.com/api/v2.0/authorize?'
auth_params = {
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'response_type': 'code',
    'scope': 'points.read'  # Adjust scope as needed
}
auth_url += urlencode(auth_params)

print(f"Please visit this URL to authorize the application: {auth_url}")
print("After authorizing, you'll be redirected to a URL. Copy the 'code' parameter from that URL.")

# Step 2: Exchange authorization code for access token
code = input("Enter the code from the redirect URL: ")
token_url = 'https://streamlabs.com/api/v2.0/token'
token_data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'code': code,
    'grant_type': 'authorization_code',
    'redirect_uri': REDIRECT_URI
}

response = requests.post(token_url, data=token_data)
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info['access_token']
    print(f"Access Token obtained successfully!")
else:
    print(f"Failed to obtain access token. Status code: {response.status_code}")
    print(f"Response: {response.text}")
    exit()

# Step 3: Use the access token to fetch loyalty points data
api_url = "https://streamlabs.com/api/v2.0/points"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json"
}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Loyalty Points Data:")
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(f"Response: {response.text}")