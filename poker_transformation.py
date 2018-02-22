import json
import poker_dict as PD

pokerDicts = PD.PokerDicts()
pokerDict = pokerDicts.pokerDict
numDict = pokerDicts.numDict


def file2json(path):
    with open(path, "r") as file:
        return json.load(file)


def str2list(string):
    str_list = []
    for i in range(0, len(string)):
        if (i + 1) % 2 == 0:
            str_list.append(string[i - 1: i + 1])
    return str_list


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


def list_list2num_list(list_list):
    num_list = []
    for i in list_list:
        num_list.append(i[0])
    return num_list


if __name__ == "__main__":
    data = file2json("./jsonfiles/seven_cards.json")
    firstMatch = data["matches"][0]
    print(firstMatch)
    a = firstMatch["alice"]
    alice = str2list(a)
    print(alice)
    alice_dict = list2dict(alice, pokerDict)
    print(alice_dict)

    x = sorted(alice_dict.values())
    print(x)

    y = list2dict_list(alice, pokerDict)
    print(y)

    z = list2list_list(alice, pokerDict)
    print(z)
