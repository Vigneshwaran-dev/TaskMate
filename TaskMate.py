import argparse
import json
from datetime import datetime

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
        with open("id.json","w+") as JSONFile:
            IdList = json.load(JSONFile)
    except json.JSONDecodeError:
        IdList = [0]
    
    CurrentId = IdList[0] + 1
    IdList.insert(0,CurrentId)
    with open("id.json",'w') as JSONFile:
        json.dump(IdList,JSONFile)
    
    return CurrentId

def AddTask(args):
    currenttime = CurrentTime()
    currentid = UpdateId()

    TaskList = [currentid,args.name,args.description,args.status,args.priority,currenttime]

    try:
        with open("log.json",'w+') as JSONFile:
            AlltaskList = json.load(JSONFile)
    except json.JSONDecodeError:
        AlltaskList = []
    AlltaskList.append(TaskList)
    
    with open('log.json','w') as JSONFile:
        json.dump(AlltaskList,JSONFile)
    print(f"Task Created Successfully (ID: {currentid})")


AddParser = SubParser.add_parser("add")
AddGroup = AddParser.add_argument_group("Add Your Task's")

AddGroup.add_argument("name",help="Add Your Task Name")
AddGroup.add_argument("-d","--description",help="Add Your Task Description")
AddGroup.add_argument("-s","--status",choices=["Todo","In-progress","Done"],default="Todo",help="Add Your Task Status")
AddGroup.add_argument("-p","--priority",choices=["Low","Medium","High"],default="Low",help="Add Your Task Priority")

AddGroup.set_defaults(func=AddTask)

args = Parser.parse_args()
args.func(args)