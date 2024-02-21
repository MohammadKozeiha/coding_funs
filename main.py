# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def function(n):
    if n>0:
        m=range(1,n+1)
    else:
        m=range(n,-1)
    for i in m:
        if i%2==0:
            return i
    return n
def func(x):
    if x==1:
        return 1
    elif x%2==0:
        return 2*func(x/2)
    else:
        return 3*func(x-1)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    for i in range(5):
        for j in range(i):
            if j%2==0:
                print(j)



def f(x=100, y=200):
    return (x+y, x-y)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(func(2))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    a='hello world'
    print(a.replace('world', 'le monde'))
    res = ""
    for i in [1,2,3,4,5,6,7,8]:
        res += "i"
    print(res)
    print(function(-10))
    numbers =[1,2,3,4,6,5]
    for n in numbers:
        strings=""
        for i in range(n):
            strings+="x"
        print(strings)

list2 = numbers.copy()
for i in list2:
    if list2.count(i)>1:
        list2.pop(i)
print(list2.index(3)%2==0)
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y=y
    def __eq__(self, other):
        return(self.x, self.y) == (other.x, other.y)
x =1
y=2
point = Point(x,y)
print('toto'.find('u'))
print('toto'.find('u'))
print('toto'.find('u'))
print(2*2**3)
print(f(y=200, x=100))
print((20//3))


