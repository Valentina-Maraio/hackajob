import pytest

class TestSolution:
    def test_example(self):
        # Example test for a known output
        assert "this is an example" == "this is an example"

    def test_run(self):
        # Create an instance of the Solution class
        solution = Solution()
        
        # Test case 1
        assert solution.run(1, 5) == "1,2,Fizz,4,Buzz"
        
        # Test case 2
        assert solution.run(10, 15) == "Buzz,11,Fizz,13,14,FizzBuzz"
        
        # Test case 3
        assert solution.run(3, 7) == "Fizz,4,Buzz,Fizz,7"
        
        # Test case 4
        assert solution.run(15, 15) == "FizzBuzz"
        
        # Test case 5 (edge case where N > M)
        assert solution.run(5, 1) == ""  # No numbers in this range

if __name__ == "__main__":
    pytest.main()