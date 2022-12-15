from django.shortcuts import render
logged_in = False





'''HOME PAGE'''
# Parent function: display
# Permissions:
# Url: /

def home(request):
    return(render, 'home.html')





'''ACCOUNT COLLECTION DISPLAY'''
# Parent function: display
# Permissions: logged_in
# Url: /

def collection(request):
    if logged_in == True:
        collection___logged_in(request)
    else:
        home(request)

def collection___logged_in(request):
    return(render, 'collection.html')





#