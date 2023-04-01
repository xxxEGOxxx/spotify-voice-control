import uuid

import spacy
# from spacy import displacy
import speech_recognition as sr
import pyaudio
import subprocess
# To access Spotipy
import spotipy
# To View the API response
import json
# To open our song in our default browser
import webbrowser
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

scope = "user-modify-playback-state"

username = 'EGO Grig\'s'
clientID = '9656ed2a998745268ce301bcad8d041c'
clientSecret = '122eaad126d045e98b9276321c2b8319'
redirectURI = 'https://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirectURI, scope=scope)
print(oauth_object)
token_dict = oauth_object.get_access_token()
print(token_dict)
token = token_dict['access_token']
print(token)
spotifyObject = spotipy.Spotify(auth=token)
print(spotifyObject)
user = spotifyObject.current_user()
# To print the response in readable format.
print(json.dumps(user, sort_keys=True, indent=4))

spotifyObject.next()


# open spotify
subprocess.call('"C:\\Users\\EGO\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"')

while True:
    print("Welcome to the project, " + user['display_name'])
    user_input = input('input : ')
    if user_input == "1":
        webbrowser.open("https://open.spotify.com/")
        print('Song has opened in your browser.')
    elif user_input == "2":
        spotifyObject.devices()
        

# # obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
#
# # recognize speech using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))
#
# nlp = spacy.load("en_core_web_trf")
#
# # You can type a lot of sentences at one time
#
# # TEST SENTENCES
# doc = nlp(
#     "Thank you, open the door. Can you break the door? I knock the door! Close the door, please. She said: \"Create the door!\" Ok, start our home project")
# # TEST SENTENCES
#
# check = 0
#
# for token in doc:
#     print(token.text + " " + token.pos_)
#
# for token in doc:
#     if token.lemma_ == token.text.lower():
#         check = 1
#         if token.pos_ == "VERB":
#             check = 1
#             if token.dep_ == "ROOT":
#                 check = 1
#                 for checkNsubj in token.sent:
#                     if checkNsubj.dep_ == "nsubj" or checkNsubj.dep_ == "xcomp":
#                         check = 0
#                         break
#             else:
#                 check = 0
#         else:
#             check = 0
#     else:
#         check = 0
#     if check == 1:
#         print(
#             str(token.sent) + "\n" + token.text + " " + token.pos_ + " " + token.dep_ + " " + token.head.text + " " + token.lemma_)
#         print("Yes, It's our target!\n")
#         print("Action: " + token.text, end=", ")
#         objectOfAction = []
#         root_token = token.sent.root
#         for child in root_token.children:
#             if child.dep_ == "dobj" or child.dep_ == "poss" or child.dep_ == "det" or child.dep_ == "compound":
#                 for nextChild in child.children:
#                     for nextNextChild in nextChild.children:
#                         objectOfAction.append(nextNextChild)
#                     objectOfAction.append(nextChild.text)
#                 objectOfAction.append(child.text)
#         print("Object: ", end="")
#         for i in objectOfAction:
#             print(i, end=" ")
#         print("\n")
#
# # displacy.serve(doc, style="dep")
