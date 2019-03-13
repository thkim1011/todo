"""
Main file for the program. The project todo is mainly a terminal-based
todo list. 

The first two functions of the __main__.py file are for loading and saving
the ~/.todo.json file. This file has all the data associated with the user,
and the basic effect of the program is to load the file when executed and
save the file before finishing. These two jobs are handled by the load_entries
and save_entries functions.

The next few functions implement the basic commands of the program itself.
TODO: Finish this descriptive comment!

Some of the things that needs to be implemented are the following.
* Save checkpoints of the entries file because if the program were to crash
for some reason, then we don't want to lose all of the data. 
"""
import sys
import os
import json 
import re
from todo.entry import Entry, json_to_entry
from todo.date import Date
import datetime
from collections import OrderedDict

import curses
import curses.textpad

priority0 = []
priority1 = [] 
priority2 = [] 

# Global entries variable!
entries = []


def load_entries():
    """
    Looks for the ~/.todo.json file and saves the list of entries
    stored in the file to the global variable ``entries". 
    The function assumes that the file is a list of jsonified entries. 
    """
    global entries
    home = os.path.expanduser("~")
    with open(home + "/.todo.json", "r") as f:
        json_object = json.load(f)

    # Since json_object is a list of entries...
    for json_entry in json_object:
        entries.append(json_to_entry(json_entry))

def save_entries():
    """
    Takes the global variable ``entries" and saves the list of entries
    to the file ~/.todo.json. 
    """
    home = os.path.expanduser("~")
    with open(home + "/.todo.json", "w") as f:
        f.write(jsonify(entries))


def jsonify(obj):
    """
    Takes any object and returns the json representation of the object.
    """
    return json.dumps(obj, default=lambda o: getattr(o, '__dict__', o))

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
        "guil": "List out all the todo entries in GUI.",
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
    in json format. Assume that all entries have been loaded.
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
    entries.append(entry)


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
    global priority0 
    global priority1 
    global priority2 
    home = os.path.expanduser("~")

    with open(home + "/.todo.json") as f:
        data = json.load(f)
        print(data)
        for entry in data: 
            print(entry)
            if entry["priority"] == 0:
                priority0.append(entry)
            elif entry["priority"] == 1:
                priority1.append(entry)
            else:
                priority2.append(entry)
    priorities = ["LOW PRIORITY", "MEDIUM PRIORITY","HIGH PRIORITY"]
    for iter in range(2, -1, -1):
        print("PRIORITY get", priorities[iter])
        priority = None 
        if iter == 0: 
            priority = priority0 
        elif iter == 1: 
            priority = priority1 
        else: 
            priority = priority2 
        for index, entry in enumerate(priority, 1):
            deadline = entry["deadline"] 
            print(str(index) + ".", str(deadline["month"]) + "/"  + str(deadline["day"]) + "/" + str(deadline["year"]))
            print('\t', entry["description"])

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

def draw_menu(stdscr):
    """
    Lists the entries similar to list_entries. This lists it out in 
    a GUI that is generated using the Curses package with python 
    """
    global priority0 
    global priority1 
    global priority2 
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    #add entries into list to be output later 
    home = os.path.expanduser("~")
    with open(home + "/.todo.json") as f:
        data = json.load(f)
        print(data)
        for entry in data: 
            print(entry)
            if entry["priority"] == "0":
                priority0.append(entry)
            elif entry["priority"] == "1":
                priority1.append(entry)
            else:
                priority2.append(entry)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        insert = True;

        if k == ord('j'):
            cursor_y = cursor_y + 1
        elif k == ord('k'):
            cursor_y = cursor_y - 1
        elif k == ord('l'):
            cursor_x = cursor_x + 1
        elif k == ord('h'):
            cursor_x = cursor_x - 1
        elif k == ord('d'):
            insert = False
        elif k == ord('i'):
            # insert = True
            #for editing text in the window
            tb = curses.textpad.Textbox(stdscr, insert_mode=insert)
            text = tb.edit()
            curses.flash()
            stdscr.clear()
            stdscr.addstr(0, 0, text.encode('utf-8'))
            stdscr.refresh()
            stdscr.getch()


        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title = "Curses example"[:width-1]
        subtitle = "Written by Clay McLeod"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | Todo GUI | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        start_list_y = 2
        priorities = ["LOW PRIORITY", "MEDIUM PRIORITY","HIGH PRIORITY"]
        for iter in range(2, -1, -1):
            priority_out = priorities[iter]
            boarder = "=" * (width - 1)
            stdscr.addstr(start_list_y, 1, boarder)
            start_list_y += 1
            stdscr.addstr(start_list_y, 1, priority_out)
            start_list_y += 1
            stdscr.addstr(start_list_y, 1, boarder)
            start_list_y += 1
            priority = None 
            if iter == 0: 
                priority = priority0 
            elif iter == 1: 
                priority = priority1 
            else: 
                priority = priority2 
            for index, entry in enumerate(priority, 1):
                deadline = entry["deadline"] 
                content = str(index) + ".  " +  str(deadline["month"]) + "/"  + str(deadline["day"]) + "/" + str(deadline["year"])
                stdscr.addstr(start_list_y, 3, content)
                start_list_y += 1
                stdscr.addstr(start_list_y, 5, entry["description"])
                start_list_y += 2

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Rendering some text
        # each curly brace represents one variable inside format method
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    """
    Main function for program. 
    """
    # Start the program by loading the entries
    load_entries()
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
    if command == "list":
        list_entries()
    if command == "guil":
        curses.wrapper(draw_menu)
    # End the program by saving the entries
    save_entries()

if __name__ == "__main__":
    main()

