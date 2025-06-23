import argparse
import json
from tabulate import tabulate
from datetime import datetime

Headers = ["Id","Task Name","Description","Status","Priority","Created at","Last Updated at"]

Parser = argparse.ArgumentParser(prog="TaskMate",
                                 description="Manage Your Everyday Tasks with ease",
                                 epilog="Thank You for Using TaskMate")
SubParser = Parser.add_subparsers(title="Sub-Commands",help="Commands to perform operations")


# === === Add Task group === === 


def CurrentTime():
    x = datetime.now()
    TimeStr = "%s %s %s %s %s:%s %s"
    TimeVal = (x.strftime('%d'),
               x.strftime('%b'),
               x.strftime('%Y'),
               x.strftime('%a'),
               x.strftime('%I'),
               x.strftime('%M'),
               x.strftime('%p'))

    currenttime = TimeStr%TimeVal
    return currenttime

def UpdateId():
    try:
        with open("id.json","r") as JSONFile:
            IdList = json.load(JSONFile)
    except FileNotFoundError:
        IdList = [0]
    
    CurrentId = IdList[0] + 1
    IdList.insert(0,CurrentId)
    with open("id.json",'w') as JSONFile:
        json.dump(IdList,JSONFile,indent=4)
    
    return CurrentId

def AddTask(args):
    currenttime = CurrentTime()
    currentid = UpdateId()

    TaskList = {"TaskId":currentid,"TaskName":args.name,"TaskDescription":args.description,"TaskStatus":args.status,"TaskPriority":args.priority,"CreatedTime":currenttime,"LastUpdatedTime":currenttime}

    try:
        with open("log.json",'r') as JSONFile:
            AlltaskList = json.load(JSONFile)
    except FileNotFoundError:
        AlltaskList = []
    AlltaskList.append(TaskList)
    
    with open('log.json','w') as JSONFile:
        json.dump(AlltaskList,JSONFile,indent=4)
    print(f"Task Created Successfully (ID: {currentid})")


AddParser = SubParser.add_parser("add")
AddGroup = AddParser.add_argument_group("Add Your Task's")

AddGroup.add_argument("name",help="Add Your Task Name")
AddGroup.add_argument("-d","--description",help="Add Your Task Description")
AddGroup.add_argument("-s","--status",choices=["Todo","In-progress","Done"],default="Todo",help="Add Your Task Status")
AddGroup.add_argument("-p","--priority",choices=["Low","Medium","High"],default="Low",help="Add Your Task Priority")

AddGroup.set_defaults(func=AddTask)


# === === list Task group === === 



def ListFilter(filter):
    try:
        with open('log.json','r') as JSONFile:
            AllTaskList = json.load(JSONFile)
    except FileNotFoundError:
        print("Add a Task first to list")
    
    Listed = []

    for Taskdict in AllTaskList:
        if Taskdict['TaskStatus'] == str(filter):
            Listed.append(list(Taskdict.values()))
    
    print(tabulate(Listed,Headers,tablefmt="rounded_grid"))

def ListAll():
    try:
        with open('log.json','r') as JSONFile:
            AllTaskList = json.load(JSONFile)
    except FileNotFoundError:
        print("Add a Task first to list")
    
    Listed = []

    for Taskdict in AllTaskList:
        Listed.append(list(Taskdict.values()))
    
    print(tabulate(Listed,Headers,tablefmt="rounded_grid"))

def ListTask(args):
    if args.filter:
        ListFilter(args.filter)
    else:
        ListAll()

ListParser = SubParser.add_parser('list')
Listgroup = ListParser.add_argument_group("List Your tasks based on Status")

Listgroup.add_argument("filter",choices=['Done','In-progress','Todo'],nargs='?')

Listgroup.set_defaults(func=ListTask)


# === === update Task group === === 



def UpdateTask(args):
    TaskId = int(str(args.id))

    try:
        with open('log.json','r') as JSONFile:
            AllTaskList = json.load(JSONFile)
    except FileNotFoundError:
        print("Add a Task first to update")

    for Taskdict in AllTaskList:
        if Taskdict['TaskId'] == int(str(TaskId)):
            
            if args.NewName:
                Taskdict["TaskName"] = str(args.NewName)
                Taskdict['LastUpdatedTime'] = CurrentTime()
            if args.NewDescription:
                Taskdict["TaskDescription"] = str(args.NewDescription)
                Taskdict['LastUpdatedTime'] = CurrentTime()
            if args.NewPriority:
                Taskdict["TaskPriority"] = str(args.NewPriority)
                Taskdict['LastUpdatedTime'] = CurrentTime()

            AllTaskList.pop(TaskId-1)
            AllTaskList.insert(TaskId-1,Taskdict)
    
    with open('log.json','w') as JSONFile:
        json.dump(AllTaskList,JSONFile,indent=4)
    
    print('Task Edited Successfully')

UpdateParser = SubParser.add_parser('update')
UpdateGroup = UpdateParser.add_argument_group("Update your Task's")

UpdateGroup.add_argument('id')
UpdateGroup.add_argument('-n','--NewName')
UpdateGroup.add_argument('-d','--NewDescription')
UpdateGroup.add_argument('-p','--NewPriority')

UpdateGroup.set_defaults(func=UpdateTask)

# add statuschange sort 
# === === delete Task group === === 


def DeleteTask(args):

    if args.id:
        try:
            with open('log.json','r') as JSONFile:
                AllTaskList = json.load(JSONFile)
        except FileNotFoundError:
            print('Add a task first to delete')
        
        deletedtask = AllTaskList.pop(int(str(args.id))-1)
        print(f"{deletedtask["TaskName"]} has been successfully deleted")

        with open('log.json','w') as JSONFile:
            json.dump(AllTaskList,JSONFile,indent=4)

    else:
        User = input("Do you want to delete all the task's (Y/n) : ")
        if User.lower() == 'Y':
            with open('log.json','w') as JSONFile:
                json.dump([],JSONFile,indent=4)
            print("All Task's has been successfully deleted")
        else:
            print('Woof!, What a close save')

Deleteparser = SubParser.add_parser('delete')
DeleteGroup = Deleteparser.add_argument_group("Delete Your Task's")

DeleteGroup.add_argument('id',help="Enter The Id of the task to delete",nargs='?')

DeleteGroup.set_defaults(func=DeleteTask)


# === === mark status Task group === === 


def MarkStatus(args):
    TaskId = int(str(args.id))
    TaskStatus = str(args.status)

    try:
        with open('log.json','r') as JSONFile:
            AllTaskList = json.load(JSONFile)
    except FileNotFoundError:
        print("Add the Task First to change the status")

    for TaskDict in AllTaskList:
        if TaskDict['TaskId'] == TaskId:
            TaskDict['TaskStatus'] = TaskStatus
            TaskDict['LastUpdatedTime'] = CurrentTime()
            print("Task Status changed successfully")
        
    with open('log.json','w') as JSONFile:
        json.dump(AllTaskList,JSONFile,indent=4)

MarkStatusParser = SubParser.add_parser('mark')
MarkStatusGroup = MarkStatusParser.add_argument_group('Change the status of your Task')

MarkStatusGroup.add_argument('id',help="Enter Your Task Id to change status")
MarkStatusGroup.add_argument('status',choices=["Done","Todo","In-progress"],help="Enter the task status to be changed")

MarkStatusGroup.set_defaults(func=MarkStatus)


args = Parser.parse_args()
args.func(args)