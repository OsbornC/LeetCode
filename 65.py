class Solution:
    def isNumber(self, s: str) -> bool:
        num_after_e, num_show_up, dot_show_up, e_show_up = False, False, False, False
        numbers = [str(i) for i in range(10)]
        n = len(s.strip())
        for i in range(n):
            if s[i] in numbers:
                num_after_e = True
                num_show_up = True
            elif s[i] in ('+', '-'):
                if i != 0 and (s[i-1] not in ('e', 'E')):
                    return False
            elif s[i] in ('E', 'e'):
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            elif s[i] == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            else:
                return False
        return num_show_up and num_after_e
                