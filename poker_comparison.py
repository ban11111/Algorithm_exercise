import poker_transformation as pt
import poker_classification as pc
import poker_classification_quicksort as pcq


# 比较大小
def compare(line):
    alice = pt.str2list_list(line["alice"])
    bob = pt.str2list_list(line["bob"])
    arank, alist = pc.rank_classify(alice)
    brank, blist = pc.rank_classify(bob)

    # print(arank, brank)
    # print(alist, blist)
    if arank > brank:
        return 1
    elif arank < brank:
        return 2
    else:
        if arank == 9 or arank == 5:
            avalue = pc.rank_straight_value(alist)
            bvalue = pc.rank_straight_value(blist)
        else:
            avalue = pc.rank_value(alist)
            bvalue = pc.rank_value(blist)

        if avalue > bvalue:
            return 1
        elif avalue < bvalue:
            return 2
        else:
            return 0


def compare_quick(line):
    alice = pt.str2list_list(line["alice"])
    bob = pt.str2list_list(line["bob"])
    arank, alist = pcq.quick_classify(alice)
    brank, blist = pcq.quick_classify(bob)

    # print(arank, brank)
    # print(alist, blist)
    if arank > brank:
        return 1
    elif arank < brank:
        return 2
    else:
        if arank == 9 or arank == 5:
            avalue = pc.rank_straight_value(alist)
            bvalue = pc.rank_straight_value(blist)
        else:
            avalue = pc.rank_value(alist)
            bvalue = pc.rank_value(blist)

        if avalue > bvalue:
            return 1
        elif avalue < bvalue:
            return 2
        else:
            return 0


# 测试
if __name__ == "__main__":
    ghost = list()
    ghost.append({"alice": "Kd5s4d7h5cJsQc", "bob": "Tc4cKd5s4d7h5c", "result": 2})
    ghost.append({"alice": "9sTcXnKh4d7hJs", "bob": "7sQh9sTcXnKh4d", "result": 0})
    ghost.append({"alice": "XnAsQd4hKh4dJc", "bob": "5cJhXnAsQd4hKh", "result": 0})
    ghost.append({"alice": "4c5h3s7h9h2hAh", "bob": "4hXn4c5h3s7h9h", "result": 2})
    ghost.append({"alice": "Xn3hTd5h4dKh8h", "bob": "6d7dXn3hTd5h4d", "result": 1})
    ghost.append({"alice": "Ad5dXn8d2c4d2d", "bob": "Xn8d2c4d2d9h4s", "result": 1})

    # for i in ghost:
    #     r = compare(i)
    #     print(r)
    r = compare_quick(ghost[0])
    print(r)
