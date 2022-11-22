from stack import Stack

class SortedStack(Stack):

    def __init__(self):
        super().__init__()

    def push(self, item):
        helper_stack = Stack()
        while not self.is_empty():
            if self.peek()>item:
                break
            helper_stack.push(self.pop())
        super(SortedStack, self).push(item)
        while not helper_stack.is_empty():
            top = helper_stack.pop()
            super(SortedStack, self).push(top)

    
# data = [3, 6, 2, 5, 1, 4]
# ss = SortedStack()

# for d in data:
#     ss.push(d)

# while not ss.is_empty():
#     item = ss.pop()
#     print(item, end=", ")
# print('')



    
    