import datetime
from ..models import User





def generate_user_token():
    current_datetime = datetime.datetime.now()
    new_user_id = User.objects.count() + 1

    token = '|' + current_datetime + '|' + str(new_user_id) + '|'
    
    return token

print(generate_user_token())

