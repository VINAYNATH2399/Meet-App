import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    create_event_file=open(events_json_file,'w+')
    event_file_1={     
            "Id":Event_ID,
            "Name":Event_Name,
            "Organizer":org,
            "Start Date":Start_Date,
            "Start Time":Start_Time,
            "End Date":End_Date,
            "End Time":End_Time,
            "Users Registered":Users_Registered,
            "Capacity":Capacity,
            "Seats Available":Availability
        }
    try:
        content=json.load(create_event_file)
        if event_file_1 not in content:
            content.append(event_file_1)
            create_event_file.seek(0)
            create_event_file.truncate()
            json.dump(content,create_event_file)
        
    except JSONDecodeError:
        list_1=[] 
        list_1.append(event_file_1)
        json.dump(list_1,create_event_file)
        create_event_file.close()
    

def View_Events(org,events_json_file):
    name=org
    file=open(events_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Organizer"]==org:
            dit=[{
                "ID":content[i]['Id'],
                "Name":content[i]['Name'],
                "Organizer":content[i]['Organizer'],
                "Start Date":content[i]['Start Date'],
                "Start Time":content[i]['Start Time'],
                "End Date":content[i]['End Date'],
                "End Time":content[i]['End Time'],
                "Users Registered":content[i]['Users Registered'],
                "Capacity":content[i]['Capacity'],
                "Seats Available":content[i]['Seats Available'],
            }]
            return dit
        else:
            pass
    file.close()
       

def View_Event_ByID(events_json_file,Event_ID):
    event_file=open(events_json_file,'r+')
    event_file_content=json.load(event_file)
    for i in range(len(event_file_content)):
        if event_file_content[i]["Id"]==Event_ID:
              d=[{
                "ID":event_file_content[i]['Id'],
                "Name":event_file_content[i]['Name'],
                "Organizer":event_file_content[i]['Organizer'],
                "Start Date":event_file_content[i]['Start Date'],
                "Start Time":event_file_content[i]['Start Time'],
                "End Date":event_file_content[i]['End Date'],
                "End Time":event_file_content[i]['End Time'],
                "Users Registered":event_file_content[i]['Users Registered'],
                "Capacity":event_file_content[i]['Capacity'],
                "Seats Available":event_file_content[i]['Seats Available'],
            }]
    
    return d
   
    f.close()


def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    file_1=open(events_json_file,'w+')
    content=json.load(file_1)
    organizer=org
    for i in range(len(content)):
        if content[i]["Id"]==event_id:
            if detail_to_be_updated=='Name':
                content[i]['Name']=updated_detail
            elif detail_to_be_updated=='Start Date':
                content[i]['Start Date']=updated_detail
            elif detail_to_be_updated=='Start Time':
                content[i]['Start Time']=updated_detail
            elif detail_to_be_updated=='End Date':
                content[i]['End Date']=updated_detail
            elif detail_to_be_updated=='End Time':
                content[i]['End Time']=updated_detail
            else:
                return False  
            file_1.seek(0)
            file_1.truncate()
            json.dump(content,file_1)
            file_1.close() 
    return True

def Delete_Event(org,events_json_file,event_ID):
    file=open(events_json_file,'r+')
    content=json.load(file)
    id=event_ID
    for i in range(len(content)):
        if content[i]["Id"]==event_ID:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file)
            file.close()
            return True
        else:
            return False

def Register_for_Event(events_json_file,event_id,Full_Name):
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    file_1=open(events_json_file,'w+')
    content=json.load(file_1)
    for i in range(len(content)):
        if content[i]["Id"]==event_id:
            content[i]["Users Registered"].append(Full_Name)
            content[i]['Seats Available']-=1
    file_1.seek(0)
    file_1.truncate()
    json.dump(content, file_1)
    file_1.close()
    return True


def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f=open(events_json_file,'r+')
    content=json.load(f)
    print(content)
    for i in range(len(content)):
        if Full_Name in content[i]['Users Registered']:
            datetime. strptime(content[i]['Start Date'], '%y/%m/%d')
            if datetime. strptime(content[i]['Start Date'], '%y/%m/%d')>=date_today:
                if content[i]['Start Time']>=now:
                    upcoming_ongoing.append(content[i])
                    return upcoming_ongoing
                else:
                    pass
            else:
                pass
    

def Update_Password(members_json_file,Full_Name,new_password):
    file_1=open(members_json_file,'w+')
    content=json.load(file_1)
    for i in range(len(content)):
        if content[i]["Full Name"]==Full_Name:
            content[i]["Password"]=new_password
    file_1.seek(0)
    file_1.truncate()
    json.dump(content, file_1)
    file_1.close()
    return True

def View_all_events(events_json_file):
    details=[]
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details