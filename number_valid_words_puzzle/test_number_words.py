from number_valid_words_puzzle.number_valid_word_puzzle import Solution

def test_standard():
    sol = Solution()
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    output = [1, 1, 3, 2, 4, 0]
    assert sol.findNumOfValidWords(words, puzzles) == output

def test_basic():
    sol = Solution()
    words = ["aaaa"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    output = [1, 1, 1, 1, 1, 0]
    assert sol.findNumOfValidWords(words, puzzles) == output

test_standard()