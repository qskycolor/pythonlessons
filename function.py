

def f1(x):
    t = 2 * x + 1
    print(t)

f1(2)
s = type(f1)
print(s)
print(type(s))


def add(*num):
	print(num)
	result = 0
	for n in num:
		result = result + n
	return result

res = add(1,2,3,4,5)
print(res)

def register(name,sex=1,**kw):
    print(name, sex, kw)

register('Tom', address='上海', job='程序员')

register(name='kite',sex=0)

print(register.__annotations__)


def func(*args, **kw):
    print(args, kw)

func(1, 2, 3, name='Jack', age='18', address='New York')

def fn(name: str, age: int) -> str:
    print(name,age)
    return 'name:%s,age:%s' % (name, age)

print(fn('John', 19))
print('*' * 40)
print('Please input your name:')
name = input()
print('Please input your age:')
age = input()
print('Your name is %s, age is %s' % (name, age))





