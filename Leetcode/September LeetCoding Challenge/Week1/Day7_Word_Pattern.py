class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        :type pattern: str
        :type str: str
        :return type: bool
        """
        
        temp1 = {}
        temp2 = {}
        #handle the last word when you split the str.
        words = str.split(' ')
        
        if len(words)!=len(pattern):
            return False
        #zip() function takes iterables (can be zero or more)
        #Here two Iterables are passed
        #1st - 'words', has the individual letters
        #2nd - 'pattern' has the word
        for word, ch in zip(words, pattern):
            #The char to word is a bijection, which means it is a one-to-one mapping.
            if temp1.get(word) == ch and temp2.get(ch) == word:
                pass            
            elif word not in temp1 and ch not in temp2:
                temp1[word] = ch
                temp2[ch] = word
            else:
                return False
        
        return True
