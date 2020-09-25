a = []
def enqueue(element):
    a.append(element)
    print(f"{element} was sucessfully enqueued")

def dequeue():
    if len(a) == 0:
        print("list is empty")
    else:
        c = a.pop(0)
        print(f"{c} was sucessfully dequeued")

def display_queue():
    for i in range(0,len(a)):
        print(a[i])

enqueue(21)
enqueue(31)
enqueue(41)
enqueue(51)
display_queue()
dequeue()
dequeue()
dequeue()
dequeue()
display_queue()
enqueue(61)
enqueue(71)
enqueue(81)
enqueue(91)
display_queue()
dequeue()
dequeue()
display_queue()