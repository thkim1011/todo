import json 

class Date:
    """
    """
    def __init__(self, year, month, day, hour, minute):
        self.year = year 
        self.month = month 
        self.day = day 
        self.hour = hour
        self.minute = minute

    def __lt__(other_date):
        pass

    def json_out(self):
        """ 
        creeate 
        """
        return self.__dict__

