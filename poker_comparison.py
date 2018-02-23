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
        # print(arank, brank)
        avalue = pc.rank_value(alist)
        bvalue = pc.rank_value(blist)

        if avalue > bvalue:
            return 1
        elif avalue < bvalue:
            return 2
        else:
            return 0


if __name__ == "__main__":
    line0 = {"alice": "8sAhAc7sJc6hQd", "bob": "6s7c8sAhAc7sJc", "result": 2}
    line5 = {"alice": "7d6hJcTs8h7s4d", "bob": "Qd9h7d6hJcTs8h", "result": 2}
    line220 = {"alice": "Qd6c7d5d5c9cTs", "bob": "Jh8cQd6c7d5d5c", "result": 0}
    line1 = {"alice": "5d6dJcJh7d", "bob": "Js7cKdKh3c", "result": 0}
    line8 = {"alice": "6s5h4c3s2c", "bob": "As2h3s4c5s", "result": 0}
    line14 = {"alice": "Ac9d6h3dTc", "bob": "2h6d8d7sJh", "result": 0}
    r = compare(line5)
    print(r)
