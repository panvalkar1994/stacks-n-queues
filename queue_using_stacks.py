from stack import Stack

class MyQueue:

    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()

    def add(self, item):
        self._in_stack.push(item)

    def remove(self):
        if self._out_stack.is_empty():
            self._transfer()
        return self._out_stack.pop()

    def _transfer(self):
        while not self._in_stack.is_empty():
            item = self._in_stack.pop()
            self._out_stack.push(item)

    def peek(self):
        if self._out_stack.is_empty():
            self._transfer()
        return self._out_stack.peek()

    def is_empty(self):
        if self._out_stack.is_empty():
            self._transfer()

        return self._out_stack.is_empty()






