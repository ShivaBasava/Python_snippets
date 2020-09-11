class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        C = [[0 for _ in range(len(B[0]) * 3 - 2)]
             for _ in range(len(B) * 3 - 2)]

        for i in range(len(B)):
            for j in range(len(B[0])):
                C[i + len(B) - 1][j + len(B[0]) - 1] = B[i][j]

        total_cnt = 0
        for i in range(len(C) - len(A) + 1):
            for j in range(len(C[0]) - len(A[0]) + 1):
                cnt = 0
                #Traversing count
                for a in range(len(A)):
                    for b in range(len(A[0])):
                        #Traversing count ia & jb, Counting
                        ia, jb = i + a, j + b
                        #If A covers B, we incrementing 'cnt' value by 1
                        if 1 == C[ia][jb] == A[a][b]:
                            cnt += 1
        #and returning the maximum value ('total_cnt') is what we want.
                if cnt > total_cnt:
                    total_cnt = cnt
        return total_cnt  
