# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word1_dic = Counter(words[0])

        for word in words:
            current_dic = Counter(word)
            for c in word1_dic:
                word1_dic[c] = min(word1_dic[c], current_dic[c])
        print(word1_dic)

        result = []
        for c in word1_dic:
            for _ in range(word1_dic[c]):
                result.append(c)
        return result



