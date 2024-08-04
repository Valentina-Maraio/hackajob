class Solution:
    def run(self, morseToEnglish, textToTranslate):
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
            'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
            'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
            'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-',
            'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
            '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
            ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
            '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
            '@': '.--.-.', ' ': ' '
        }
        
        reverse_morse_dict = {v: k for k, v in morse_dict.items()}
        
        def morse_to_english(morse_text):
            if not morse_text or '    ' in morse_text:  # Check for empty input or too many spaces
                return 'Invalid Morse Code Or Spacing'
            
            words = morse_text.split('   ')
            result = []
            for word in words:
                letters = word.split()
                if not letters or '' in letters:  # Check for empty words or extra spaces within words
                    return 'Invalid Morse Code Or Spacing'
                if any(letter not in reverse_morse_dict for letter in letters):
                    return 'Invalid Morse Code Or Spacing'
                result.append(''.join(reverse_morse_dict[letter] for letter in letters))
            
            return ' '.join(result)
        
        def english_to_morse(english_text):
            words = english_text.split(' ')
            morse_words = []
            for word in words:
                morse_word = ' '.join(morse_dict[char] for char in word if char in morse_dict)
                morse_words.append(morse_word)
            return '   '.join(morse_words)
        
        if morseToEnglish:
            translatedText = morse_to_english(textToTranslate)
        else:
            translatedText = english_to_morse(textToTranslate)
        
        return translatedText