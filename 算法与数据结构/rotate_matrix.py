class Solution:
    def rotate(self, matrix):
        n=len(matrix)
        matrix_new=[[0]*n for _ in range(n)] #下划线和for i in ... 的i作用相同
        #[0]*3=[0,0,0]
        for i in range(n):#行
            for j in range(n):#列
                matrix_new[j][n-i-1]=matrix[i][j]
        matrix[:]=matrix_new
'''
 5  1  9 11              x  x  x  5
 x  x  x  x   =旋转后=>   x  x  x  1
 x  x  x  x              x  x  x  9
 x  x  x  x              x  x  x 11
'''
