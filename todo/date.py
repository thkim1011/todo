import json 

class Date:
    """
    """
    def __init__(self, year, month, day, time): 
        self.year = year 
        self.month = month 
        self.day = day 
        self.time = time 

    def __lt__(other_date):
        pass

    def json_out(self):
        """ 
        creeate 
        """
        return self.__dict__

