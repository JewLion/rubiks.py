import random

frontFace = [['red','red','red'],['red','red','red'],['red','red','red']]
rightFace = [['green','green','green'],['green','green','green'],['green','green','green']]
backFace = [['orange','orange','orange'],['orange','orange','orange'],['orange','orange','orange']]
leftFace = [['blue','blue','blue'],['blue','blue','blue'],['blue','blue','blue']]
downFace = [['white','white','white'],['white','white','white'],['white','white','white']]
upFace = [['yellow','yellow','yellow'],['yellow','yellow','yellow'],['yellow','yellow','yellow']]
cube = [frontFace, rightFace, backFace, leftFace, downFace, upFace]

f = [['red','red','red'],['red','red','red'],['red','red','red']]
r = [['green','green','green'],['green','green','green'],['green','green','green']]
b = [['orange','orange','orange'],['orange','orange','orange'],['orange','orange','orange']]
l = [['blue','blue','blue'],['blue','blue','blue'],['blue','blue','blue']]
d = [['white','white','white'],['white','white','white'],['white','white','white']]
u = [['yellow','yellow','yellow'],['yellow','yellow','yellow'],['yellow','yellow','yellow']]
finished = [f,r,b,l,d,u]

def rotate(face, inv):
    ogFace = [['','',''],['','',''],['','','']]
    for i in range(0,3):
        for j in range(0,3):
            ogFace[i][j] = face[i][j]
    if (inv):
        face[0][0] = ogFace[0][2]
        face[0][1] = ogFace[1][2]
        face[0][2] = ogFace[2][2]

        face[1][0] = ogFace[0][1]
        face[1][2] = ogFace[2][1]

        face[2][0] = ogFace[0][0]
        face[2][1] = ogFace[1][0]
        face[2][2] = ogFace[2][0]
    else:
        face[0][0] = ogFace[2][0]
        face[0][1] = ogFace[1][0]
        face[0][2] = ogFace[0][0]

        face[1][0] = ogFace[2][1]
        face[1][2] = ogFace[0][1]

        face[2][0] = ogFace[2][2]
        face[2][1] = ogFace[1][2]
        face[2][2] = ogFace[0][2]


def right(inv = False):
    rotate(rightFace, inv)
    fArr = []
    uArr = []
    bArr = []
    dArr = []
    for i in range(0,3):
        fArr.append(frontFace[i][2])
        uArr.append(upFace[i][2])
        bArr.append(backFace[i][0])
        dArr.append(downFace[i][2])
    temp = fArr
    if(inv):
        fArr = uArr
        uArr = list(reversed(bArr))
        bArr = list(reversed(dArr))
        dArr = temp
    else:
        fArr = dArr
        dArr = list(reversed(bArr))
        bArr = list(reversed(uArr))
        uArr = temp
    for i in range(0,3):
        frontFace[i][2] = fArr[i]
        upFace[i][2] = uArr[i]
        backFace[i][0] = bArr[i]
        downFace[i][2] = dArr[i]

def left(inv = False):
    rotate(leftFace, inv)
    fArr = []
    uArr = []
    bArr = []
    dArr = []
    for i in range(0,3):
        fArr.append(frontFace[i][0])
        uArr.append(upFace[i][0])
        bArr.append(backFace[i][2])
        dArr.append(downFace[i][0])
    temp = fArr
    if(not inv):
        fArr = uArr
        uArr = list(reversed(bArr))
        bArr = list(reversed(dArr))
        dArr = temp
    else:
        fArr = dArr
        dArr = list(reversed(bArr))
        bArr = list(reversed(uArr))
        uArr = temp
    for i in range(0,3):
        frontFace[i][0] = fArr[i]
        upFace[i][0] = uArr[i]
        backFace[i][2] = bArr[i]
        downFace[i][0] = dArr[i]

def up(inv = False):
    rotate(upFace, inv)
    temp = frontFace[0]
    if (inv):
        frontFace[0] = leftFace[0]
        leftFace[0] = backFace[0]
        backFace[0] = rightFace[0]
        rightFace[0] = temp
    else:
        frontFace[0] = rightFace[0]
        rightFace[0] = backFace[0]
        backFace[0] = leftFace[0]
        leftFace[0] = temp


def down(inv = False):
    rotate(downFace, inv)
    temp = frontFace[2]
    if (inv):
        frontFace[2] = rightFace[2]
        rightFace[2] = backFace[2]
        backFace[2] = leftFace[2]
        leftFace[2] = temp
    else:
        frontFace[2] = leftFace[2]
        leftFace[2] = backFace[2]
        backFace[2] = rightFace[2]
        rightFace[2] = temp

def front(inv = False):
    rotate(frontFace, inv)
    rArr = []
    uArr = upFace[2]
    lArr = []
    dArr = downFace[0]
    for i in range(0,3):
        rArr.append(rightFace[i][0])
        lArr.append(leftFace[i][2])
    temp = rArr
    if (inv):
        rArr = list(reversed(dArr))
        dArr = lArr
        lArr = list(reversed(uArr))
        uArr = temp
    else:
        rArr = uArr
        uArr = list(reversed(lArr))
        lArr = dArr
        dArr = list(reversed(temp))
    upFace[2] = uArr
    downFace[0] = dArr
    for i in range(0,3):
        rightFace[i][0] = rArr[i]
        leftFace[i][2] = lArr[i]

def back(inv = False):
    rotate(backFace, inv)
    rArr = []
    uArr = upFace[0]
    lArr = []
    dArr = downFace[2]
    for i in range(0,3):
        rArr.append(rightFace[i][2])
        lArr.append(leftFace[i][0])
    temp = rArr
    if (not inv):
        rArr = list(reversed(dArr))
        dArr = lArr
        lArr = list(reversed(uArr))
        uArr = temp
    else:
        rArr = uArr
        uArr = list(reversed(lArr))
        lArr = dArr
        dArr = list(reversed(temp))
    upFace[0] = uArr
    downFace[2] = dArr
    for i in range(0,3):
        rightFace[i][2] = rArr[i]
        leftFace[i][0] = lArr[i]

def shuffle(num = 20):
    for i in range(0,num):
        n = random.randint(0,5)
        choice = random.choice([True,False])
        if (choice):
            state = (' inv')
        else:
            state = ''
        if (n == 0):
            print('right' + state)
            right(choice)
        if (n == 1):
            print('left' + state)
            left(choice)
        if (n == 2):
            print('up' + state)
            up(choice)
        if (n == 3):
            print('down' + state)
            down(choice)
        if (n == 4):
            print('front' + state)
            front(choice)
        if (n == 5):
            print('back' + state)
            back(choice)

print (cube)
shuffle()
print (cube)
i = 0

while (cube != finished):
    shuffle(1)
    i += 1
    print (i)
print (cube)
