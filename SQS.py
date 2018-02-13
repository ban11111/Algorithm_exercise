import datetime
import time

day = datetime.timedelta(days=1)


def GetSQSValue(calculateyear):
    answer = 0
    startdate = datetime.datetime(calculateyear, 1, 1, 0, 0, 0)
    while startdate.year == calculateyear:
        daymonthlist = [int(startdate.month % 10), int(startdate.month / 10 % 10), int(startdate.day % 10),
                        int(startdate.day / 10 % 10)]
        tmplist = list(set(daymonthlist))
        if len(tmplist) == 4:
            #todo, 24hours split
            for tmphour1 in range(0, 3):
                tmphour1list = list(set(tmplist + [tmphour1]))
                if len(tmphour1list) == 5:
                    i = 4 if tmphour1 == 2 else 10
                    for tmphour2 in range(0, i):
                        tmphour2list = list(set(tmphour1list + [tmphour2]))
                        if len(tmphour2list) == 6:
                            for tmpmin1 in range(0, 6):
                                tmpmin1list = list(set(tmphour2list + [tmpmin1]))
                                if len(tmpmin1list) == 7:
                                    for tmpmin2 in range(0, 10):
                                        tmpmin2list = list(set(tmpmin1list + [tmpmin2]))
                                        if len(tmpmin2list) == 8:
                                            for tmpsec1 in range(0, 6):
                                                tmpsec1list = list(set(tmpmin2list + [tmpsec1]))
                                                if len(tmpsec1list) == 9:
                                                    for tmpsec2 in range(0, 10):
                                                        tmpsec2list = list(set(tmpsec1list + [tmpsec2]))
                                                        if len(tmpsec2list) == 10:
                                                            answer += 1
        startdate += day
    print(answer)
    return answer


if __name__ == "__main__":
    start = time.clock()
    print("2003年的十全时总共有:", GetSQSValue(2003), "个")
    end = time.clock()
    print("%f秒" % (end - start))
