# ex8-1,ex8-2は省略
# ex8-3
a = input('数字を入力')
c = int(a)
if c%2 == 0:
    print("偶数")
else:
    print("奇数")

# ex8-4
a = input('input')
if a == '朝':
    print('おはよう')
elif a == '昼':
    print('こんにちは')
elif a == '夜':
    print('こんばんは')
else:
    print('わからないよ')

# ex8-6
x = input('pass->')
y = len(x)

if y < 8:
    print('短すぎるよ！')

# ex8-7
m = input('月')
m1 = int(m)

if m1 == 2:
    print("29日")
elif m1 == 1 or m1 == 3 or m1 == 5 or m1 == 7 or m1 == 8 or m1 == 12 or m1 == 10:
    print("31日")
elif m1 == 4 or m1 == 6 or m1 == 9 or m1 == 11:
    print('30日')
else:
    print('そんな月ありません')

# ex8-8
kg = input("体重は(kgで)？")
kg1 = float(kg)
m = input("身長は(mで)？")
m1 = float(m)

bmi = kg1/(m1**2)

print(bmi)

if bmi < 18.5:
    print('低体重')
elif 18.5 <= bmi < 25.0:
    print('標準')
elif 25.0 <= bmi < 30.0:
    print('太り気味')
else:
    print('肥満')

# ex8-9
import math
e = input('係数a')
f = input('係数b')
g = input('係数a')

a = int(e)
b = int(f)
c = int(g)

dm = b*b - 4*a*c
if dm >= 0:
    kai1 = (-b+math.sqrt((b**2)-4*a*c)) / 2*a
    kai2 = (-b-math.sqrt((b**2)-4*a*c)) / 2*a

    print(int(kai1))
    print(int(kai2))
else:
    print('実数解を持ちません')

# ex 8-11
x = input('西暦年を入力')
y = int(x)
if y%4 == 0:
    if y%100 != 0 or y%400 == 0:
        print('閏年')
    else:
        print("閏年じゃない")
else:
        print('閏年じゃない')

# ex8-12
x = input('数字を入力')
y = int(x)

if y%2 == 0 or y%3 == 0:
    if y%2 == 0 and y%3 == 0:
        print('6の倍数')
    if y%2 == 0 and y%3 != 0:
        print('2の倍数')
    if y%2 != 0 and y%3 == 0:
        print('3の倍数')
else:
    print('その他')

# ex8-13
# [start:step]とすると、start <= x < stopの範囲の文字列が抽出できる。
s = input('ログイン名？')
print(s[0])
print(s[1:3])

if s[0] == 's':
    if s[1:3] <= '89':
        print('総合政策20%s年度入学' % s[1:3])
    else:
        print('総合政策19%s年度入学' % s[1:3])

elif s[0] == 't':
    if s[1:3] <= '89':
        print('環境情報20%s年度入学' % s[1:3])
    else:
        print('環境情報19%s年度入学' % s[1:3])

elif s[0] == 'i':
    if s[1:3] <= '89':
        print('看護医療20%s年度入学' % s[1:3])
    else:
        print('看護医療19%s年度入学' % s[1:3])
else:
    print('error')


# ex8-14
c = input('お名前は？')
print('こんにちは、名無しさん') if c == "" else print('こんにちは,'+c)

# ex8-15
c = input('お名前は?')
if c or "":
    print('こんにちは,'+c)
else:
    print('こんにちは、名無しさん')
