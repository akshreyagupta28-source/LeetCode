class Solution(object):
    def isValid(self, s):
        st = []

        for c in s:
            if c == '(':
                st.append(')')
            elif c == '{':
                st.append('}')
            elif c == '[':
                st.append(']')
            elif not st or st[-1] != c:
                return False
            else:
                st.pop()

        return len(st) == 0
        