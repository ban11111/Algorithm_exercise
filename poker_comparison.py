import poker_transformation as pt
import poker_classification as pc


def compare(line):
    alice = pt.str2list_list(line["alice"])
    bob = pt.str2list_list(line["bob"])
    arank, alist = pc.rank_classify(alice)
    brank, blist = pc.rank_classify(bob)

    if arank > brank:
        return 1
    elif arank < brank:
        return 2
    else:
        avalue = pc.rank_value(alist)
        bvalue = pc.rank_value(blist)

        if avalue > bvalue:
            return 1
        elif avalue < bvalue:
            return 2
        else:
            return 0


if __name__ == "__main__":
    line0 = {"alice": "8sAhAc7sJc6hQd", "bob": "6s7c8sAhAc7sJc", "result": 0}
    line5 = {"alice": "Kd5s4d7h5cJsQc", "bob": "Tc4cKd5s4d7h5c", "result": 0}
    line220 = {"alice": "Qd6c7d5d5c9cTs", "bob": "Jh8cQd6c7d5d5c", "result": 0}
    r = compare(line220)
    print(r)
