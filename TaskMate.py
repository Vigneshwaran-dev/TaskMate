import argparse

Parser = argparse.ArgumentParser(prog="TaskMate",
                                 description="Manage Your Everyday Tasks with ease",
                                 epilog="Thank You for Using TaskMate")
SubParser = Parser.add_subparsers(title="Sub-Commands",help="Commands to perform operations")


# === === Add Task group === === 

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