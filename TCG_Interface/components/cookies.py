from django.http import HttpResponse





def set_cookie(data1, data2, data3, data4):
    response = HttpResponse("Cookie set")
    response.set_cookie(data1, data2, data3, data4)
    return response

def get_cookie(request, querry):
    if querry in request.COOKIES:
        data = request.COOKIES[querry]
    else:
        data = '404:not_found'
    return data