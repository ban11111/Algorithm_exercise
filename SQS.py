import datetime
import time

day = datetime.timedelta(days=1)


def GetSQSValue0(calculateyear):
    answer = 0
    startdate = datetime.datetime(calculateyear, 1, 1, 0, 0, 0)
    while startdate.year == calculateyear:
        daymonthlist = [int(startdate.month % 10), int(startdate.month / 10 % 10), int(startdate.day % 10),
                        int(startdate.day / 10 % 10)]
        tmplist = list(set(daymonthlist))
        if len(tmplist) == 4:
            for tmphour in range(0, 24):
                tmphourlist = list(set(tmplist + [int(tmphour % 10), int(tmphour / 10 % 10)]))
                if len(tmphourlist) == 6:
                    for tmpmin in range(0, 60):
                        tmpminlist = list(set(tmphourlist + [int(tmpmin % 10), int(tmpmin / 10 % 10)]))
                        if len(tmpminlist) == 8:
                            for tmpsec in range(0, 60):
                                tmpseclist = list(set(tmpminlist + [int(tmpsec % 10), int(tmpsec / 10 % 10)]))
                                if len(tmpseclist) == 10:
                                    answer += 1
        startdate += day
    print(answer)
    return answer


def GetSQSValue(calculateyear):
    answer = 0
    # todo, split date
    startdate = datetime.datetime(calculateyear, 1, 1, 0, 0, 0)
    while startdate.year == calculateyear:
        daymonthlist = [int(startdate.month % 10), int(startdate.month / 10 % 10), int(startdate.day % 10),
                        int(startdate.day / 10 % 10)]
        tmplist = list(set(daymonthlist))
        if len(tmplist) == 4:
            # todo, 24hours split
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
    return answer


def GetSQSValue1(calculateyear):
    answer = 0
    startdate = datetime.datetime(calculateyear, 1, 1, 0, 0, 0)
    while startdate.year == calculateyear:
        daymonthlist = [int(startdate.month % 10), int(startdate.month / 10 % 10), int(startdate.day % 10),
                        int(startdate.day / 10 % 10)]
        tmpset = set(daymonthlist)
        if len(tmpset) == 4:
            for tmphour1 in range(0, 3):
                tmpset1 = set(tmpset)
                tmpset1.add(tmphour1)
                if len(tmpset1) == 5:
                    i = 4 if tmphour1 == 2 else 10
                    for tmphour2 in range(0, i):
                        tmpset2 = set(tmpset1)
                        tmpset2.add(tmphour2)
                        if len(tmpset2) == 6:
                            for tmpmin1 in range(0, 6):
                                tmpset3 = set(tmpset2)
                                tmpset3.add(tmpmin1)
                                if len(tmpset3) == 7:
                                    for tmpmin2 in range(0, 10):
                                        tmpset4 = set(tmpset3)
                                        tmpset4.add(tmpmin2)
                                        if len(tmpset4) == 8:
                                            for tmpsec1 in range(0, 6):
                                                tmpset5 = set(tmpset4)
                                                tmpset5.add(tmpsec1)
                                                if len(tmpset5) == 9:
                                                    for tmpsec2 in range(0, 10):
                                                        tmpset6 = set(tmpset5)
                                                        tmpset6.add(tmpsec2)
                                                        if len(tmpset6) == 10:
                                                            answer += 1
        startdate += day
    return answer


def GetSQSValue2(calculateyear):
    answer = 0
    startdate = datetime.datetime(calculateyear, 1, 1, 0, 0, 0)
    while startdate.year == calculateyear:
        daymonthlist = [int(startdate.month % 10), int(startdate.month / 10 % 10), int(startdate.day % 10),
                        int(startdate.day / 10 % 10)]
        tmpset = set(daymonthlist)
        if len(tmpset) == 4:
            for tmphour1 in range(0, 3):
                if tmphour1 not in tmpset:
                    tmpset1 = set(tmpset)
                    tmpset1.add(tmphour1)
                    i = 4 if tmphour1 == 2 else 10
                    for tmphour2 in range(0, i):
                        if tmphour2 not in tmpset1:
                            tmpset2 = set(tmpset1)
                            tmpset2.add(tmphour2)
                            for tmpmin1 in range(0, 6):
                                if tmpmin1 not in tmpset2:
                                    tmpset3 = set(tmpset2)
                                    tmpset3.add(tmpmin1)
                                    for tmpmin2 in range(0, 10):
                                        if tmpmin2 not in tmpset3:
                                            tmpset4 = set(tmpset3)
                                            tmpset4.add(tmpmin2)
                                            for tmpsec1 in range(0, 6):
                                                if tmpsec1 not in tmpset4:
                                                    tmpset5 = set(tmpset4)
                                                    tmpset5.add(tmpsec1)
                                                    for tmpsec2 in range(0, 10):
                                                        if tmpsec2 not in tmpset5:
                                                            answer += 1
        startdate += day
    return answer


