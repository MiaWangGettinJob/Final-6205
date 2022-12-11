#Time complexity: O(n)
import collections


class Solution:
    def organize(self,strs):
        visited = collections.defaultdict(list)
        for string in strs:
            sortedstring = "".join(sorted(string))
            if sortedstring not in visited:
                visited[sortedstring] = [string]
            else:
                visited[sortedstring].append(string)
        result = []
        for strings in visited.values():
            result.append(strings)

        return result


def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    a = Solution
    print(a.organize(a, ["eat","tea","tan","ate","nat","bat"]))


main()

