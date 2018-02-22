import poker_transformation as PT
import poker_classification as PC


if __name__ == "__main__":
    s = None
    list_list = [[4, "d"], [2, "c"], [8, "d"], [5, "h"], [5, "s"], [7, "s"], [8, "s"], [9, "s"], [9, "d"]]
    maxnum = max(list_list)

    c = PC.rank_color(list_list)
    if c:
        s = PC.rank_color_flush(c)
        print(s)
        v = PC.rank_value(s[1])
        print(v)
    else:
        x = PC.rank_level(PT.list_list2num_list(list_list))
        print(x)
        v = PC.rank_value(x[1])
        print(v)
