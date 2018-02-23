import poker_transformation as pt


def check_result(file1, file2):
    fail = False
    results1 = pt.file2json(file1)
    results2 = pt.file2json(file2)

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
    return not fail


if __name__ == "__main__":
    # 7 cards
    check_result("./jsonfiles/seven_cards.result.json", "./results/seven_cards.my.json")

    # 5 cards
    check_result("./jsonfiles/result.json", "./results/five_cards.my.json")
