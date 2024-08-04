import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def test_luke_skywalker(self):
        result = self.solution.run("Luke Skywalker")
        self.assertEqual(result, 5)
    
    def test_darth_vader(self):
        result = self.solution.run("Darth Vader")
        self.assertEqual(result, 4)  
    
    def test_yoda(self):
        result = self.solution.run("Yoda")
        self.assertEqual(result, 5)
    
    def test_non_existent_character(self):
        result = self.solution.run("Non Existent Character")
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
