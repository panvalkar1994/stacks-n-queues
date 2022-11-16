class EmptyStackError:
    pass



class Stack:
    TOP = -1

    def __init__(self) -> None:
        self._stack = []

    def pop(self):
        if self.is_empty():
            raise EmptyStackError()
        return self._stack.pop()
    
    def push(self, item):
        self._stack.append(item)

    def is_empty(self):
        return len(self._stack) == 0
    
    def peek(self):
        if self.is_empty():
            raise EmptyStackError()
        return self._stack[Stack.TOP]

    