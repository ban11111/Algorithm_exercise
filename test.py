import unittest
import poker_comparison as cmp


# TODO, 增加单元测试
class TestPoker(unittest.TestCase):

    def test_5_no_ghost(self):
        ghost = list()
        ghost.append({"alice": "AsKsQsJsTs", "bob": "AsKsQsJs2s", "result": 1})
        ghost.append({"alice": "9sTcKh4d7h", "bob": "Qh9sTcKh4d", "result": 2})
        ghost.append({"alice": "As5d4h3h2d", "bob": "5cJhAsQdKh", "result": 1})
        ghost.append({"alice": "4c5h3s7h9h", "bob": "4h5h3s7h9h", "result": 0})
        ghost.append({"alice": "3h5h4dKh8h", "bob": "6d7dTd5h4d", "result": 1})
        ghost.append({"alice": "Ad5d8d2c2d", "bob": "2c4d2d9h4s", "result": 2})

        for i in ghost:
            self.assertEqual(i["result"], cmp.compare_quick(i))


if __name__ == '__main__':
    unittest.main()
