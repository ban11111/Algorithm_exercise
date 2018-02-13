class PokerDicts:
    pokerDict, numDict = {}, {}

    def __init__(self):
        for i in range(2, 10):
            self.numDict[str(i)] = i
        self.numDict["T"] = 10
        self.numDict["J"] = 11
        self.numDict["Q"] = 12
        self.numDict["K"] = 13
        self.numDict["A"] = 14

        for i in ["s", "h", "d", "c"]:
            for key, value in self.numDict.items():
                self.pokerDict[key + i] = value
