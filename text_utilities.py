class text:
    @staticmethod
    def word_length(word: str):
        return len(word)
    
    @staticmethod
    def split_char(word: str):
        chars = []
        for i in word:
            chars.append(i)
        return chars
    
    @staticmethod
    def line_by_line(word: str):
        for j in word:
            print(j)
