class Solution(object):
    def validateStackSequences(self, pushed, popped):
        st = []
        j = 0
        for i in range(len(pushed)):
            st.append(pushed[i])
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return j == len(popped)