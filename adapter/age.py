import datetime


class AgeCalculator(object):

    def __init__(self, birthday):
        self.year, self.month, self.day = (int(x) for x in birthday.split('-'))

    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split('-'))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age


class DateAgeAdapter(object):

    def _str_age(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        birthday = self._str_age(birthday)
        self.age_calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_age(date)
        return self.age_calculator.calculate_age(date)


class AgeableDate(datetime.date):
    def split(self, char):
        return self.year, self.month, self.day
