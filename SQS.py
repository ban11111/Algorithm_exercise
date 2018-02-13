import datetime

day = datetime.timedelta(days=1)


def GetSQSValue(calculateyear):
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


print("2003年的十全时总共有:", GetSQSValue(2003), "个")
