import poker_transformation as pt
import poker_classification as pc


# 比较大小
def compare(line):
    alice = pt.str2list_list(line["alice"])
    bob = pt.str2list_list(line["bob"])
    arank, alist = pc.rank_classify(alice)
    brank, blist = pc.rank_classify(bob)

    print(arank, brank)
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
    ghost = []
    ghost.append({"alice": "3s4s5s2sXn", "bob": "7s2s5s4s3sXn", "result": 0})
    ghost.append({"alice":"9sTcXnKh4d7hJs","bob":"7sQh9sTcXnKh4d","result":0})

    # for i in ghost:
    #     r = compare(i)
    #     print(r)
    r = compare(ghost[1])
    print(r)
