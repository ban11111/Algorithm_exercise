import random


def flush(list_list):
    pass


def getvalue(dictionary):
    for i in dictionary.values():
        return i


def getkey(dictionary):
    for i in dictionary.keys():
        return i


# for dict_list
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    value = getvalue(lists[left])
    low = left
    high = right
    while left < right:
        while left < right and getvalue(lists[right]) >= value:
            right -= 1
        lists[left][getkey(lists[left])] = getvalue(lists[right])
        while left < right and getvalue(lists[left]) <= value:
            left += 1
        lists[right][getkey(lists[right])] = getvalue(lists[left])
    lists[right][getkey(lists[right])] = value
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


# for list_list
def quick_sort2(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    value = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right][0] >= value[0]:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left][0] <= value[0]:
            left += 1
        lists[right] = lists[left]
    lists[right] = value
    quick_sort2(lists, low, left - 1)
    quick_sort2(lists, left + 1, high)
    return lists


# 快速去重排序
def qsort(l):
    if len(l) < 2:
        return l
    pivot_element = random.choice(l)
    large = [i for i in l if i > pivot_element]
    # medium = [i for i in L if i==pivot_element]
    small = [i for i in l if i < pivot_element]
    return qsort(large) + [pivot_element] + qsort(small)


def bubsort(l):
    if max(l)[0] == 14:
        m = [[1, max(l)[1]]]
        print(m, l)
    else:
        m = [min(l)]
        l.remove(m[0])
    while len(l) + len(m) >= 5 and len(l) != 0:
        tm = min(l)
        if tm[0] == m[-1][0]:
            l.remove(tm)
            continue
        if tm[0] == m[-1][0] + 1:
            l.remove(tm)
            m.append(tm)
            continue
        if tm[0] > m[-1][0] + 1 and len(l) >= 5:
            m = [tm]
            l.remove(tm)
            continue
        break
    if len(m) >= 5:
        return m
    else:
        return []


def select_sort(lists):
    # 选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)


def build_heap(lists, size):
    for i in range(0, (size / 2))[::-1]:
        adjust_heap(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


if __name__ == "__main__":
    print(qsort([5, 2, 1, 0, 67, 2, 43, 2, 87]))
