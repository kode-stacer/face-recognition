a = []

def push(element):
    a.append(element)

def pull():
    if len(a) == 0:
        print("List is empty")
    else:
        c = a.pop()
        print(c)

def display_stack():
    for i in range(len(a)-1, -1, -1):
        print(a[i])

push(21)
display_stack()
print(a)
push(32)
display_stack()
print(a)
pull()
display_stack()
print(a)
push(31)
display_stack()
print(a)
push(35)
display_stack()
print(a)
pull()
display_stack()
print(a)