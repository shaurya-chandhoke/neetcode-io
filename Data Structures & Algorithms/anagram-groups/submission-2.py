class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = collections.defaultdict(list)
        return_list = []

        for el in strs:
            sorted_str = "".join(sorted(el))
            table[sorted_str].append(el)
        
        for item in table.values():
            return_list.append(item)

        return return_list