# coding: utf-8

import time, logging, os, sorts
import poker_transformation as pt
import poker_comparison as cmp
import verification as vf


def poker(file_in, file_out):
    start = time.clock()  # 开始时间

    data = pt.file2json(pt.path + file_in)
    match = data["matches"]
    flag = 1

    for i in match:
        try:
            result = cmp.compare(i)
        except Exception as e:
            logging.error("第%s行出错, err: %s" % (flag, e))
        else:
            i["result"] = result
        flag += 1
    # pt.json2file(data, pt.my_path + file_out)

    end = time.clock()  # 结束时间
    print("%f秒" % (end - start))
    pt.json2file(data, pt.my_path + file_out)


# 第二个方法
def poker_quick(file_in, file_out):
    start = time.clock()  # 开始时间

    data = pt.file2json(pt.path + file_in)
    match = data["matches"]
    flag = 1

    for i in match:
        try:
            result = cmp.compare_quick(i)
        except Exception as e:
            logging.error("第%s行出错, err: %s" % (flag, e))
        else:
            i["result"] = result
        flag += 1

    end = time.clock()  # 结束时间

    print("%f秒" % (end - start))
    pt.json2file(data, pt.my_path + file_out)


if __name__ == "__main__":
    # sorts.time_for_sorting()
    os.remove("./err.log")
    logging.basicConfig(filename='err.log', level=logging.DEBUG)

    print("\n\n*********************************")
    print("7张牌 无赖子")
    poker("seven_cards.json", "seven_cards.my.json")
    vf.check_result(pt.path + "seven_cards.result.json", pt.my_path + "seven_cards.my.json")

    print("5张牌 无赖子")
    poker("match.json", "five_cards.my.json")
    vf.check_result(pt.path + "result.json", pt.my_path + "five_cards.my.json")

    print("7张牌 有赖子")
    poker("seven_cards_with_ghost.json", "seven_ghost.my.json")
    vf.check_result(pt.path + "seven_cards_with_ghost.result.json", pt.my_path + "seven_ghost.my.json")

    print("5张牌 有赖子")
    poker("five_cards_with_ghost.json", "five_ghost.my.json")

    print("\n\n*********************************")
    print("quick-classify, 7张牌 无赖子")
    poker_quick("seven_cards.json", "seven_cards.q.json")
    vf.check_result(pt.path + "seven_cards.result.json", pt.my_path + "seven_cards.q.json")

    print("quick-classify, 5张牌 无赖子")
    poker_quick("match.json", "five_cards.q.json")
    vf.check_result(pt.path + "result.json", pt.my_path + "five_cards.q.json")

    print("quick-classify, 7张牌 有赖子")
    poker_quick("seven_cards_with_ghost.json", "seven_ghost.q.json")
    vf.check_result(pt.path + "seven_cards_with_ghost.result.json", pt.my_path + "seven_ghost.q.json")

    print("quick-classify, 5张牌 有赖子")
    poker_quick("five_cards_with_ghost.json", "five_ghost.q.json")
