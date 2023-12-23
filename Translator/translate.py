# Writting a simple script that translates languages.
'''Importing requests to get the api'''
import requests

'''Url from we which we are requesting'''
url = 'https://text-translator2.p.rapidapi.com/translate'

'''Taking user input'''
src_lang = input("Enter your source language code: ")
trgt_lang =  input("Enter your target language code: ")
txt =  input("Enter the text you would like to translate: ")
'''Message to translate in form of a dict'''
payload = {
    'source_language': src_lang,
    'target_language': trgt_lang,
    'text': txt
}

'''The request header go hear'''
header = {
    'content-type': 'application/x-www-form-urlencoded',
    'X-RapidAPI-Key': '306a0c6eb7mshc0f4bbfa89c212bp197011jsnc5d51358fbb9',
    'X-RapidAPI-Host': 'text-translator2.p.rapidapi.com'
  }

'''Getting a response from the server'''
response = requests.post(url=url, headers=header, data=payload)

'''Printing out the available languages and their codes'''
print()
print(response.json()['data']['translatedText'])