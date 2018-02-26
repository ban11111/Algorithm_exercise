import poker_classification as pc

# TODO, 增加单元测试


if __name__ == "__main__":
    s = None
    list_list = [[4, "d"], [2, "c"], [8, "d"], [5, "h"], [5, "d"], [7, "s"], [8, "s"], [9, "d"], [14, "d"]]
    maxnum = max(list_list)

    c = pc.rank_classify(list_list)
    print(c)
