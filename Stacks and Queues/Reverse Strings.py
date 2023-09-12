from queue import LifoQueue

text = input()
stack = LifoQueue()

for letter in text:
    stack.put(letter)

for _ in range(stack.qsize()):
    print(stack.get(), end="")