import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#def parse_weather():
req = requests.get('https://')

html = req.text
soup=BeautifulSoup(html, 'html.parser') #인자:html소스코드, 어떤parser이용인

header = req.headers
status = req.status_code #200: 정상
is_ok = req.ok #HTTP가 정상적으로 되었는지 (T/F)
