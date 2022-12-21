from django.shortcuts import render
logged_in = False





'''HOME PAGE'''
# Parent function: collection

def home(request):
    return(render(request, 'home.html'))





'''CARDS DISPLAY'''
# Parent function: collection (itself)
# URLS:  _  / (not logged in)
#       |_  / (logged in)
#       |_  /cards/{int:id} (logged in)

def collection_PARENT(request): # PARENT
    if logged_in == True:
        return(collection(request)) # --> card
    else:
        return(home(request))

def collection(request):
    
    return(render(request, 'collection.html'))

def card(request):
    return(render(request, 'card.html'))





'''REGISTER'''
# Parent function: register (itself)
# URLS:  _  /register (not logged in)
#       |_  [REDIRECT]/ (logged in)

def register_PARENT(request): # PARENT
    if logged_in == False:
        return(register(request))
    else:
        return(collection(request))

def register(request):
    return(render(request, 'register.html'))





'''LOGIN'''
# Parent function: register (itself)
# URLS:  _  /login (not logged in)
#       |_  [REDIRECT]/ (logged in)

def login_PARENT(request): # PARENT
    if logged_in == False:
        return(login(request))
    else:
        return(collection(request))

def login(request):
    return(render(request, 'login.html'))