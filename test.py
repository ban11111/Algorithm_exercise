import datetime as date
import sorts

x = date.datetime(1993, 1, 1, 00, 00, 00)
y = date.datetime(1993, 1, 1, 23, 59, 59)

# print(x == y)
# print(y.hour, x.hour)

d = [{"Qh": 12}, {"2d": 2}, {"4c": 4}, {"5c": 5}, {"Kc": 13}]

s = sorts.quick_sort(d, 0, len(d)-1)
print(s)
