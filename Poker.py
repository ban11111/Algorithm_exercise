# coding: utf-8

import time
import poker_transformation as pt
import poker_comparison as cmp


if __name__ == "__main__":
    # 7张牌 无赖子
    start = time.clock()

    data = pt.file2json("./jsonfiles/seven_cards.json")
    match = data["matches"]
    flag = 1

    for i in match:
        try:
            result = cmp.compare(i)
        except Exception as e:
            print("第%s行出错, err: %s" % (flag, e))
        else:
            i["result"] = result
        flag += 1
    pt.json2file(data, "seven_cards.my.json")

    end = time.clock()
    print("%f秒" % (end - start))

    # 5张牌 无赖子
    start = time.clock()

    data = pt.file2json("./jsonfiles/match.json")
    match = data["matches"]
    flag = 1

    for i in match:
        try:
            result = cmp.compare(i)
        except Exception as e:
            print("第%s行出错, err: %s" % (flag, e))
        else:
            i["result"] = result
        flag += 1
    pt.json2file(data, "five_cards.my.json")

    end = time.clock()
    print("%f秒" % (end - start))
