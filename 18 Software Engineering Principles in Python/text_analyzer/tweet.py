
from .document import Document
from collections import Counter

class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      

    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')

def filter_word_counts(word_counts, first_char):
    """Filter Document.word_counts by the first character of the word
    
    :param word_counts: the word_counts attribute of a Document class instance
    :param first_char: only keep word counts that start with this character
    
    >>> # How to filter to only words that start with 'A'
    >>> filter_word_counts(document.word_counts, 'A')
    """

    return Counter({k: v for k, v in word_counts.items() if k[0] == first_char})

class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(text)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text)
    
def filter_lines(text, first_chars):
    """Filter lines by beginning characters (case sensitive)

    :param text:  multi-line text to filter
    :param first_chars: required characters for line to start with to be returned
    :return: text with only lines starting with first_chars included

    >>> text = 'humpty dumpty\\nsat on a wall\\nhumpty dumpty\\nhad a great fall'
    >>> filter_lines(text, 'h')
    'humpty dumpty\\nhumpty dumpty\\nhad a great fall'

    >>> filter_lines(text, 'humpty')
    'humpty dumpty\\nhumpty dumpty'
    """
    n_chars = len(first_chars)
    lines = text.split('\n')

    filtered_lines = [l for l in lines if l[:n_chars] == first_chars]

    return '\n'.join(filtered_lines)