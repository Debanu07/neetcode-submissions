class MinStack:

    def __init__(self):
        self.l=[]
        self.ml=[]

    def push(self, val: int) -> None:
        self.l.append(val)
        if len(self.ml)==0:
            self.ml.append(val)
        else:
            self.ml.append(min(self.ml[-1],val))
    def pop(self) -> None:
        self.l.pop()
        self.ml.pop()
    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.ml[-1]
