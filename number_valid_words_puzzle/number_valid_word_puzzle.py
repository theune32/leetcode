from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        answer = []
        for p in puzzles:
            number_solutions = 0
            for word in words:
                list_p = list(p)
                set_words = set(list(word))
                sol = True
                if list_p[0] not in set_words:
                    sol = False
                else:
                    for char in set_words:
                        if char not in set(list_p):
                            sol = False
                            break
                if sol:
                    number_solutions += 1
            answer.append(number_solutions)
        return answer

    def find_v_two(self, words: List[str], puzzles: List[str]) -> List[int]:
        for word, p in words, puzzles:
            set_word = set(list(word))
            p_list = list(p)
            if p_list[0] in set_word:
                comb = zip(set(list(word)), set(p_list))
                for i in comb:
                    if i[0] in i[1]:

