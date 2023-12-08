class Anagram:

    def __init__(self, word):
        self.word = word
        

    def word(self, word_list):
        return [word for word in word_list if self.is_anagram(word)]
    
    def is_anagram(self, other_word):
        return sorted(self.word.lower()) == sorted(other_word.lower())