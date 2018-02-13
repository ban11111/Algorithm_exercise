# coding: utf-8
import poker_dict as PD
import time
import sorts
import poker_transformation as PT


pokerDicts = PD.PokerDicts()
pokerDict = pokerDicts.pokerDict
numDict = pokerDicts.numDict

if __name__ == "__main__":
    start = time.clock()

    data = PT.file2json("./jsonfiles/seven_cards.json")

    firstMatch = data["matches"]
    for i in firstMatch:
        a = i["alice"]
        alice = PT.str2list(a)
        # print(numDict, "\n", pokerDict)
        # alice_dict = PT.list2dict(alice, pokerDict)
        d = PT.list2dict_list(alice, pokerDict)
        s = sorts.quick_sort(d, 0, len(d) - 1)
    end = time.clock()
    print("%f秒" % (end - start))

    start = time.clock()
    for i in firstMatch:
        a = i["alice"]
        alice = PT.str2list(a)
        d = PT.list2list_list(alice, pokerDict)
        s = sorts.quick_sort2(d, 0, len(d) - 1)
    end = time.clock()
    print("%f秒" % (end - start))
