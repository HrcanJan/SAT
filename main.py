import random


def create(n, var):
    retArr = []
    clauses = []
    for i in range(n):
        arr = []
        for j in range(3):
            x = random.randint(1, var)
            arr.append([x, random.randint(0, 1)])
            if x not in clauses:
                clauses.append(x)
        retArr.append(arr)
    return retArr, clauses


def cnf(arr, clauses):
    c = [-1 for i in range(len(clauses))]
    ret = 1
    for i in arr:
        x = False
        sat = []
        for j in i:
            index = clauses.index(j[0])
            if(c[index] == -1):
                y = random.randint(0, 1)
                c[index] = y
            else:
                y = c[index]
            z = j[1]
            if y == 0:
                z = (j[1] + 1) % 2
            if z == 1:
                x = True
        if not x:
            ret = 0
    return ret, c 


def cnf2(arr, clauses):
    n = len(clauses)
    c = [-1 for i in range(len(clauses))]
    for _ in range(3 * n):
        ret = 1
        failed = []
        for i in arr:
            x = False
            sat = []
            for j in i:
                index = clauses.index(j[0])
                if(c[index] == -1):
                    y = random.randint(0, 1)
                    c[index] = y
                else:
                    y = c[index]
                z = j[1]
                if y == 0:
                    z = (j[1] + 1) % 2
                if z == 1:
                    x = True
            
            if not x:
                ret = 0
                failed.append(i)
        #print(c)
        #print(failed)

        if(ret == 0):
            # print(len(failed), (n - len(failed)) / n)
            x = random.randint(0, len(failed) - 1)
            i = failed[x]
            y = random.randint(0, 2)
            index = clauses.index(i[y][0])
            c[index] = (c[index] + 1) % 2
        else:
            break

    return ret, c


arr, cl = create(20, 5)
# print(arr)
ret, clauses = cnf2(arr, cl)
print(ret)
print(clauses)