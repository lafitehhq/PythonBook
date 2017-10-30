# 使用unittest模块进行单元测试1.0
# 两个函数在每个测试的开始和结束都会运行一次，而不是把类中所有测试作为一个整体在开始或结束时各运行一次

import unittest

# 为每个单元测试的开始和结束提供 setUp 和tearDown 函数
# 提供不同类型的“断言”语句让测试成功或失败
class TestAddition(unittest.TestCase):
    def setUp(self):
        print('Setting up the Test!')

    def tearDown(self):
        print('Tearing down the Test')

    def test_twoPlusTwo(self):
        total = 2 + 2
        self.assertEqual(4, total)

if __name__ == '__main__':
    unittest.main()