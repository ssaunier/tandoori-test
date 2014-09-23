class HelloWorld:
  def greets(self, name):
    return "Hello World, %s" % name

import unittest

class TestHelloWorld(unittest.TestCase):

  def setUp(self):
    self.hw = HelloWorld()

  def test_greets(self):
    self.assertEqual(self.hw.greets("John"), "Hello World, John")


if __name__ == '__main__':
    unittest.main()