class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=9
        row=9
        rowhash={}
        colhash={}
        squarehash={}
        for i in range(row):
            
            for j in range(col):
                index=((i//3)*3+(j//3))
                val=board[i][j]
                if i not in rowhash:
                        rowhash[i]=[]
                if j not in colhash:
                        colhash[j]=[]
                if index not in squarehash:
                    squarehash[index]=[]
                
                if ((val!="." ) and  (val in rowhash[i] or val in colhash[j] or val in squarehash[index])):

                    return False
                else:
                    rowhash[i].append(val)
                    colhash[j].append(val)
                    squarehash[index].append(val)
                    print(index)
                    
        return True

        