import poker_transformation as pt


# 分类
def rank_classify(list_list):
    c = rank_color(list_list)
    if c:
        crank = rank_color_flush(c)
        if crank[0] == 9:
            return crank
        else:
            rank = rank_level(pt.list_list2num_list(list_list))
            if rank[0] > crank[0]:
                return rank
            else:
                return crank
    else:
        return rank_level(pt.list_list2num_list(list_list))


# 同花的列表
def rank_color_flush(l):
    original = l.copy()
    flush = [max(l)]
    if flush[0][0] == 14:
        l.append([1, flush[0][1]])
    l.remove(flush[0])
    while len(flush) < 5:
        tmp = max(l)
        l.remove(tmp)
        if tmp[0] == flush[-1][0]:
            continue
        if tmp[0] == flush[-1][0] - 1:
            flush.append(tmp)
            continue
        if tmp[0] < flush[-1][0] - 1 and len(l) >= 4:
            flush = [tmp]
            continue
        return 6, sorted(original, reverse=True)[:5]
    return 9, flush


# 带花色的列表
def rank_color(l):
    c, h, d, s, n = [], [], [], [], []
    for i in l:
        if i[1] == "c":
            c.append(i)
        if i[1] == "h":
            h.append(i)
        if i[1] == "d":
            d.append(i)
        if i[1] == "s":
            s.append(i)
        if i[1] == "n":
            n.append(i)
    if len(c) >= 5:
        return pt.list_list2num_list(c + n)
    if len(h) >= 5:
        return pt.list_list2num_list(h + n)
    if len(d) >= 5:
        return pt.list_list2num_list(d + n)
    if len(s) >= 5:
        return pt.list_list2num_list(s + n)
    return


# 不带花色的列表
# 返回 等级 和 列表
def rank_level(l):
    # original = l.copy()
    # count 用于标示以及计算重复牌数量, 0 表示第一次遇到重复牌, 1 表示之后遇到重复牌, 2 及以上表示重复牌的数量
    count = 0
    multi2, multi22, multi3, multi4, whole = [], [], [], [], []            # multi 用于存储重复牌, whole 用于存储去重后所有牌
    flush, whole = [max(l)], [max(l)]

    if flush[0] == 14:
        l.append(1)
    l.remove(flush[0])

    while len(l) > 0:
        tmp = max(l)
        l.remove(tmp)

        if tmp == whole[-1]:

            if count == 0:
                count = l.count(tmp) + 2
                if count == 2:
                    multi2 = [tmp] * 2
                if count == 3:
                    multi3 = [tmp] * 3
                if count == 4:
                    multi4 = [tmp] * 4
                    break

            if count == 1:
                count = l.count(tmp) + 2
                if count == 4 and not multi4:
                    multi4 = [tmp] * 4
                    break
                if count == 3 and not multi3:
                    multi3 = [tmp] * 3
                if count == 3 and multi3 and not multi2:
                    multi2 = [tmp] * 2
                if count == 2 and not multi2:
                    multi2 = [tmp] * 2
                if count == 2 and multi2 and not multi22:
                    multi22 = [tmp] * 2
                if multi3 and multi2:
                    break
            continue

        if tmp < whole[-1] and count > 1:
            count = 1

        if tmp == flush[-1] - 1:
            whole += [tmp]
            flush.append(tmp)
            continue

        # whole变量用于保存 "排序 并 去重" 后的列表
        if tmp < flush[-1] - 1:
            whole += [tmp]
            flush = [tmp] if len(l) >= 4 else flush

    # print("======WHOLE!!!!!!!", whole)
    # print("======flush=======", flush)
    if multi4:
        x = set(whole + l)
        x.remove(multi4[0])
        return 8, multi4 + sorted(x, reverse=True)[:1]

    if multi3 and multi2:
        return 7, multi3 + multi2

    if len(flush) >= 5:
        return 5, flush[:5]

    if multi3:
        whole.remove(multi3[0])
        return 4, multi3 + whole[:2]

    if multi2 and multi22:
        whole.remove(multi2[0])
        whole.remove(multi22[0])
        return 3, multi2 + multi22 + whole[:1]

    if multi2:
        # print("rank2", whole)
        whole.remove(multi2[0])
        return 2, multi2 + whole[:3]

    if not multi2:
        return 1, whole[:5]


# 计算权重分值
def rank_value(l):
    # print("===list===   ", l)
    if len(l) != 5:
        raise Exception("只能接收5张作为最终牌型!")
    value = 0
    if type(l[0]) == int:
        for i in range(0, 5):
            value += l[i] * 16 ** (4 - i)
    else:
        for i in range(0, 5):
            value += l[i][0] * 16 ** (4 - i)
    return value
