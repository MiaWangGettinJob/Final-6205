#Time complexity: O(n)
class Solution:
    def minimumdel(self, s):
        stack = []
        todelete = set()

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            if char == ")":
                if not stack:
                    todelete.add(i)
                else:
                    stack.pop()
        for i in stack:
            todelete.add(i)
        result = []
        for i, char in enumerate(s):
            if i not in todelete:
                result.append(char)

        return "".join(result)


def main():
    a = Solution
    s = "a)b(c)d"
    print(a.minimumdel(a,s))
    s = "lee(t(c)o)de)"
    print(a.minimumdel(a,s))
    s = "))(("
    print(a.minimumdel(a,s))

main()
