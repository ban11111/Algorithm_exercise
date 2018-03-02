class PokerDicts:
    numDict = {}
    pokerDict = {}
    # all_list_list = list()

    def __init__(self):
        for i in range(2, 10):
            self.numDict[str(i)] = i
        self.numDict["T"] = 10
        self.numDict["J"] = 11
        self.numDict["Q"] = 12
        self.numDict["K"] = 13
        self.numDict["A"] = 14

        # for i in ["s", "h", "d", "c"]:
        #     for j in range(2, 10):
        #         self.all_list_list.append([j, i])
        #     self.all_list_list.append([])
        #     self.all_list_list.append()
        #     self.all_list_list.append()
        #     self.all_list_list.append()
        #     self.all_list_list.append()
        #     self.all_list_list.append()

        for i in ["s", "h", "d", "c"]:
            for key, value in self.numDict.items():
                self.pokerDict[key + i] = [value, i]

        self.pokerDict["Xn"] = [-1, "n"]
        self.numDict["X"] = -1
        print("转换字典生成成功!\n")


if __name__ == "__main__":
    test = PokerDicts()
    print(test.pokerDict)
    print(test.numDict)
    print(test.pokerDict["Tc"])
