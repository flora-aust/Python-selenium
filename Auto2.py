import requests
import json
import base64

# Replace these values with your Siebel environment details
siebel_url = "https://10.64.125.34:8002/siebel/app/admin/enu?SWECmd=Start"
username = "Cheetah20"
password = "CHEETAH2020!4"

# Load data from a JSON file
with open('SUPERVISOR_NO_FLAG.json', 'r') as file:
    data_list = json.load(file)

# Iterate through each dictionary in the list
for data in data_list:
    # Prepare headers for authentication
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}'
    }

    # Assuming your Siebel web service expects data in a specific format
    payload = {
        'EMPLOYEE': data['EMPLOYEE'],
        'PROVIDER': data['PROVIDER'],
        # Add other fields as needed
    }

    try:
        # Make a POST request to the Siebel web service endpoint
        response = requests.post(siebel_url, json=payload, headers=headers, verify=False)

        # Check the response status for each entry
        if response.status_code == 200:
            print(f"Data for {data['EMPLOYEE']} successfully sent to Siebel.")
        else:
            print(f"Failed to send data for {data['EMPLOYEE']}. Status code: {response.status_code}, Error: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
