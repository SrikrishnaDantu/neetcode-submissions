class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        my_list = []
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s not in my_dict:
                my_dict[s] = [i]
            else:
                my_dict[s].append(i)
        for word, value in my_dict.items():
            my_list.append([strs[x] for x in my_dict[word]])
        return my_list

        