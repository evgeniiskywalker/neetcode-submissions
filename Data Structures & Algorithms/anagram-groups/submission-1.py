class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # trasform:['word1', 'word2', ...]

        for word in strs: 
            key = {} # letter:count

            for letter in word:
                key[letter] = key.get(letter, 0) + 1
            
            key = tuple(sorted(key.items()))
            
            if key not in hashmap:
                hashmap[key] = []
            hashmap.get(key, []).append(word)

        return list(hashmap.values())