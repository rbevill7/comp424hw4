"""
File: kivastats.py
Initial authors: COMP 424 course instructors
Developer:
"""
from csv import DictReader


class KivaStats:
    """
    Analyze Kiva statistics data.
    """
    def __init__(self, filename):
        """
        Initialize instance variable `self.data` with information from
        the file named `filename`, located in the same directory as
        `kivastats.py`.
        The file has lines of comma-separated strings. First line has heading
        names, and the rest of the lines have data values corresponding to each
        heading, as folows:
            - loan amount
            - name of the country that got the loan
            - time it took to raise the loan
            - number of lenders who contributed to the loan.
        The instance variable `self.data` is a list of dictionaries
            keys are: 'loan', 'country', 'raising_time', and 'lenders'
            values: strings representing loan, country, time, and number of
                lenders
        Example: For the file named 'data_1.csv', the function reaturns a list
        with a single dictionary:
            [{'loan':1250.0, 'country': 'Azergaijan', 'raising_time':193075,
                'lenders':31}]

        :param filename: string
        :return: KivaStats object
        """
        self.data = []
        try:
            with open(filename, mode='r', encoding='utf-8') as csv_file:
                csv_reader = DictReader(
                    csv_file, delimiter=',', quotechar='"'
                )
                self.data = list(csv_reader)
        except IOError as err:
            print(err)

    def __str__(self):
        """
        Returns string representation of the list `self.data`. The elements
        of the list are dictionaries.
        """
        return str(self.data)

    def total_loan(self):
        """
        Calculate the total amount of loans by summing up the values
        corresponding to the 'loan' key in `self.data` dictionary.
        Example: if the dictionry is {'loan':1250.0, 'country': 'Azergaijan',
            'raising_time':193075, 'lenders':31}
        the method returns 1250.0
        :return: float
        """
        return 0.0

    def avg_lenders(self):
        """
        Calculate the average number of lenders who contributed to a loan.
        :return: integer
        """
        return 0

    def smallest_loan_country(self):
        """
        Find the list of countries that received the smallest loan.
        :return: list of strings
        """
        return []

    def time_per_dollar(self):
        """
        Find the time per dollar raised for each loan by dividing raising
        time value for each loan by loan amount.
        :return: list of floats
        """
        return []

    def write_data(self, fileout):
        """
        Write to a textfile named `fileout`:
            - the headings 'loan', 'country', 'raising_time', 'lenders', and
                'time_per_dollar'
            - all subsequent lines have the content of each dictionary in
            in `self.data`, plus the time per dollar raised for each loan.
            Hint: get the list of time per dollar information by calling
                `self.time_per_dollar_raised()` method.
        """
