from django.shortcuts import render
logged_in = False





'''HOME PAGE'''
# Parent function: collection

def home(request):
    return(render(request, 'home.html'))





'''ACCOUNT COLLECTION DISPLAY'''
# Parent function: collection (itself)
# URLS:  _  / (not logged in)
#       |_  / (logged in)
#       |_  /cards/{int:id} (logged in)

def collection(request): # PARENT
    if logged_in == True:
        return(collection___logged_in(request))
    else:
        return(home(request))

def collection___logged_in(request):
    return(render(request, 'collection.html'))





#