#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    res = "{
  \"id\": \"6ebc9621-0f96-4572-a923-d8477adb5bee\",
  \"timestamp\": \"2017-07-08T03:33:02.423Z\",
  \"lang\": \"en\",
  \"result\": {
    \"source\": \"agent\",
    \"resolvedQuery\": \"weather in sunnyvale\",
    \"action\": \"yahooWeatherForecast\",
    \"actionIncomplete\": false,
    \"parameters\": {
      \"geo-city\": \"Sunnyvale\"
    },
    \"contexts\": [],
    \"metadata\": {
      \"intentId\": \"3f980d91-c152-40f9-8ed7-d863fb84f4be\",
      \"webhookUsed\": \"true\",
      \"webhookForSlotFillingUsed\": \"false\",
      \"webhookResponseTime\": 278,
      \"intentName\": \"weather-intent\"
    },
    \"fulfillment\": {
      \"speech\": \"Today in Sunnyvale: Sunny, the temperature is 79 F\",
      \"source\": \"apiai-weather-webhook-sample\",
      \"displayText\": \"Today in Sunnyvale: Sunny, the temperature is 79 F\",
      \"messages\": [
        {
          \"type\": 0,
          \"speech\": \"Today in Sunnyvale: Sunny, the temperature is 79 F\"
        }
      ]
    },
    \"score\": 1
  },
  \"status\": {
    \"code\": 200,
    \"errorType\": \"success\"
  },
  \"sessionId\": \"7d0ac25a-bb87-4b05-a2ff-65df5424982a\"
}"
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
