class StockSpanner:

    def __init__(self):
        self.stack=[] #each pair=(price,span)
    def next(self, price: int) -> int:
        span=1 #by default
        while self.stack and self.stack[-1][0]<=price: #here [-1] is the top most ele of stack and [0] is the span
            span+=self.stack[-1][1] 
            self.stack.pop()
        self.stack.append((price,span))
        return span
            
            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)