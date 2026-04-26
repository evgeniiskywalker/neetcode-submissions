class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for ind in range(len(nums)):
            hashmap[nums[ind]] = hashmap.get(nums[ind], 0) + 1

        # hashmap.items() ->  [(key, val), ...]

        return [x[0] for x in sorted(hashmap.items(), key=lambda x:x[1], reverse=True)][:k]