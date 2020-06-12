# ex1
print('Hello, world!')

# ex2
print(365*24*60*60)

# ex3
print("みなさん、こんにちは")

# ex4
print('Hello, ')
print('world!')

# ex05
x = 1
x = x*2
x = x*2
x = x*2
print(x)

#ex6
a1 = len('horse')
a2 = len('elephant')
a3 = len('hippopotamus')
a4 = len('dolphin')

print(max(a1,a2,a3,a4))

# ex7
b = input('数値を入力')
b_num = int(b)
print(b_num+1)

# ex8
c = input('お名前は？')
print('こんにちは,'+c)

# ex9
d1 = input('number1->')
d2 = float(d1)
d3 = input('number2->')
d4 = float(d3)

wa = d2+d4
sa = d2-d4
seki = d2*d4
shou = d2/d4
print(wa,sa,seki,shou)

# ex10
kg = input("体重は(kgで)？")
kg1 = float(kg)
m = input("身長は(mで)？")
m1 = float(m)

bmi = kg1/(m1**2)

print(bmi)

# ex11
import math
e = input('係数a')
f = input('係数b')
g = input('係数a')

a = int(e)
b = int(f)
c = int(g)

kai1 = (-b+math.sqrt((b**2)-4*a*c)) / 2*a
kai2 = (-b-math.sqrt((b**2)-4*a*c)) / 2*a


print(int(kai1))
print(int(kai2))

# ex12
import datetime

now = datetime.datetime.today()

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond

print(year,'年',month,'月',day,'日',hour,'時',minute,'分')  # 2018

# ex13
h = input('number1->')
r = input('number2->')
j = input('number3->')
k = input('number4->')

a = int(h)
b = int(r)
c = int(j)
d = int(k)

e = complex(a,b);
f = complex(c,d);
wa = e+f
sa = e-f
seki = e*f
shou = e/f

print(wa,sa,seki,shou)