# 第四种方法, 赢家!!!!!
def GetSQSValue3(calculateyear):
    answer = 0
    for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]:
        monthlist = [int(month / 10 % 10), int(month % 10)]
        if month == 2:
            i = 30 if ((calculateyear % 4 == 0 and calculateyear % 100 != 0) or calculateyear % 400 == 0) else 29
        elif month == 4 or month == 6 or month == 9:
            i = 31
        else:
            i = 32
        for date in range(0, i):
            tmpset3 = set(monthlist + [int(date / 10 % 10), int(date % 10)])
            if len(tmpset3) == 4:
                for tmphour1 in range(0, 3):
                    if tmphour1 not in tmpset3:
                        tmpset4 = set(tmpset3)
                        tmpset4.add(tmphour1)
                        i = 4 if tmphour1 == 2 else 10
                        for tmphour2 in range(0, i):
                            if tmphour2 not in tmpset4:
                                tmpset5 = set(tmpset4)
                                tmpset5.add(tmphour2)
                                for tmpmin1 in range(0, 6):
                                    if tmpmin1 not in tmpset5:
                                        tmpset6 = set(tmpset5)
                                        tmpset6.add(tmpmin1)
                                        for tmpmin2 in range(0, 10):
                                            if tmpmin2 not in tmpset6:
                                                tmpset7 = set(tmpset6)
                                                tmpset7.add(tmpmin2)
                                                for tmpsec1 in range(0, 6):
                                                    if tmpsec1 not in tmpset7:
                                                        tmpset8 = set(tmpset7)
                                                        tmpset8.add(tmpsec1)
                                                        for tmpsec2 in range(0, 10):
                                                            if tmpsec2 not in tmpset8:
                                                                answer += 1
    return answer


def GetSQSValue4(calculateyear):
    answer = 0
    for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]:
        monthlist = [int(month / 10 % 10), int(month % 10)]
        i = 3 if month == 2 else 4
        for date1 in range(0, i):
            if date1 not in monthlist:
                tmpset2 = monthlist + [date1]
                j = 1 if date1 == 0 else 0
                if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12)\
                        and date1 == 3:
                    i = 2
                if (month == 4 or month == 6 or month == 9) and date1 == 3:
                    i = 1
                if month == 2 and date1 == 2:
                    i = 10 if ((calculateyear % 4 == 0 and calculateyear % 100 != 0) or calculateyear % 400 == 0) else 9
                if (month == 2 and date1 < 2) or (month != 2 and date1 < 3):
                    i = 10
                for date2 in range(j, i):
                    if date2 not in tmpset2:
                        tmpset3 = tmpset2 + [date2]
                        for tmphour1 in range(0, 3):
                            if tmphour1 not in tmpset3:
                                tmpset4 = tmpset3 + [tmphour1]
                                i = 4 if tmphour1 == 2 else 10
                                for tmphour2 in range(0, i):
                                    if tmphour2 not in tmpset4:
                                        tmpset5 = tmpset4 + [tmphour2]
                                        for tmpmin1 in range(0, 6):
                                            if tmpmin1 not in tmpset5:
                                                tmpset6 = tmpset5 + [tmpmin1]
                                                for tmpmin2 in range(0, 10):
                                                    if tmpmin2 not in tmpset6:
                                                        tmpset7 = tmpset6 +[tmpmin2]
                                                        for tmpsec1 in range(0, 6):
                                                            if tmpsec1 not in tmpset7:
                                                                tmpset8 = tmpset7 + [tmpsec1]
                                                                for tmpsec2 in range(0, 10):
                                                                    if tmpsec2 not in tmpset8:
                                                                        answer += 1
    return answer


# todo, 查表法


if __name__ == "__main__":
    start = time.clock()
    print("2003年的十全时总共有:", GetSQSValue0(2003), "个")
    end = time.clock()
    print("原始方法：%f秒" % (end - start))

    start = time.clock()
    print("2003年的十全时总共有:", GetSQSValue(2003), "个")
    end = time.clock()
    print("第一种方法：%f秒" % (end - start))

    start = time.clock()
    print("2003年的十全时总共有:", GetSQSValue1(2003), "个")
    end = time.clock()
    print("第二种方法：%f秒" % (end - start))

    start = time.clock()
    print("2003年的十全时总共有:", GetSQSValue2(2003), "个")
    end = time.clock()
    print("第三种方法：%f秒" % (end - start))

    start = time.clock()
    print("2003年的十全时总共有:", GetSQSValue3(2003), "个")
    end = time.clock()
    print("第四种方法：%f秒" % (end - start))

    start = time.clock()
    print("2003年的十全时总共有:", GetSQSValue4(2003), "个")
    end = time.clock()
    print("第五种方法：%f秒" % (end - start))
