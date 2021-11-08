import requests
import json
import pyttsx3
import re

API_KEY = "tTkTfiDNHy3S"
project_Token = "tWd7Z1Pmk3mG"
run_Key = "tsGuTvdGOdkG"




class Data:

    def __init__(self,api_key,project_Token):
        self.api_key = api_key
        self.project_Token = project_Token
        self.params = {
            "api_key" : API_KEY  #this is the authentication to pass a request
        }

        self.get_data()# used to make sure we get the resent data from the get data function 

    def get_data(self):#call the request and set the data attribute for the object
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{project_Token}/last_ready_run/data',params={"api_key" : API_KEY})# for the authentication to get the data
        self.data = json.loads(response.text)


    def get_total_Cases(self):#method to get the total cases 
        data = self.data['Total']

        for content in data: #loop through the data in total until we get the name Coronavirus Cases and return the value of the dict 
            if content['name'] == "Coronavirus Cases:":
                return content['value']
    

    def get_total_Deaths(self):#method to get the total deaths
        data = self.data['Total']

        for content in data: #loop through the data in total until we get the name Deaths and return the value of the dict 
            if content['name'] == "Deaths:":
                return content['value']
    


    def get_total_Recovered(self): #method to get the total recoveries
        data = self.data['Total']

        for content in data: #loop through the data in total until we get the name Recovered and return the value of the dict 
            if content['name'] == "Recovered:":
                return content['value']
    
        return "0"

    def get_Country_Data(self,Country): #method to get the counties data
        data = self.data["Country"]

        for content in data:
            if content['name'].lower() == Country.lower():
                return content
        
        return "0"

data = Data(API_KEY,project_Token)
#print(data.get_Country_Data("Senegal")['total_Deaths'])




#voice recognition setup
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()




print('press 1 Get total cases')
print('press 2 Get total deaths')
print('press 3 Get total recoveries')
choice = input('enter input: ')


if choice == 1:
    print('press 1 to get total cases worldwide')
    print('press 2 to get total cases for country')
    tot = print('enter choice: ')
    if tot == 1:
        speak(data.get_total_Cases())
    elif tot == 2:
            country1 = input('Enter country: ')
            speak(data.get_Country_Data(country1)['total_Cases'])
elif choice == 2:
    print('press 1 to get total deaths worldwide')
    print('press 2 to get total deaths for country')
    tot = print('enter coice: ')
    if tot == 1:
        speak(data.get_total_Deaths())
    elif tot == 2:
        country1 = input('Enter country: ')
        speak(data.get_Country_Data(country1)['total_Deaths'])
            
elif choice == 3:

    print('press 1 to get total Recoveries worldwide')
    print('press 2 to get total Recoveries for country')
    tot = print('enter coice: ')
    if tot == 1:
        speak(data.get_total_Recovered())
    elif tot == 2:
        country1 = input('Enter country: ')
        speak(data.get_Country_Data(country1)['total_Recovered'])
        




#print(get_audio())




