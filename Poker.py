# coding: utf-8

import time, logging, os
import poker_transformation as pt
import poker_comparison as cmp
import verification as vf


def poker(file_in, file_out):
    start = time.clock()   # 开始时间

    data = pt.file2json(pt.path + file_in)
    match = data["matches"]
    flag = 1

    for i in match:
        try:
            result = cmp.compare(i)
        except Exception as e:
            pass
            logging.error("第%s行出错, err: %s" % (flag, e))
        else:
            i["result"] = result
        flag += 1
    pt.json2file(data, pt.my_path + file_out)

    end = time.clock()     # 结束时间
    print("%f秒" % (end - start))


if __name__ == "__main__":
    os.remove("./err.log")
    logging.basicConfig(filename='err.log', level=logging.DEBUG)
    # 7张牌 无赖子
    poker("seven_cards.json", "seven_cards.my.json")
    vf.check_result(pt.path + "seven_cards.result.json", pt.my_path + "seven_cards.my.json")
    # 5张牌 无赖子
    poker("match.json", "five_cards.my.json")
    vf.check_result(pt.path + "result.json", pt.my_path + "five_cards.my.json")
    # 7张牌 有赖子
    poker("seven_cards_with_ghost.json", "seven_ghost.my.json")
    vf.check_result(pt.path + "seven_cards_with_ghost.result.json", pt.my_path + "seven_ghost.my.json")
    # 5张牌 有赖子 todo
