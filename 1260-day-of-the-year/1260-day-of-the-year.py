from datetime import datetime 

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        given_date = datetime.strptime(date,"%Y-%m-%d") 

        start_of_year = datetime(given_date.year, 1,1)

        return (given_date - start_of_year).days + 1