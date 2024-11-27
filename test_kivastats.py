"""
File: test_kivastats.py
Initial author: Mihaela
Developer:
Date:
"""
from kivastats import KivaStats


def test_total_loan():
    """
    Test `total_loan_amount()` method with all 3 CSV files.
    """
    ks_obj = KivaStats('data_25.csv')
    print(ks_obj)
    # expected = 1250.0
    # actual = ks_obj.total_loan()
    # print(f'Expected is {expected}, Actual is {actual}')


def test_avg_lenders():
    """
    Test `avg_lenders_per_loan()` method with all 3 CSV files.
    """


def test_smallest_loan_country():
    """
    Test `smallest_loan_country()` method with all 3 CSV files.
    """
    ks_obj = KivaStats('data_1.csv')
    expected = ['Azerbaijan']
    actual = ks_obj.smallest_loan_country()
    print(f'Expected is {expected}, Actual is {actual}')

    ks_obj = KivaStats('data_5.csv')
    expected = ['El Salvador', 'Paraguay']
    actual = ks_obj.smallest_loan_country()
    print(f'Expected is {expected}, Actual is {actual}')

    ks_obj = KivaStats('data_5.csv')
    expected = ['Nicaragua', 'Philippines', 'Madagascar']
    actual = ks_obj.smallest_loan_country()
    print(f'Expected is {expected}, Actual is {actual}')


def test_time_per_dollar():
    """
    Test `time_per_dollar_raised()` method with `data_1.csv` and `data_5.csv`
    """


def test_write_data():
    """
    Test write_data() method with `data_25.csv` by just calling the method.
    """
    ks_obj = KivaStats('data_25.csv')
    ks_obj.write_data('output.csv')


def main():
    """
    Call the testing functions defined in this module
    """
    test_total_loan()
    # test_write_data()


main()
