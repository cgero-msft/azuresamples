##One shot cell

import requests
import base64

# Replace with your endpoint from Foundry Serverless
url = "https://<<YOUR ENDPOINT>>.<<REGION>>.models.ai.azure.com/v1/ocr"

# Define the file URL
# Replace with your file URL
file_url = "https://arxiv.org/pdf/2201.04234"  

# Download the file from the URL
file_response = requests.get(file_url)
if file_response.status_code == 200:
    # Encode the file content in Base64
    base64_content = base64.b64encode(file_response.content).decode("utf-8")
else:
    print(f"Failed to download file. Status Code: {file_response.status_code}")
    exit()

# Prepare the request payload
payload = {
    "model": "mistral-ocr-2503",
    "document": {
        "document_url": f"data:application/pdf;base64,{base64_content}",
        "type": "document_url"  # Keep this as document_url
    },
    "include_image_base64": True
}

# Set the headers
# Replace with your token
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <<YOUR TOKEN>>"
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print(#"Success:", response.json()#
        ("Raw Response:", response.text))
elif response.status_code == 422:
    print("Validation Error:", response.json())
else:
    print("Error:", response.status_code, response.text)
