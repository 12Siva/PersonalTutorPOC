import unittest

class TestExecutionRunner(unittest.TestCase):
  
  def test_HappyPath(self):
      self.assertEqual('foo'.upper(), 'FOO')

 
  def test_LoadTest(self):
    for i in range(0,490):
      self.assertEqual('foo'.upper(), 'FOO')
      
  

if __name__ == '__main__':
    unittest.main()
