from queue import LifoQueue as Stack

text = input()
stack = Stack()
for index in range(len(text)):
    if text[index] == "(":
        stack.put(index)
    if text[index] == ")":
        print(text[stack.get():index+1])
