# Script that gets the code for specific languages

'''Importing requests'''
import requests

'''Taking the server url'''
url = "https://text-translator2.p.rapidapi.com/getLanguages"

'''Url headers i.e api-Key'''
header ={
	"X-RapidAPI-Key": "306a0c6eb7mshc0f4bbfa89c212bp197011jsnc5d51358fbb9",
	"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}

'''Get response from the server'''
response = requests.get(url=url, headers=header)

def recognise_lang():
    specific_lang = response.json()['data']['languages']
    search_lang = input("Enter language you would want the code to: ")
    for lang in specific_lang:
        if str(search_lang.capitalize()) in lang['name']:
            print(f"The code for {lang['name']} is {lang['code']}")
        # else:
        #     print("The language you have entered is not recognised! Try inputing well or try a different language")

recognise_lang()
