from rest_framework import generics
from django.http import JsonResponse
from fuzzywuzzy import fuzz
import requests
import re
# Create your views here.

class testview(generics.GenericAPIView):

    def get(self,request):
        return
    
    def post(self,request):
        print(request.data['prompt'])
        best_response = resgen(request.data['prompt'].lower(), response_dict)
        response = JsonResponse(
            {'response': best_response},status=200)
        return response

def resgen(input_text, response_dict):
    best_match = None
    best_score = -1
    for key, response in response_dict.items():
        similarity_score = fuzz.ratio(input_text, key)
        if similarity_score > best_score:
            best_score = similarity_score
            best_match = response if isinstance(response, str) else response(input_text)

    return best_match

def bleach():
    linkB = "https://aniwatch.to/search?keyword=bleach"
    return linkB

def jujutsu():
    linkJ = "https://aniwatch.to/search?keyword=jujutsu+kaisen"
    return linkJ


response_dict = {
    "hello": "Hello, what do you want to watch today: Anime or Movies(which is boring).",
    "movies": "Thats not a great choice, choose again.",
    "anime": "you have great taste, tell me which one do you want to watch, we dont hae much available but please choose between Bleach or Jujutsu Kaisen.",
    "same":  "no those are not same i swear. Please choose one.",
    "bleach": "Ok here you go:    " + bleach() + "   .do you want me to open the link for you? if yes then type- hell yeah ",
    "jujutsu kaisen": "Ok here you go:    " + jujutsu() + "   do you want me to open the link for you? if yes then type- you bet",
    "other": "sorry to dissoppoint you i dont have anything else right now.",
    "else": "sorry to dissoppoint you i dont have anything else right now.",
    "help":"i am only here to help you with anime, anything except that will cost you $20,000",
    "hell yeah": "It's not that hard do it your self.",
    "you bet": "It's not that hard do it your self."
}
