"""
Challenge Statement:

    Given a sentence, count the number of times each word appears in the sentence.
      - All words should be counted in lowercase
      - Non-alphanumeric characters should be stripped from the beginning and end of each    
        word.
    

Example:

    Input:
        'hi i am bob'

    Expected Output:
        {
            'hi': 1,
            'i': 1,
            'am': 1,
            'bob': 1,
        }


Important Notes:

1. You may search online for any useful resources while solving the problem.
2. To run the test suite click the "Run" button in the top left.

"""

import unittest
import re


class WordCounter:

    @classmethod
    def count_word_frequency(cls, text):
        """
        Given a text returns the number of times a word appears.
        
        :param text: A string of text.
        :type text: str
        
        :return: A dictionary with key being the word and value being the number of times it appeared.
        :rtype: dict[str, int]
        """
        words = re.split(' +', text)

        if not sum([False if w == '' else True for w in words]):
            return {}

        w_count = {}
        for word in words:
            match = re.search('[A-Za-z0-9].*[A-Za-z0-9]|[A-Za-z0-9]', word)
            if match == None: continue
            
            word = match.group().lower()
            if word in w_count:
                w_count[word] += 1
            else:
                w_count[word] = 1

        return w_count
        
class WordCounterTestSuite(unittest.TestCase):

    def test_1(self):
        text_input = ''

        expected_output = {}

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_2(self):
        text_input = '. .   '

        expected_output = {}

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_3(self):
        text_input = 'a horse jumped with Overalls JUMPED into the pool.'

        expected_output = {
            'a': 1,
            'horse': 1,
            'with': 1,
            'overalls': 1,
            'jumped': 2,
            'into': 1,
            'the': 1,
            'pool': 1,
        }

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_4(self):
        text_input = 'Check.  Check.  Check one two three four.'

        expected_output = {
            'check': 3,
            'one': 1,
            'two': 1,
            'three': 1,
            'four': 1,
        }

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_5(self):
        text_input = 'She said: "why?"; He said, wow!'

        expected_output = {
            'she': 1,
            'said': 2,
            'why': 1,
            'he': 1,
            'wow': 1,
        }

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_6(self):
        text_input = 'Just - do it (or just laugh)'

        expected_output = {
            'just': 2,
            'do': 1,
            'it': 1,
            'or': 1,
            'laugh': 1,
        }

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_7(self):
        text_input = '1 + 1 = 2'

        expected_output = {
            '1': 2,
            '2': 1,
        }

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_8(self):
        text_input = 'Matt Billie-Yellow'

        expected_output = {
            'matt': 1,
            'billie-yellow': 1,
        }

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_9(self):
        text_input = '_Matt _matt_ Billie_*Yellow'

        expected_output = {
            'matt': 2,
            'billie_*yellow': 1,
        }

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_10(self):
        text_input = '-When+ _-when__'

        expected_output = {
            'when': 2,
        }

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

    def test_11(self):
        text_input = '***************abc123. ?abc123***************'

        expected_output = {
            'abc123': 2,
        }

        output = WordCounter.count_word_frequency(text_input)

        self.assertDictEqual(expected_output, output)

        
if __name__ == '__main__':

    unittest.main()