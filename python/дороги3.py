# N - кількість координат для N міст
# A - список координат міст ((x0, y0), (x1,y1),...(xN-1, yN-1))
# res - сумарна довжина доріг, враховуючи прямі дороги між містами
#
debug = 0  # 0..8 (1:A,2:dist,4:lines,8:input) - друк проміжних результатів

import io
def datainput(filename): #формування списку координат А()
    try:
        with open(filename) as f:
            n =  int(f.readline())
            a = []
            for i in  range(1,n+1):
                x,y = f.readline().split()   #c = f.readline().split()
                c = (int(x),int(y),i)        #c = tuple(map(int, c))
                a.append(c)
                if debug & 8: print('%3.d: %3s, %s' %(i,x,y))
            a = tuple(sorted(a,key=lambda x:(x[0],x[1]))) #закрити сорт.список від змін =тільки читати + швидкість доступу
            if debug & 1: print('\n'.join(map(str,a)))
            return  a 
    except FileNotFoundError:
        print(filename, " file is missing")
        exit()
    except PermissionError:
        print("You are not allowed to read ",filename)
        exit()

def dataINPUT(filename): #формування списку координат А()
    try:
        n = None
        a = []
        for line in open(filename):
            if n == None:
                n =  int(line)
                continue
            n -= 1  
            if n < 0: break
            c = line.split()
            c = tuple(map(int, c))
            a.append(c)
        a.sort()
        a = tuple(a) #закрити список від змін =тільки читати + швидкість доступу
        if debug & 1: print('\n'.join(map(str,a)))
        return  a 
    except FileNotFoundError:
        print(filename, " file is missing")
        exit()
    except PermissionError:
        print("You are not allowed to read ",filename)
        exit()

        
    #A = [[ int(j) for j in f.readline().split() ] for i in range(N) ]
    #A = [(0,0),(40,0),(80,0),(0,30),(40,30),(80,30),(0,60),(40,60),(80,60)]

#from math import sqrt
def dist(t1,t2):  #відстань між містами t1, t2 / 0..N-1/ 
    global A
    x1,y1,t_1 = A[t1]
    x2,y2,t_2 = A[t2]
    d1 = ((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))**0.5
    if debug & 2: print("(%d, %d) = %0.2f" % (t_1, t_2, d1))
    return d1

def lines(b, e):  #перевірка, чи знайдуться міста (b+1,..e) на одній прямій із (b,e)
    global A
    flg = 0
    for i in range(b+1, e):
        x1,y1,tb = A[b]
        x2,y2,ti = A[i]    
        x3,y3,te = A[e]
        if abs( float(y2-y1)*float(x3-x1)- float(y3-y1)*float(x2-x1) ) < 0.0001:
           flg = 1
           if debug &4: print("(%d ->%d->%d) = пряма" % (tb, ti, te))
           break
    return flg

A = datainput("input.txt")
#A = dataINPUT("input.txt")
N = len(A)
res = 0
        
for i in range(N-1):
    for j in range(i+1,N):
        if not lines(i,j):
            res = res + dist(i,j)
            
print("%d" % res )
