import sys

sys.stdin=open("chap06/2.txt", "r")

def DFS(v):
    if v>7:
        return
    else:  
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2+1)
        
if __name__=="__main__":
    DFS(1)