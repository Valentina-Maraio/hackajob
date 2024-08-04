import pytest

class TestSolution:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solution = Solution()

    def test_english_to_morse(self):
        assert self.solution.run(False, "SOS") == "... --- ..."

    def test_morse_to_english(self):
        assert self.solution.run(True, "... --- ...") == "sos"

    def test_sentence_english_to_morse(self):
        input_text = "THE QUICK BROWN FOX"
        expected_output = "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-"
        assert self.solution.run(False, input_text) == expected_output

    def test_sentence_morse_to_english(self):
        input_text = "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-"
        expected_output = "the quick brown fox"
        assert self.solution.run(True, input_text) == expected_output

    def test_punctuation(self):
        assert self.solution.run(False, "Hello, World!") == ".... . .-.. .-.. --- --..--   .-- --- .-. .-.. -.. -.-.--"

    def test_numbers(self):
        assert self.solution.run(False, "123") == ".---- ..--- ...--"

    def test_mixed_case(self):
        assert self.solution.run(False, "MixEd CaSe") == "-- .. -..- . -..   -.-. .- ... ."

    def test_multiple_spaces(self):
        assert self.solution.run(False, "Two  Spaces") == "- .-- ---      ... .--. .- -.-. . ..."

    def test_invalid_morse(self):
        # This test might need adjustment based on how your implementation handles this case
        result = self.solution.run(True, "... --- ... ---")
        assert result in ["soso", "Invalid Morse Code Or Spacing"]

    def test_invalid_spacing_morse(self):
        assert self.solution.run(True, "..- .... ..-. .-.. --- .-    ...-") == "Invalid Morse Code Or Spacing"

    def test_empty_input(self):
        assert self.solution.run(True, "") == "Invalid Morse Code Or Spacing"

    def test_long_sentence(self):
        morse = "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--   .--- .. -. -..- . -..   - .... .   --. -. --- -- . ...   -... . ..-. --- .-. .   - .... . -.--   ...- .- .--. --- .-. .. --.. . -.. .-.-.-"
        english = "the wizard quickly jinxed the gnomes before they vaporized."
        assert self.solution.run(True, morse) == english

if __name__ == "__main__":
    pytest.main()