import argparse
import pickle
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
        with open("id.bin","wb+") as BinFile:
            IdList = pickle.load(BinFile)
    except EOFError:
        IdList = [0]
    
    CurrentId = IdList[0] + 1
    IdList.insert(0,CurrentId)
    with open("id.bin",'wb') as BinFile:
        pickle.dump(IdList,BinFile)

def AddTask(args):
    pass


AddParser = SubParser.add_parser("add")
AddGroup = AddParser.add_argument_group()

AddGroup.add_argument("name",help="Add Your Task Name")
AddGroup.add_argument("-d","--description",help="Add Your Task Description")
AddGroup.add_argument("-s","--status",help="Add Your Task Status")
AddGroup.add_argument("-p","--priority",help="Add Your Task Priority")

AddGroup.set_defaults(func=AddTask)

args = Parser.parse_args()
args.func(args)