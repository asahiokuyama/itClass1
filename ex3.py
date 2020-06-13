# ex9-1
for i in range(1,11):
    print(str(i)+'回目の処理')
print('終了')

# ex9-2
for i in range(1,10):
    if i%2 == 0:
        print(str(i)+'は偶数です。')
    elif i%2 != 0:
        print(str(i)+'は奇数です。')

# ex9-3
s = 0
i = 1
while(i<=100):
    s = s+i
    i = i+1
print(s)

# ex9-4
y = 0
while y < 8:
    x = input('パスワード（８文字以上）')
    y = len(x)
    if y < 8:
        print('短すぎ')

# ex9-5
a = input('文字列')
x = len(a)
s = 0
h = 0
for i in range(x):
    if 'A' <= a[i] <= 'Z':
        s = s+1
    if 'a' <= a[i] <= 'z':
        h = h+1

print('大文字は%d個' % s)
print('小文字は%d個' % h)

# ex9-6
x = 0
y = 1
while y > 0:
    a = input('number')
    y = int(a)
    x = x+y
print(x)

# ex9-7-1
a = 0
for i in range(1,100,2):
    a = a+i
print(a)

# ex9-7-2
a = 0
for i in range(1,100):
    if i%2 != 0:
        a = a+i
print(a)

# ex9-7-3
a = 0
i = 0
while i<100:
    if i%2 != 0:
        a = a+i
    i = i+1;
print(a)

# ex9-8
a = input('number')
x = int(a)
j = 0
for i in range(1,x+1):
    if x%i == 0:
        j = j+1
print(j)

# ex9-9 １ずつずらすアスキーコード
a = input('文字列')
x = len(a)
c = ""
for i in range(x):
    b = ord(a[i])
    b = b+1
    c += chr(b)
print(c)

# ex9-10
a = input('number')
x = int(a)

for i in range(2,x-1):
    if x%i == 0:
        print('素数ではありません')
        break
else:
    print('素数です')
