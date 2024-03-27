class Stack:

    def __init__(self, items = [], limit = 100):
        if len(items) <= limit:
            self.items = items
            self.limit = limit
        pass

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        pass

    def push(self, item):
        if self.full():
            return "Stack is full"
        else:
            self.items.append(item)
            return self
        pass

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()
        pass

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)
        pass

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False        
        pass

    def search(self, target):
        for index,value in enumerate(self.items,1):
            if value == target:
                return len(self.items) - index
        return -1    
        pass

