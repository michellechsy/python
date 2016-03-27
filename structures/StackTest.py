from structures.Stack import Stack


s = Stack()

print("Created empty stack:", s.isEmpty())
s.push(1)
s.push('dog')
print("Peek:", s.peek())
s.push(True)
print("Stack size:", s.size())
print("Stack is empty:", s.isEmpty())
print(s.pop())
print(s.pop())
print(s.pop())
print("Stack size:", s.size())
# print(s.pop())
