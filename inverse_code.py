def start():
    check=True
    while check:
       try:
             r,c=map(int,input('enter the number of rows and columns').split())
             if r==c:
                   check=False
             else:
                   print('Non-square matrices (m-by-n matrices for which m ≠ n) do not have an inverse')
       except ValueError:
             print('please enter the value in right format row then col')

    print(50*('-'))
    return (r,c)

################################################################################################################

def inp(r,c):
    m=[]
    inverse=[]

    for i in range(r):
        row=[]
        inv=[]
        for j in range(c):
            row.append(int(input(f'please enter the [{i}][{j}] element')))
            if i==j:
                  inv.append(1)
            else:
                  inv.append(0)
        m.append(row)
        inverse.append(inv)
    m,inverse=positoin(m,inverse)
    return m,inverse

################################################################################################################

def singular(m):
  total = 0
  for element in m[r-1]:
        total += element
  if total==0:
        print('this matrix is singular')
        exit()

################################################################################################################

def positoin(m,inverse):
    for i in range(len(m)):
        if m[i][i] != 0:
            pass
        else:
            for j in range(i+1,len(m)):
                if m[j][i] != 0:
                    li=m[j]
                    m[j]=m[i]
                    m[i]=li
                    inv=inverse[j]
                    inverse[j] = inverse[i]
                    inverse[i] = inv
                    break
                elif j==len(m)-1:
                    print('this matrix is singular')
                    exit()
    return (m,inverse)

################################################################################################################




def echelon(m,inverse,r):
    for i in range(r):
            for j in range(i+1,r):
                if m[j][i]==0:
                    continue
                update=-(m[j][i]/m[i][i])
                m[i]=[update * x for x in m[i]]
                inverse[i] = [update * x for x in inverse[i]]

                m[j]=[x+y for x,y  in zip(m[i],m[j])]
                inverse[j] = [x + y for x, y in zip(inverse[i], inverse[j])]

    singular(m)
    return m,inverse

################################################################################################################

def rrec(m, inverse, r):
    for i in range(r - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if m[j][i] == 0:
                continue
            update = -(m[j][i] / m[i][i])
            m[i] = [update * x for x in m[i]]
            inverse[i] = [update * x for x in inverse[i]]

            m[j] = [x + y for x, y in zip(m[i], m[j])]
            inverse[j] = [x + y for x, y in zip(inverse[i], inverse[j])]


    for i in range(r):
        inverse[i]=[ x/m[i][i] for x in inverse[i]]

    return m,inverse

################################################################################################################

r,c = start()
m,inverse = inp(r,c)
m,inverse = echelon(m,inverse,r)
m,inverse = rrec(m,inverse,r)

print(50*'-')
print('the inverse matrix is')
print(inverse)