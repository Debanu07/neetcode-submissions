class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.n1,self.k=nums,k
        heapq.heapify(self.n1)
        while len(self.n1)>k:
            heapq.heappop(self.n1)

    def add(self, val: int) -> int:
        heapq.heappush(self.n1, val)
        if len(self.n1) > self.k:
            heapq.heappop(self.n1)
        return self.n1[0]
