class Entry:
    """
    Entry class.
    """

    def __init__(self, description, deadline, priority):
        """
        Constructs a new entry for the Todo List.

        description -- Description of the task to be finished 
        deadline -- Date object representing deadline
        priority -- Integer among 0, 1, 2 describing priority
        """
        self.description = description
        self.deadline = deadline
        self.priority = priority


