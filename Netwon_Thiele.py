"""
牛顿-Thiele插值算法
"""
from Netwon_Taylor import Taylor

"""计算逆差商的值"""
def nichashang(X,Y):
    if (len(X) == 1):
        return Y[0]
    if (len(X) == 2):
        return (X[1] - X[0]) / (Y[1] - Y[0])
    else:
        Ori_1 = []
        Ori_1_label = []
        Ori_2 = []
        Ori_2_label = []
        n = len(X) - 1
        debug = (X[n] - X[n - 1])
        for i in range(n - 1):
            Ori_1.append(X[i])
            Ori_1_label.append(Y[i])
            Ori_2.append(X[i])
            Ori_2_label.append(Y[i])
        Ori_1.append(X[n])
        Ori_1_label.append(Y[n])
        Ori_2.append(X[n - 1])
        Ori_2_label.append(Y[n-1])
        debug1 = nichashang(Ori_1, Ori_1_label)
        debug2 = nichashang(Ori_2, Ori_2_label)
        val = debug / (debug1 - debug2)
        return val

"""验证逆差商分母是否为0，返回一个布尔值"""
def vaild_nichashang(X,Y,BOOL = True):
    if (len(X) == 1):
        return Y[0], BOOL
    if (len(X) == 2):
        if (Y[1] != Y[0]):
            return (X[1] - X[0]) / (Y[1] - Y[0]), BOOL
        else:
            BOOL = False
            return (X[1] - X[0]) / (Y[1] - Y[0]+3), BOOL
    else:
        Ori_1 = []
        Ori_1_label = []
        Ori_2 = []
        Ori_2_label = []
        n = len(X) - 1
        debug = (X[n] - X[n - 1])
        for i in range(n - 1):
            Ori_1.append(X[i])
            Ori_1_label.append(Y[i])
            Ori_2.append(X[i])
            Ori_2_label.append(Y[i])
        Ori_1.append(X[n])
        Ori_1_label.append(Y[n])
        Ori_2.append(X[n - 1])
        Ori_2_label.append(Y[n-1])
        debug1,bool_1 = vaild_nichashang(Ori_1, Ori_1_label)
        debug2,bool_2 = vaild_nichashang(Ori_2, Ori_2_label)
        if (bool_1 == False):
            BOOL=False
        if (bool_2 == False):
            BOOL = False
        if (debug1 == debug2):
            BOOL = False
            return debug / (debug1 - debug2+10), BOOL
        else:
            xujian = debug / (debug1 - debug2)
        return xujian, BOOL

def Netwon_Thiele(x,b,X):
    m = len(X)
    result = (x-X[m-2])/b[m-1]
    while (m>=3):
        result = (x-X[m-3])/(b[m-2]+result)
        m = m-1
    result = result+b[0]
    return result

"""X和Y可以人为定义，利用X和Y可以求出对应的插值函数f，f(x)是待预测的点，可以人为定义"""
X = [1,3,6,2]
Y = [4,12,39,7] # 可以根据自己的情况，修改已知的插值点
x = 10 # 可以修改相应的x的值

Z = []
Z_label = []
b = []
num = len(X)
# 下面是验证逆差商为0的条件 #
_,BOOL = vaild_nichashang(X,Y)
if(BOOL==True):
    print('使用Netwon-thiele插值：')
else:
    print("逆差商分母分0，使用Netwon-Taylor插值：")
if BOOL:
    for i in range(num):
        Z.append(X[i])
        Z_label.append(Y[i])
        b.append(nichashang(Z, Z_label))  # 这里计算的是逆差商的数组，存储在b中
    final_result = Netwon_Thiele(x, b, X)
    print(final_result)
else:
    func = Taylor()
    final_result = func.Interpolate_Taylor(X,Y,x)
    print(final_result)








