# Define Document class

from collections import Counter

# from token_utils import tokenize  # Import the tokenize function

from .counter_utils import plot_counter, sum_counters
from collections import Counter

# Define Document class

class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """

    def __init__(self, text):
        self.text = text
        # Tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # Perform word count with non-public count_words method
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)
        
    # non-public method to tally document's word counts with Counter
    def _count_words(self):
        return Counter(self.tokens)

    def plot_counts(self, attribute='word_counts', n_most_common=5):
        """Plot most common elements of a ``collections.Counter`` instance attribute

        :param attribute: name of ``Counter`` attribute to use as an object to plot
        :param n_most_common: number of elements to plot (using ``Counter.most_common()``)
        :return: None; a plot is shown using matplotlib

        >>> doc = Document("duck duck goose is fun when you're the goose")
        >>> doc.plot_counts('word_counts', n_most_common=5)  # same as the default call
        """
        plot_counter(getattr(self, attribute), n_most_common)

# This is extracted from Datacamp
import re

def tokenize(text):
    """Split text into tokens using a regular expression

    This is a wrapper for re.findall with case ignored.

    :param text: text to be tokenized
    :return: a list of resulting tokens

    >>> tokenize("word word 1.22 can't. cannot")
    ['word', 'word', 'can', 't', 'cannot']
    """
    # return re.findall(r'[a-zA-z#@]+', text, flags=re.IGNORECASE) # This is the original line
    return re.findall(r'[a-zA-z#@]+', text, flags=re.IGNORECASE)


### Below is the original one


# ### Below is my modification attempt

# def __init__(self, text):
#     self.text = text
#     # Tokenize the document with non-public tokenize method
#     self.tokens = self._tokenize()
#     # Perform word count with non-public count_words method
#     self.word_counts = self._count_words()

# def _tokenize(self):
#     tokenized = tokenize(self.text)

#     token_string_list = []
#     for i in range(len(tokenized)):
#         token_string_list.append(tokenized[i].string)
#     return  token_string_list
    
# # non-public method to tally document's word counts with Counter
# def _count_words(self):
#     return Counter(self.tokens)