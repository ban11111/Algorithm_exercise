import datetime as date
import sorts

x = date.datetime(1993, 1, 1, 00, 00, 00)
y = date.datetime(1993, 1, 1, 23, 59, 59)

# print(x == y)
# print(y.hour, x.hour)

d = [{"h": 12}, {"d": 2}, {"c": 4}, {"c": 5}, {"c": 13}]

s = sorts.quick_sort(d, 0, len(d)-1)
print(s, "\n", d[4])

if __name__ == "__main__":
    for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]:
        monthlist = [int(month / 10 % 10), int(month % 10)]
        i = 3 if month == 2 else 4
        for date1 in range(0, i):
            if date1 not in monthlist:
                tmpset2 = monthlist + [date1]
                j = 1 if date1 == 0 else 0
                if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and date1 == 3:
                    i = 2
                if (month == 4 or month == 6 or month == 9) and date1 == 3:
                    i = 1
                if month == 2 and date1 == 2:
                    i = 10 if ((2003 % 4 == 0 and 2003 % 100 != 0) or 2003 % 400 == 0) else 9
                if (month == 2 and date1 < 2) or (month != 2 and date1 < 3):
                    i = 10
                for date2 in range(j, i):
                    if date2 not in tmpset2:
                        tmpset3 = tmpset2 + [date2]
                        print(tmpset3)