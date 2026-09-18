class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
        # great = fine
        # drama = acting
        # skills = talent
        if len(sentence1) != len(sentence2):
            return False
        synos =  defaultdict(set)
        for word1, word2 in similarPairs:
            synos[word1].add(word2)
            synos[word2].add(word1)

        for index in range(len(sentence1)):
            word1 = sentence1[index]
            word2 = sentence2[index]
            if word1 == word2 or word2 in synos[word1]:
                continue
            return False
        return True