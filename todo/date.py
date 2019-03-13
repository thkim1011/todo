def json_to_date(json_date):
    """
    Converts json object to a Date object.
    >>> print(json_to_date({"year": 2019, "month": 10, "day": 12, "hour": None, "minute": None}))
    October 12, 2019
    """
    return Date(year=json_date["year"],
            month=json_date["month"],
            day=json_date["day"],
            hour=json_date["hour"],
            minute=json_date["minute"])

class Date:
    """
    Date object for entries. 
    """
    def __init__(self, year, month, day=None, hour=None, minute=None):
        """ 
        second is only useful for tracking the time ENTRY was created
        """
        self.year = year 
        self.month = month 
        self.day = day 
        self.hour = hour
        self.minute = minute

    def __lt__(self, other_date):
        """
        Compares two dates.
        """
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
