import cot_reports as cot
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
import datetime;

def getData():
    url = 'https://c.fxssi.com/api/current-ratios?filter=AUDJPY&rand=0.5203286106651004&user_id=0'

    # Make a request to the URL
    response = requests.get(url)
    data = response.json()

    return data

data = getData()

timestamp =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
d = {}

for i in data["pairs"].keys():
    d[i] = {}
    d[i]["timestamp"] = timestamp
    d[i]["long"] = float(data["pairs"][i]["average"])
    d[i]["short"] = 100 - float(data["pairs"][i]["average"])

print(d)

with open("retail_data.json","r") as p1:
    data = json.load(p1)
   
data.append(d)

with open("retail_data.json","w") as p:
    json.dump(data,p,indent=4)
