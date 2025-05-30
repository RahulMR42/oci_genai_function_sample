# Copyright (c) 2025 Oracle and/or its affiliates.
## All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl


import requests
import json

url = "<Deployment/Route URL> "

payload = json.dumps({
  "compartmentId": "ocid1.compartment.oc1..xxx",
  "servingMode": {
    "modelId": "meta.llama-3.3-70b-instruct",
    "servingType": "ON_DEMAND"
  },
  "chatRequest": {
    "messages": [
      {
        "role": "USER",
        "content": [
          {
            "type": "TEXT",
            "text": "A sample SQL code"
          }
        ]
      }
    ],
    "apiFormat": "GENERIC",
    "maxTokens": 600,
    "isStream": False,
    "numGenerations": 1,
    "frequencyPenalty": 0,
    "presencePenalty": 0,
    "temperature": 1,
    "topP": 1,
    "topK": 1
  }
})
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}


response = requests.request("POST", url, headers=headers, data=payload)

