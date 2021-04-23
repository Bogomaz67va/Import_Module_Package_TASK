from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
import datetime


time = datetime.datetime.now()
if __name__ == '__main__':
    cs()
    ge()
    print(time)