def capitalize(fn):
    def wrapper():
        res=fn()
        res=res.upper()
        return res
    return wrapper
@capitalize

def morning_greetings():
    return "good morning"
#print(morning_greetings())

from datetime import datetime
current_time=datetime.now()
current_hour=current_time.hour
print(current_hour)
def greetings_bytime():
    if(5<=current_hour<12):
       print("good morning")
    elif(12<=current_hour<18):
        print("good evening")
    else:
       print("good night")
greetings_bytime()



