from stack import Stack

class MinStack(Stack):

    def __init__(self) -> None:
        super().__init__()

    def push(self, item):
        if self.is_empty():
            self._stack.append((item, item))
            return
        _min, _ = self.peek()
        _min = min(_min, item)
        self._stack.append((_min, item))
    
    def minval(self):
        return self.peek()[0]


st = MinStack()

data = [4,5, 3, 2, 6, -1, 11, 7]

for d in data:
    st.push(d)

while not st.is_empty():
    m, v = st.pop()
    print(f'min:{m} and val:{v}')
