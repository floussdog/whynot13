import requests
import csv, sys 

CSV_FILE = 'participants.csv'    # File containing participant numbers


url = "https://sms-international.p.rapidapi.com/WebTool/SMStoCountry/sms1"

querystring = {"with open(CSV_FILE, 'r') as csvfile:
    peoplereader = csv.reader(csvfile)
    numbers = set([p[0] for p in peoplereader]) ","msg":"Hello, welcome to use sms service"}

headers = {
    'x-rapidapi-key': "87aa264292msh2e35dac4ce1ce22p11813ejsn51eefb26e5ba",
    'x-rapidapi-host': "sms-international.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
