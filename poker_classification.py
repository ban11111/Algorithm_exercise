import poker_transformation as pt


# 常量
StraightFlush, FourOfAKind, FullHouse, Flush, Straight, ThreeOfAKind, TwoPairs, OnePair, NoHand = \
    (9, 8, 7, 6, 5, 4, 3, 2, 1)
Ghost = -1  # -1 代表 赖子


# 分类
def rank_classify(list_list):
    # 首先判断是否同花
    c = rank_flush(list_list)
    if len(c) >= 5:  # 如果是同花
        if -1 not in c:  # 没有赖子
            crank = rank_straight_flush(c)
            if crank[0] == 9:
                return crank
            else:
                rank = rank_level(pt.list_list2num_list(list_list))
                if rank[0] > crank[0]:
                    return rank
                else:
                    return crank

        elif -1 in c:  # 如果有赖子
            crank = rank_straight_flush_with_ghost(c)
            if crank[0] == 9:
                return crank
            else:
                rank = rank_level_with_ghost(pt.list_list2num_list(list_list))
                if rank[0] > crank[0]:
                    return rank
                else:
                    return crank
    else:  # 如果不是同花
        if c[0] == 0:
            return rank_level(pt.list_list2num_list(list_list))
        else:  # 如果有赖子
            return rank_level_with_ghost(pt.list_list2num_list(list_list))


# 传入带花色的列表， 判断是否同花，并返回不带花色的列表。
def rank_flush(l):
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
    if len(c) + len(n) >= 5:
        return pt.list_list2num_list(c + n)
    if len(h) + len(n) >= 5:
        return pt.list_list2num_list(h + n)
    if len(d) + len(n) >= 5:
        return pt.list_list2num_list(d + n)
    if len(s) + len(n) >= 5:
        return pt.list_list2num_list(s + n)
    if n:
        return [1]
    return [0]


# 传入同花的列表， 判断是否是同花顺
def rank_straight_flush(l):
    original = l.copy()
    straight = [max(l)]
    if straight[0] == 14:
        l.append(1)
    l.remove(straight[0])
    while len(straight) < 5:
        tmp = max(l)
        l.remove(tmp)
        if tmp == straight[-1]:
            continue
        if tmp == straight[-1] - 1:
            straight.append(tmp)
            continue
        if tmp < straight[-1] - 1 and len(l) >= 4:
            straight = [tmp]
            continue
        return Flush, sorted(original, reverse=True)[:5]
    return StraightFlush, straight


# 同花列表, 带赖子, 值-1 代表赖子 todo, 同花中,赖子是否可以变成 "已有的牌" 中相同的一张牌? 目前做法是不能.
def rank_straight_flush_with_ghost(l):
    # 分别记录赖子在顺子里的值 以及 最大的可能值
    straight_index, max_index = 14, 14

    original = l.copy()
    straight = [max(l)]
    if straight[0] == 14:
        l.append(1)
        straight_index, max_index = 13, 13
    else:
        straight[0] = Ghost
    l.remove(straight[0])

    tmp = max(l)
    if straight_index > tmp:
        straight_index = tmp + 1
    if straight_index == tmp:
        straight_index -= 1

    while len(l) > 0:
        tmp = max(l)
        l.remove(tmp)

        # 根据straight最后一位 是否是 赖子, 来分别判断.
        if straight[-1] != Ghost:
            if tmp == straight[-1]:
                continue

            if tmp == straight[-1] - 1:
                straight.append(tmp)
                max_index -= 1 if straight[0] == 14 else 0
                continue
            # 如果tmp 与 straight 相隔 一位
            if tmp == straight[-1] - 2:
                if len(l) > 0 and l[-1] == Ghost:  # 如果赖子还未使用
                    l.pop()
                straight_index = tmp + 1
                straight = straight[straight.index(Ghost) + 1:] + [Ghost, tmp] if Ghost in straight else \
                    straight + [Ghost, tmp]
                continue
            # 如果tmp 与 straight 相隔 超过一位
            if tmp < straight[-1] - 2:
                if len(l) > 0 and l[-1] == Ghost:  # 如果赖子还未使用
                    l.pop()
                if len(straight) < 5:                 # 如果遍历到的顺子不到5, 则重新计算顺子
                    straight_index = tmp + 1
                    straight = [Ghost, tmp]
                    continue
                break

        if straight[-1] == Ghost:
            # 如果tmp 与 赖子的值 相等, 赖子值-1
            if tmp == straight_index:
                straight_index -= 1
                straight.insert(-1, tmp)
                continue

            if tmp == straight_index - 1:
                straight.append(tmp)
                max_index -= 1 if straight[0] == 14 else 0
                continue

            # 如果tmp 与 赖子的值 相隔 一位
            if tmp == straight_index - 2:
                straight_index = tmp + 1
                straight = straight[straight.index(Ghost) + 1:] + [Ghost, tmp]
                continue

            # 如果tmp 与 赖子的值 相隔 超过一位
            if tmp < straight_index - 2:
                l.pop()
                if len(straight) < 5:                 # 如果遍历到的顺子不到5, 则重新计算顺子
                    straight_index = tmp + 1
                    straight = [Ghost, tmp]
                    continue
                break

    if len(straight) < 5:
        original.append(max_index)
        return Flush, sorted(original, reverse=True)[:5]
    straight[straight.index(Ghost)] = straight_index
    return StraightFlush, straight[:5]


