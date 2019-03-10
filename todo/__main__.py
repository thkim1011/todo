"""
Main file for program. 
"""
import sys
import os
import json 
import re
from todo.entry import Entry
from todo.date import Date
import datetime
from collections import OrderedDict

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
    Adds a new entry to our todo list. The main effect of this function is to
    query the user for the specific data associated with an entry (that is,
    description, deadline, and priority), and appends this to ~/.todo.json.
    Recall that the structure of ~/.todo.json is a list of Entry objects
    in json format. 
    """
    #time_created = datetime.datetime.now()
    #date_created = (Date(time_created.year, time_created.month, time_created.day,
    #        time_created.hour, time_created.minute, time_created.second))
    description = input("Enter the task: ") 
    deadline_date = input("What is the deadline date (MM/DD/YY): ") 
    deadline_time = input("What is the deadline time (HH:MM (AM/PM)): ")
    priority = input("Enter the priority (0,1,2): ")
    tuple_deadline = parse_date(deadline_date)
    date_deadline = Date(tuple_deadline[0], tuple_deadline[1], tuple_deadline[2])

    entry = Entry(description, priority, date_deadline, int(priority))
    json_entry = entry.json_out() 

    home = os.path.expanduser("~")
    print(home) 
    with open(home + "/.todo.json", "a") as file:
        file.write(json_entry)

def parse_date(deadline_date):
    """
    Given a date in the form MM/DD/YY or MM/DD/YYYY, returns
    the integers MM, DD, and YYYY (or YY) in this order.
    """
    deadline_split = re.split('\\/|\\-', deadline_date)
    return int(deadline_split[0]), int(deadline_split[1]), int(deadline_split[2])

def list_entries():
    """
    Lists all entries
    """

    priority0 = []
    priority1 = [] 
    priority2 = [] 
    if os.path.isfile("~/todo.json"):
        with open('~/todo.json') as f:
            data = json.load(f)
        for entry in data: 
            if entry["priority"] == 0:
                priority0.append(entry)
            elif entry["priority"] == 1:
                priority1.append(entry)
            else:
                priority2.append(entry)

def edit_entry():
    """
    Edits an entry
    """
    pass

def remove_entry():
    """
    Removes an entry
    """
    home = os.path.expanduser("~")
    file = open(home + "/.todo.json", "a")
    file.write(json_entry)

    with open() as f:
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
    if len(sys.argv) == 1:
        print_help()
        return
    command = sys.argv[1]
    if command == "help":
        print_help()
    if command == "add":
        add_entry()
    if command == "edit":
        edit_entry()

if __name__ == "__main__":
    main()

