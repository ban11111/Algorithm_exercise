import poker_classification as pc
import poker_transformation as pt

# 常量
StraightFlush, FourOfAKind, FullHouse, Flush, Straight, ThreeOfAKind, TwoPairs, OnePair, NoHand = \
    (9, 8, 7, 6, 5, 4, 3, 2, 1)
Ghost = -1  # -1 代表 赖子


def quick_classify(list_list):
    # 首先判断是否同花
    c = pc.rank_flush(list_list)
    if len(c) >= 5:  # 如果是同花
        crank = quick_straight_flush(c)
        if crank[0] == 9:
            return crank
        else:
            rank = quick_level(pt.list_list2num_list(list_list))
            if rank[0] > crank[0]:
                return rank
            else:
                return crank

    else:  # 如果不是同花
        if c[0] == 0:
            return quick_level(pt.list_list2num_list(list_list))
        else:  # 如果有赖子
            return quick_level_with_ghost(pt.list_list2num_list(list_list))


def quick_straight_flush(l):
    l.sort(reverse=True)
    if l[-1] != Ghost:
        if l[0] == 14:
            l.append(1)
        for i in range(0, len(l) - 4):
            if l[i] - l[i + 4] == 4:
                return StraightFlush, l[i: i + 5]
        return Flush, l[:5]

    else:
        l.pop()
        if l[0] == 14:
            l.append(1)
        for i in range(0, len(l) - 3):
            if l[i] - l[i + 3] == 4:
                return StraightFlush, l[i: i + 4]
            if l[i] - l[i + 3] == 3:
                return StraightFlush, [14] + l[i: i + 4] if l[i] == 13 else l[i: i + 4] + [l[i] - 1]
        return Flush, l[:5]


def quick_level(l):
    straight, multi2, multi22, multi3, multi4 = [], [], [], [], []
    ls = sorted(set(l), reverse=True)
    if ls[0] == 14:
        ls.append(1)

    for i in range(0, len(ls) - 4):
        if ls[i] - ls[i + 4] == 4:
            straight = ls[i: i + 5]
            break

    for i in ls:
        count = l.count(i)
        if count == 4:
            multi4 = i
            break
        if count == 3 and not multi3:
            multi3 = i
            continue
        if count == 3 and multi3:
            multi2 = i
            continue
        if count == 2 and not multi2:
            multi2 = i
            continue
        if count == 2 and multi2 and not multi22:
            multi22 = i

    if multi4:
        ls.remove(multi4)
        return FourOfAKind, [multi4] * 4 + ls[:1]

    if multi3 and multi2:
        ls.remove(multi3)
        ls.remove(multi2)
        return FullHouse, [multi3] * 3 + [multi2] * 2

    if straight:
        return Straight, straight

    if multi3:
        ls.remove(multi3)
        return ThreeOfAKind, [multi3] * 3 + ls[:2]

    if multi2 and multi22:
        ls.remove(multi2)
        ls.remove(multi22)
        return TwoPairs, [multi2] * 2 + [multi22] * 2 + ls[:1]

    if multi2:
        ls.remove(multi2)
        return OnePair, [multi2] * 2 + ls[:3]
    else:
        return NoHand, ls[:5]


def quick_level_with_ghost(l):
    straight, multi2, multi22, multi3, multi4 = [], [], [], [], []
    ls = sorted(set(l), reverse=True)
    ls.pop()
    l.remove(Ghost)
    if ls[0] == 14:
        ls.append(1)

    for i in range(0, len(ls) - 3):
        if ls[i] - ls[i + 3] == 4:
            straight = ls[i: i + 4]
            break
        if ls[i] - ls[i + 3] == 3:
            straight = [14] + ls[i: i + 4] if ls[i] == 13 else ls[i: i + 4] + [ls[i] - 1]
            break

    for i in ls:
        count = l.count(i)
        if count == 4:
            multi4 = i
            break
        if count == 3 and not multi3:
            multi3 = i
            continue
        if count == 3 and multi3:
            multi2 = i
            continue
        if count == 2 and not multi2:
            multi2 = i
            continue
        if count == 2 and multi2 and not multi22:
            multi22 = i

    if multi4:
        ls.remove(multi4)
        return FourOfAKind, [multi4] * 4 + [13] if multi4 == 14 else [multi4] * 4 + [14]

    # if multi3 and multi2:
    #     ls.remove(multi3)
    #     return FourOfAKind, [multi3] * 4 + ls[:1]

    if multi3:
        ls.remove(multi3)
        return FourOfAKind, [multi3] * 4 + ls[:1]

    if multi2 and multi22:
        ls.remove(multi2)
        ls.remove(multi22)
        return FullHouse, [multi2] * 3 + [multi22] * 2

    if straight:
        return Straight, straight

    if multi2:
        ls.remove(multi2)
        return ThreeOfAKind, [multi2] * 3 + ls[:2]
    else:
        ls.insert(0, ls[0])
        return OnePair, ls[:5]
