from statistics import mean


class MinStat:
    list_number = []

    def add_number(self, number):
        MinStat.list_number.append(number)

    def result(self):
        return min(MinStat.list_number) if len(MinStat.list_number)!=0 else "None "


class MaxStat:
    list_number = []

    def add_number(self, number):
        MaxStat.list_number.append(number)

    def result(self):
        return max(MaxStat.list_number) if len(MaxStat.list_number)!=0 else "None "


class AverageStat:
    list_number = []

    def add_number(self, number):
        AverageStat.list_number.append(float(number))

    def result(self):
        return '{:<05.7f}'.format(mean(AverageStat.list_number)) if len(AverageStat.list_number)!=0 else "None "


#values = [1, 0, 0]
values = [1, 2, 4, 5]
minNumber = MinStat()
maxNumber = MaxStat()
averageNumber = AverageStat()
for v in values:
    minNumber.add_number(v)
    maxNumber.add_number(v)
    averageNumber.add_number(v)
print(maxNumber.result(),minNumber.result(),averageNumber.result())