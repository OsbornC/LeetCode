class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ls = list(s)
        stk = []
        res = []
        idx = 0
        for item in ls:
            if item == ')':
                if stk:
                    loc = stk.pop()
                    res.append(')')
                    res[loc] = '('
                else:
                    res.append(' ')
            elif item == '(':
                stk.append(idx)
                res.append(' ')
            else:
                res.append(item)
            idx += 1
        res[:] = [i for i in res if i != ' ']
        return ''.join(res)
                    