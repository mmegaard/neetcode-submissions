class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
        # great = fine
        # drama = acting
        # skills = talent
        if len(sentence1) != len(sentence2):
            return False
        synos = {}
        for word, syn in similarPairs:
            if not synos.get(word): 
                synos[word] = set()
            if not synos.get(syn):
                synos[syn] = set()
            synos[word].add(syn)
            synos[syn].add(word)

        for index in range(len(sentence1)):
            word1 = sentence1[index]
            word2 = sentence2[index]
            print(word1,word2)
            if word1 == word2:
                continue
            elif synos.get(word1) and word2 in synos[word1]:
                sentence1[index] = word2
               # print('changed', word1, 'to', synos[word1], 'to match', word2)
                #if sentence1[index] != sentence2[index]:
                   # print("this didn't fix it")
            elif synos.get(word2) and word1 in synos[word2]:
                sentence2[index] = word1
                #print('changed', word2, 'to', synos[word2], 'to match', word1)
                #if sentence1[index] != sentence2[index]:
                    #print("this didn't fix it")
            else:
                return False
        return sentence1 == sentence2