# 不带花色的列表
# 返回 等级 和 列表
def rank_level(l):
    # original = l.copy()
    # count 用于标示以及计算重复牌数量, 0 表示第一次遇到重复牌, 1 表示之后遇到重复牌, 2 及以上表示重复牌的数量
    count = 0
    multi2, multi22, multi3, multi4, whole = [], [], [], [], []            # multi 用于存储重复牌, whole 用于存储去重后所有牌
    straight, whole = [max(l)], [max(l)]

    if straight[0] == 14:
        l.append(1)
    l.remove(straight[0])

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

        if tmp == straight[-1] - 1:
            whole += [tmp]
            straight.append(tmp)
            continue

        # whole变量用于保存 "排序 并 去重" 后的列表
        if tmp < straight[-1] - 1:
            whole += [tmp]
            straight = [tmp] if len(straight) < 5 else straight

    # print("======WHOLE!!!!!!!", whole)
    # print("======straight=======", straight)
    if multi4:
        x = set(whole + l)
        x.remove(multi4[0])
        return FourOfAKind, multi4 + sorted(x, reverse=True)[:1]

    if multi3 and multi2:
        return FullHouse, multi3 + multi2

    if len(straight) >= 5:
        return Straight, straight[:5]

    if multi3:
        whole.remove(multi3[0])
        return ThreeOfAKind, multi3 + whole[:2]

    if multi2 and multi22:
        whole.remove(multi2[0])
        whole.remove(multi22[0])
        return TwoPairs, multi2 + multi22 + whole[:1]

    if multi2:
        # print("rank2", whole)
        whole.remove(multi2[0])
        return OnePair, multi2 + whole[:3]

    if not multi2:
        return NoHand, whole[:5]


# 带赖子, 判断牌型
def rank_level_with_ghost(l):
    l.remove(Ghost)
    l.append(Ghost)
    # 记录赖子在顺子里的值
    straight_index = 14

    # count 用于标示以及计算重复牌数量, 0 表示第一次遇到重复牌, 1 表示之后遇到重复牌, 2 及以上表示重复牌的数量
    count = 0
    multi2, multi22, multi3, multi4, whole = [], [], [], [], []  # multi 用于存储重复牌, whole 用于存储去重后所有牌
    straight, whole = [max(l)], [max(l)]

    if straight[0] == 14:
        l.insert(-1, 1)
        straight_index = 13
    else:
        straight[0], whole[0] = Ghost, Ghost
    l.remove(straight[0])

    tmp = max(l)
    if straight_index > tmp:
        straight_index = tmp + 1
    if straight_index == tmp:
        straight_index -= 1

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

        if straight[-1] != Ghost:
            if tmp == straight[-1] - 1:
                whole += [tmp]
                straight.append(tmp)
                continue

            # 如果tmp 与 straight 相隔 一位
            if tmp == straight[-1] - 2:
                whole += [tmp]
                if len(l) > 0 and l[-1] == Ghost:  # 如果赖子还未使用
                    l.pop()
                if len(straight) < 5:
                    straight_index = tmp + 1
                    straight = straight[straight.index(Ghost) + 1:] + [Ghost, tmp] if Ghost in straight else \
                        straight + [Ghost, tmp]
                continue

            # 如果tmp 与 straight 相隔 超过一位
            if tmp < straight[-1] - 2:
                whole += [tmp]
                if len(l) > 0 and l[-1] == Ghost:  # 如果赖子还未使用
                    l.pop()
                if len(straight) == 4 and Ghost not in straight:  # 如果遍历到的顺子长度为4, 并且赖子未使用，则直接将赖子放到第5位
                    straight_index = straight[3] - 1
                    straight.append(Ghost)
                    continue
                if len(straight) < 5:                 # 如果遍历到的顺子不到5, 则重新计算顺子
                    straight_index = tmp + 1
                    straight = [Ghost, tmp]
                    continue

        elif straight[-1] == Ghost:
            if tmp == straight_index - 1:
                whole += [tmp]
                straight.append(tmp)
                continue

            # 如果tmp 与 straight 相隔 一位
            if tmp == straight_index - 2:
                whole += [tmp]
                if len(straight) < 5:
                    straight_index = tmp + 1
                    straight = straight[straight.index(Ghost) + 1:] + [Ghost, tmp]
                continue

            # 如果tmp 与 straight 相隔 超过一位
            if tmp < straight_index - 2:
                whole += [tmp]
                if len(straight) < 5:                 # 如果遍历到的顺子不到5, 则重新计算顺子
                    straight_index = tmp + 1
                    straight = [Ghost, tmp]
                continue

            # if tmp < straight_index - 1:
            #     whole += [tmp]
            #     straight = [tmp] if len(l) >= 4 else straight

    # print("======WHOLE!!!!!!!", whole)
    # print("======straight=======", straight)
    if Ghost in whole:
        whole.remove(Ghost)
    if multi4:
        return FourOfAKind, multi4 + [13] if multi4[0] == 14 else [14]

    if multi3 and multi2:
        x = set(whole + l)
        x.remove(multi3[0])
        return FourOfAKind, multi3 + [multi3[0], max(x)]

    if multi3:
        whole.remove(multi3[0])
        return FourOfAKind, multi3 + [multi3[0]] + whole[:1]

    if multi2 and multi22:  # multi2 肯定比 multi22 大， 因此不需要在这里进行比较
        whole.remove(multi2[0])
        whole.remove(multi22[0])
        return FullHouse, multi2 + [multi2[0]] + multi22

    if len(straight) >= 5:
        if Ghost in straight:
            straight[straight.index(Ghost)] = straight_index
        return Straight, straight[:5]

    if multi2:
        whole.remove(multi2[0])
        return ThreeOfAKind, multi2 + [multi2[0]] + whole[:2]

    if not multi2:
        whole.insert(0, whole[0])
        return OnePair, whole[:5]


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
