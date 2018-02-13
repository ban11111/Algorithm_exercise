# coding: utf-8
import poker_dict as PD
import time


pokerDicts = PD.PokerDicts()
pokerDict = pokerDicts.pokerDict
numDict = pokerDicts.numDict

if __name__ == "__main__":
    start = time.clock()

    print(numDict, "\n", pokerDict)
    end = time.clock()
    print("%f秒" % (end - start))
