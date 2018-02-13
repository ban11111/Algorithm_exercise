def flush(list_list):



def getvalue(dictionary):
    for i in dictionary.values():
        return i


def getkey(dictionary):
    for i in dictionary.keys():
        return i


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
