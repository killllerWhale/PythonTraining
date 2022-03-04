class AmericanDateFormat:
    def __init__(self,year ,month ,day):
        self.year = year
        self.month = month
        self.day = day

    def date_format(self):
        day = "0"+str(self.day) if self.day<10 else str(self.day)
        month = "0"+str(self.month) if self.month<10 else str(self.month)
        return month +"."+ day +"."+ str(self.year)


class EuropeanDateFormat:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def date_format(self):
        day = "0" + str(self.day) if self.day < 10 else str(self.day)
        month = "0" + str(self.month) if self.month < 10 else str(self.month)
        return day + "." + month + "." + str(self.year)



#american = AmericanDateFormat(2000, 4,10)
#european = EuropeanDateFormat(2000, 4,10)
american = AmericanDateFormat(2000, 12,10)
european = EuropeanDateFormat(2000, 1,7)
print(american.date_format())
print(european.date_format())
