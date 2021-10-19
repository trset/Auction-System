import datetime

def message(msg):
    print("\n------------------- "+msg.title()+" -------------------\n")

def box_message(msg):
    s = "-" * (len(msg)+6)
    print(s + "\n|  "+msg.title()+"  |\n"+ s)   
    
def transformDate(date):
    try:
        splitted = list(map(lambda item : int(item), date.split("-")))
        if(len(splitted) != 5):
            return None
        year = splitted[0]
        month = splitted[1]
        day = splitted[2]
        hour = splitted[3]
        minute = splitted[4] 
        return datetime.datetime(year, month, day, hour, minute).strftime("%c")
    except:
      return None
