class Stack:
    def __init__(self):
        self.q1 = []
        self.index_q1 = -1
        top = None

    def push(self,val):
        self.q1.append(val)
        self.index_q1 += 1
        top = val

    def pop(self):
        if (self.index_q1 != -1):
            top = self.q1[self.index_q1]
            self.index_q1 -= 1
            return top

    def isEmpty(self):
        if len(self.q1) == 0 and len(self.q2) == 0:
            return True
        else:
            return False

    def isFull(self):
        return self.index_q1 == self.size - 1

if __name__ == '__main__':
    s = Stack()
    s.push(3)
    s.push(4)
    print (s.pop())
