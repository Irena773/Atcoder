import sys
N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]
X,Y = [list(i) for i in zip(*XY)]
S = input()

right_min, left_max = dict(), dict()

for i in range(N):
    # →　←が存在するかの判定を右か左かで分けて行う
    if S[i] == "R":
        # 左向きでかつ同じY座標の点があるかどうか
        # ←が　→よりも右側にあるか(←のほうのX座標のほうがおおきいかどうか)
        if Y[i] in left_max and X[i] < left_max[Y[i]]:
            print("Yes")
            sys.exit()
    else:
        if Y[i] in right_min and right_min[Y[i]] < X[i]:
            print("Yes")
            sys.exit()    

    # 右を向いていて同じY座標の点が存在するときの一番左にいる点を求める(→)
    if S[i] == "R":
        if Y[i] in right_min:
            right_min[Y[i]] = min(X[i], right_min[Y[i]])
        else:
            right_min[Y[i]] = X[i]        
    # 左を向いていて同じY座標の点が存在するときの一番右にいる点を求める(←) 
    else:
        if Y[i] in left_max:
            left_max[Y[i]] = max(X[i], left_max[Y[i]])
        else:
            left_max[Y[i]] = X[i]    
print("No")
