import sorts


def classify(cards_dict):
    sort = sorted(cards_dict.values())


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
    c, h, d, s = [], [], [], []
    for i in l:
        if i[1] == "c":
            c.append(i)
        if i[1] == "h":
            h.append(i)
        if i[1] == "d":
            d.append(i)
        if i[1] == "s":
            s.append(i)
    if len(c) >= 5:
        return c
    if len(h) >= 5:
        return h
    if len(d) >= 5:
        return d
    if len(s) >= 5:
        return s
    return


# 不带花色的列表
def rank_level(l):
    count = 0
    multi2, multi22, multi3, multi4, whole = [], [], [], [], []
    flush = [max(l)]

    if flush[0] == 14:
        l.append(1)
    l.remove(flush[0])

    while len(l) > 0:
        tmp = max(l)
        l.remove(tmp)

        if tmp == flush[-1]:

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
                if count == 2 and not multi2:
                    multi2 = [tmp] * 2
                if count == 2 and multi2 and not multi22:
                    multi22 = [tmp] * 2
                if count == 3 and not multi3:
                    multi3 = [tmp] * 3
                if count == 3 and multi3:
                    multi2 = [tmp] * 2
                if count == 4 and not multi4:
                    multi4 = [tmp] * 4
                    break
                if multi2 and multi3:
                    break
            continue

        if tmp < flush[-1] and count != 0:
            count = 1

        if tmp == flush[-1] - 1 and len(l) > 0:
            flush.append(tmp)
            continue

        if tmp < flush[-1] - 1:
            whole += flush
            if len(l) == 0:
                whole.append(tmp)
            flush = [tmp]
            continue
        whole += flush + [tmp]
        print("======WHOLE!!!!!!!", whole)

    if multi4:
        whole.remove(multi4[0])
        return 8, multi4 + whole[0]

    if multi3 and multi2:
        return 7, multi3 + multi2

    if len(flush) == 5:
        return 5, flush

    if multi3 and not multi2:
        whole.remove(multi3[0])
        return 4, multi3 + whole[:2]

    if multi2 and multi22:
        whole.remove(multi2[0])
        whole.remove(multi22[0])
        return 3, multi2 + multi22 + whole[:1]

    if multi2 and not multi22:
        whole.remove(multi2[0])
        return 2, multi2 + whole[:3]

    if not multi2:
        print(whole)
        return 1, whole[:5]


def rank_value(l):
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
