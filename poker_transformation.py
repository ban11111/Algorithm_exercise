import json
import poker_dict as pd

pokerDicts = pd.PokerDicts()
pokerDict = pokerDicts.pokerDict
numDict = pokerDicts.numDict

my_path = "./results/"
path = "./json_files/"


# 读取json文件
def file2json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# 结果写入文件
def json2file(content, file_path):
    with open(file_path, "w") as file:
        file.write(json.dumps(content, sort_keys=True))
        # json.dump(content, file)


# 字符串 转 str_list
def str2list(string):
    str_list = []
    for i in range(0, len(string)):
        if (i + 1) % 2 == 0:
            str_list.append(string[i - 1: i + 1])
    return str_list


# 字符串 转 list_list
def str2list_list(string):
    list_list = []
    for i in str2list(string):
        list_list.append([numDict[i[0]], i[1]])
    return list_list


# list_list 转 数字list
def list_list2num_list(list_list):
    num_list = []
    for i in list_list:
        num_list.append(i[0])
    return num_list


# 测试一下
if __name__ == "__main__":
    data = file2json(path + "seven_cards.json")
    firstMatch = data["matches"][0]
    print(firstMatch)
    li_li = str2list_list(firstMatch["alice"])
    print(li_li)
    li = list_list2num_list(li_li)
    print(li)


# **************  下面的方法暂不需要  ****************
def list2dict(poker_list, poker_dict):
    result = {}
    for value in poker_list:
        result[value] = poker_dict[value]
    return result


def list2dict_list(poker_list, poker_dict):
    dict_list = []
    result = {}
    for value in poker_list:
        result[value[1:]] = poker_dict[value]
        dict_list.append(result)
        result = {}
    return dict_list


def list2list_list(poker_list, poker_dict):
    list_list = []
    result = []
    for key in poker_list:
        result.append(poker_dict[key])
        result.append(key[1:])
        list_list.append(result)
        result = []
    return list_list
