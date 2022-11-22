class QueueNode:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:

    def __init__(self) -> None:
        self._first = None
        self._last = None

    def add(self, item):
        node = QueueNode(item)
        if self._last is not None:
            self._last.next = node
        self._last = node
        if self._first is None:
            self._first = self._last

    def remove(self):
        if self._first is None:
            raise EmptyQueueException
        data = self._first.data
        self._first = self._first.next
        if self._first is None:
            self._last = None
        return data

    def peek(self):
        if self._first is None:
            raise EmptyQueueException
        return self._first.data

    def is_empty(self):
        return self._first is None


class EmptyQueueException(Exception):
    pass
