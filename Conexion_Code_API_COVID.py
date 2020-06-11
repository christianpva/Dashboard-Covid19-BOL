import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import requests
def getStats(country):
  api_url = 'https://api.smartable.ai/coronavirus/stats/'+country
  api_params = {
    'Cache-Control': 'no-cache',
    'Subscription-Key': 'XXXXXXXX',
  }
  r = requests.get(url=api_url, params=api_params) 
  return r.text

data = getStats("BO")
import json
jsonData = json.loads(data)
jsonData['stats']['breakdowns']
latestData = jsonData['stats']['breakdowns'][0]
latestData['newDeaths']
history = pd.DataFrame(jsonData['stats']['history'])
history['date']=pd.to_datetime(history['date'])
history['updatetime'] = jsonData['updatedDateTime']
