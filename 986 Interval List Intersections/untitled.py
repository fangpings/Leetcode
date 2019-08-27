class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []
        cur_A, cur_B = 0, 0
        ret = []
        while cur_A < len(A) and cur_B < len(B):
            if A[cur_A][0] < B[cur_B][0]:
                if A[cur_A][1] < B[cur_B][0]:
                    cur_A += 1
                elif A[cur_A][1] < B[cur_B][1]:
                    ret.append([B[cur_B][0], A[cur_A][1]])
                    cur_A += 1
                else:
                    ret.append(B[cur_B])
                    cur_B += 1
            else:
                if B[cur_B][1] < A[cur_A][0]:
                    cur_B += 1
                elif B[cur_B][1] < A[cur_A][1]:
                    ret.append([A[cur_A][0], B[cur_B][1]])
                    cur_B += 1
                else:
                    ret.append(A[cur_A])
                    cur_A += 1 
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.intervalIntersection([[-100, 100]], [[1,5],[8,12],[15,24],[25,26]]))

