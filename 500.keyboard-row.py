class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
        row_index_by_char = {}
        for row_index in range(len(rows)):
            for char in rows[row_index]:
                row_index_by_char[char] = row_index

        result = []
        for word in words:
            if not word:
                result.append(word)
                continue
            
            word_is_good = True
            potential_row = row_index_by_char[word[0]]
            for char in word:
                if row_index_by_char[char] != potential_row:
                    word_is_good = False

            if word_is_good:
                result.append(word)

        return result

