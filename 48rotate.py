class Solution:
    # def rotate(self, A):
    #     A[:]=zip(*A[::-1])
    #     return A

    # def rotate(self, A):
    #     n = len(A)
    #     for i in range(int(n/2)):
    #         for j in range(n-int(n/2)):
    #             A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
    #                      A[~j][i], A[~i][~j], A[j][~i], A[i][j]

    def rotate(self, A):
        # tranpose first, then flip horizontally
        n = len(A)

        for i in range(n):
            for j in range(i+1, n):
                tmp=A[i][j]
                A[i][j]=A[j][i]
                A[j][i]=tmp

        for i in range(n):
            for j in range(int(n/2)):
                tmp=A[i][j]
                A[i][j]=A[i][~j]
                A[i][~j]=tmp

        return A


obj=Solution()
print(obj.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))

# check the discussion, some short answers
