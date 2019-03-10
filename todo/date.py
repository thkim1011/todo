class Date:
    """
    Date object for entries. 
    """
    def __init__(self, year, month, day, hour, minute, second = 0):
        """ 
        second is only useful for tracking the time ENTRY was created
        """
        self.year = year 
        self.month = month 
        self.day = day 
        self.hour = hour
        self.minute = minute

    def __lt__(self, other_date):
        pass

    def __str__(self):
        """
        Prints out the string representation of a given date. 
        """
        months = ["January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"]
        return str(months[self.month - 1]) + " "\
                + str(self.day) + ", "\
                + str(self.year)
