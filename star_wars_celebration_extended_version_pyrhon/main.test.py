
class TestSolution:
    def test_example(self):
        assert "this is an example" == "this is an example"

    def test_run_existing_film_and_character(self):
        solution = Solution()
        result = solution.run("A New Hope", "Luke Skywalker")
        assert result is not None
        assert "A New Hope:" in result
        assert "Luke Skywalker:" in result
        assert "A New Hope" in result.split("Luke Skywalker:")[1]

    def test_run_existing_film_non_existing_character(self):
        solution = Solution()
        result = solution.run("The Force Awakens", "Walter White")
        assert result is not None
        assert "The Force Awakens:" in result
        assert "Walter White: none" in result

    def test_run_spock_in_return_of_the_jedi(self):
        solution = Solution()
        result = solution.run("Return of the Jedi", "Spock")
        assert result is not None
        assert "Return of the Jedi:" in result
        assert "Spock: none" in result

    def test_run_non_existing_film(self):
        solution = Solution()
        result = solution.run("Non Existing Film", "Luke Skywalker")
        assert result is None

if __name__ == "__main__":
    pytest.main()