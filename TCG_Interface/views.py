from django.shortcuts import render
from django.http import HttpResponse
import time

from .components.cookies import set_cookie, get_cookie






'''CARDS DISPLAY & HOME PAGE'''
# Parent function(s): collection_PARENT
# URLS:  _  / (not logged in)
#       |_  / (logged in)
#       |_  /cards/{int:id} (logged in)

def collection_PARENT(request): # PARENT
    if get_cookie(request, 'user_token') != '404:not_found':
        return(collection(request))
    else:
        return(home(request))



def home(request):
    return(render(request, 'home.html'))



def collection(request):
    
    return(render(request, 'collection.html'))

def card(request):
    return(render(request, 'card.html'))





'''ACCOUNT'''
# Parent function(s): register_PARENT, login_PARENT, profile
# URLS:  _  /register (not logged in)
#       |_  /login (not logged in)
#       |_  [REDIRECT]/ (logged in)

def register_PARENT(request): # PARENT
        return(register(request))

def register(request):
    
    return(render(request, 'register.html'))



def login_PARENT(request): # PARENT
    return(login(request))

def login(request):
    return(render(request, 'login.html'))