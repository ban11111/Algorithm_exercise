import datetime as date
# import poker_classification as PC
import sorts

x = date.datetime(1993, 1, 1, 00, 00, 00)
y = date.datetime(1993, 1, 1, 23, 59, 59)

# print(x == y)
# print(y.hour, x.hour)

# d = [{"h": 12}, {"d": 2}, {"c": 4}, {"c": 5}, {"c": 13}]
#
# s = sorts.quick_sort(d, 0, len(d)-1)
# print(s, "\n", d[4])

if __name__ == "__main__":
    list_list = [[4, "j"], [2, "c"], [3, "l"], [2, "s"], [5, "c"], [7, "s"], [8, "s"], [9, "s"], [14, "f"]]
    maxnum = max(list_list)
    s = sorts.bubsort(list_list)
    print(s, "\n")
    # s = list_list.remove(maxnum)
    # print(list_list, s)

    # flag, m, mi = PC.class_flush(s)
    # print(flag, m, mi)
