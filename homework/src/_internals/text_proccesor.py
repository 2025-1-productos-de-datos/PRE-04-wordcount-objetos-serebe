class TextProcessor:
    '''Class to preprocess text lines and split them into words'''
    @staticmethod
    def preprocess_lines(self,lines):
        """Preprocess lines by normalizing and cleaning text."""
        return [line.lower().strip() for line in lines]
    @staticmethod
    def split_into_words(self, lines):
        """Split lines into individual words and clean punctuation."""
        words = []
        for line in lines:
            words.extend(word.strip(",.!?") for word in line.split())
        return words