import poker_transformation as pt


# 检测答案是否正确
def check_result(jsonfile, myfile):
    fail = False
    results1 = pt.file2json(jsonfile)
    results2 = pt.file2json(myfile)

    answer1 = results1["matches"]
    answer2 = results2["matches"]

    for i in range(0, len(answer1)):
        if answer1[i]["result"] != answer2[i]["result"]:
            fail = True
            print("第%d个不对" % (i + 1))

    if fail:
        print("你完了, 你答案错了!!!")
    else:
        print("恭喜恭喜,答案全对!!!")
    # return not fail


if __name__ == "__main__":
    # 7 cards
    check_result("./json_files/seven_cards.result.json", "./results/seven_cards.my.json")

    # 5 cards
    check_result("./json_files/result.json", "./results/five_cards.my.json")
