"""
Main file for program. 
"""
import sys
import os
import json 
from todo.entry import Entry
from todo.date import Date
import datetime
from collections import OrderedDict

priority0 = []
priority1 = [] 
priority2 = [] 

def print_help():
    """
    Prints out the help text!
    """
    print("USAGE: todo [COMMAND]") 
    print("COMMAND:")
    help_dict = {
        "help": "Prints out the help text.",
        "add": "Adds a new entry.",
        "list": "Lists out all the todo entries.",
        "edit": "Edit an entry.",
    }
    help_dict = OrderedDict(sorted(help_dict.items()))
    for entry in help_dict:
        print(("  " + entry).ljust(10), help_dict[entry])

def add_entry():
    """
    description, deadline, priority
    Adds a new entry
    """
    time_created = datetime.datetime.now()
    date_created = (Date(time_created.year, time_created.month, time_created.day,
            time_created.hour, time_created.minute, time_created.second))
    description = input("Enter the task:") 
    #not sure if it should be y/m/d m/d/y or y/m/d
    deadline = input("What is the deadline (y/m/d):") 
    priority = input("Enter the priority (0,1,2):")
    tuple_deadline = parseDate(deadline)
    date_deadline = Date(tuple_deadline[0], tuple_deadline[1], tuple_deadline[2])

    entry = Entry(description, date_deadline, priority, int(priority), date_created)
    json_entry = entry.json_out() 

    home = os.path.expanduser("~")
    print(home) 
    file = open(home + "/.todo.json", "a")
    file.write(json_entry)

def parseDate(deadline):
    year =  0
    month = 0 
    day = 0

    search = 0
    index = 0
    while len(deadline) > 0: 
        if deadline[index] == "/" or deadline[index] == "-": 
            if search == 0: 
                year = deadline[:index]
            elif search == 1:
                month = deadline[:index]
            elif search == 2:
                day = deadline[:index]
            deadline = deadline[index:]
            search += 1
            index = 0
        else: 
            index  += 1
    return year, month, day

def list_entries():
    """
    Lists all entries
    """

    home = os.path.expanduser("~")

    with open(home + "/.todo.json") as f:
        data = json.load(f)
        for entry in data: 
            if entry["priority"] == 0:
                priority0.append(entry)
            elif entry["priority"] == 1:
                priority1.append(entry)
            else:
                priority2.append(entry)
    priorities = ["HIGH PRIORITY", "MEDIUM PRIORITY", "LOW PRIORITY"]
    for iter in range(3):
        print(priorities[iter])
        for index, entry in enumerate(priority1, 1):
            deadline = entry["deadline"] 
            print(index + ".", str(deadline["month"] + "/" str(deadline["day"] + "/" + \
                str(deadline["year"]))

def edit_entry():
    """
    Edits an entry
    """
    global priority0, priority1, priority2 
    row = input("Provide current priority:") 
    index  = input("Provide current Index of list:") 

def remove_entry():
    """
    Removes an entry
    """
    home = os.path.expanduser("~")
    with open(home + "/.todo.json") as f:
        data = json.load(f)

def mark_complete(entry):
    """
    Mark a task as completed
    """
    pass

def main():
    """
    Main function for program. 
    """
    command = sys.argv[1]
    if command == "help":
        print_help()
    if command == "add":
        add_entry()
    if command == "edit":
        edit_entry()

if __name__ == "__main__":
    main()

