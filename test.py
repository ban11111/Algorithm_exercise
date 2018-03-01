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
            self.assertEqual(i["result"], cmp.compare_quick(i), "alice: " + i["alice"] + "  bob: " + i["bob"])

    def test_5_with_ghost(self):
        ghost = list()
        ghost.append({"alice": "AsKsXnJsTs", "bob": "XnKsQsJsTs", "result": 0})  # 这种情况在json的牌型里没有, 标记一下
        ghost.append({"alice": "9sTcKhXn7h", "bob": "Qh9sTcKhXn", "result": 2})
        ghost.append({"alice": "As5d4h3hXn", "bob": "5cJhAsQdXn", "result": 1})
        ghost.append({"alice": "4c5hXn7h9h", "bob": "4h5sXn7h9h", "result": 0})
        ghost.append({"alice": "3hXn4dKh8h", "bob": "6dXnTd5h4d", "result": 1})
        ghost.append({"alice": "Ad5dXn2c2d", "bob": "2c4d2dXn4s", "result": 2})

        for i in ghost:
            self.assertEqual(i["result"], cmp.compare_quick(i), "alice: " + i["alice"] + "  bob: " + i["bob"])

    def test_7_no_ghost(self):
        ghost = list()
        ghost.append({"alice": "2sAsKsQsJsTs9s", "bob": "Ah7hKh3hQhJhTh", "result": 0})
        ghost.append({"alice": "9sTcKh7h2d3d8s", "bob": "Qh9sTcKh7s6h5s", "result": 2})
        ghost.append({"alice": "As5d4h3h5s5h2s", "bob": "5c5hAsQdKh2s5d", "result": 1})
        ghost.append({"alice": "4c5h3s7h9h6d8s", "bob": "4h5s8c7h9h6s3s", "result": 0})
        ghost.append({"alice": "3hAs4dKh8h6h5s", "bob": "6dAsTd5h4d7h9s", "result": 1})
        ghost.append({"alice": "Ad5d2c3d2d5s3s", "bob": "2c4d2d4s5d5s7h", "result": 2})

        for i in ghost:
            self.assertEqual(i["result"], cmp.compare_quick(i), "alice: " + i["alice"] + "  bob: " + i["bob"])

    def test_7_with_ghost(self):
        ghost = list()
        ghost.append({"alice": "XnAsKsQsJsTs9s", "bob": "Xn7hKh3hQhJhTh", "result": 0})
        ghost.append({"alice": "9sTcKh7h2dXn8s", "bob": "Qh9sTcKhXn6h5s", "result": 2})
        ghost.append({"alice": "As5d4h3h5sXn2s", "bob": "9c5hAsXn4d2s5d", "result": 1})
        ghost.append({"alice": "4c5h3s7h9h6d8s", "bob": "4h5s8c7h9h6s3s", "result": 0})
        ghost.append({"alice": "3hAs4dKh8h6h5s", "bob": "6dAsTd5h4d7h9s", "result": 1})
        ghost.append({"alice": "Ad5d2c3d2d5s3s", "bob": "2c4d2d4s5d5s7h", "result": 2})

        for i in ghost:
            self.assertEqual(i["result"], cmp.compare_quick(i), "alice: " + i["alice"] + "  bob: " + i["bob"])


if __name__ == '__main__':
    unittest.main()
