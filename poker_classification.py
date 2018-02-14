import sorts


def classify(cards_dict):
    sort = sorted(cards_dict.values())


def class_flush(list_list):
    length = len(list_list)
    maxnum = max(list_list)
    minnum = min(list_list)
    result = maxnum[0] - minnum[0]
    if length < 5:
        # raise Exception("牌组长度必须大于等于5，只接收到%d张牌" % length)
        return 0, maxnum, minnum
    elif length == 5:
        if result == 4:
            return 1, maxnum, minnum
        elif result > 4:
            return -1, maxnum, minnum
        else:
            return 0, maxnum, minnum
    elif length > 5:
        if result == 4:
            return True, maxnum, minnum
        elif result < 4:
            return False, maxnum, minnum
        else:
            list_list.remove(maxnum)
            high, _, _ = class_flush(list_list)
            if high == 0:
                return 0, maxnum, minnum
            elif high == 1:
                return 1, maxnum, minnum
            else:
                print(list_list)
                print(maxnum)
                list_list.append(maxnum)
                list_list.remove(minnum)
                low, _, _ = class_flush(list_list)
                if low == 0:
                    return 0, maxnum, minnum
                elif low == 1:
                    return 1, maxnum, minnum
                else:
                    print(list_list)
                    print(minnum)
                    new, _, _ = class_flush(list_list)
                    if new == 0:
                        return 0, maxnum, minnum
                    elif new == 1:
                        return 1, maxnum, minnum
                    else:
                        list_list.remove(maxnum)
                        print("new", list_list)
                        class_flush(list_list)

