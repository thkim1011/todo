import json
import todo.date

def json_to_entry(json_str):
    """
    Converts json string to an Entry object.
    """
    pass


class Entry:
    """
    Entry class.
    """

    def __init__(self, description, deadline, priority, date_created, completed = False):
        """
        Constructs a new entry for the Todo List.
        description -- Description of the task to be finished 
        deadline -- Date object representing deadline
        priority -- Integer among 0, 1, 2 describing priority
        """
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.priority = priority 
        self.completed = completed 
        self.date_created = date_created

    def __str__(self):
        pass

    def json_out(self):
        """
        Decompresses each object into json object. 
        >>> date = Date(2019, 3, 8, 10, 0) # 3/8/19 at 10:00
        >>> entry = Entry("Math Homework", date, 2)
        >>> entry.json_out()
        {'description': 'Math Homework', 'deadline': ... }
        """
        return json.dumps(self, default=lambda o: getattr(o, '__dict__', o))
