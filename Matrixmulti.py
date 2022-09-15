class Matrix:
    def MatrixMul(self,A,B):
        n=len(A)
        p=len(B)
        q=len(B[0])
        if len(A[0])!=p:
            return -1
        # C=[[0]*q]*n
        C=[[0 for i in range(q)]for k in range(n) ]
        for i in range(n):
            for j in range(q):
                for k in range(p):
                    C[i][j]+=A[i][k]*B[k][j]
                    print(C[i][j])
            
        return C

mul=Matrix()
result=mul.MatrixMul([[0,2,9],[1,3,8]],[[2,2],[1,8],[1,8]])
print(result)

        
















