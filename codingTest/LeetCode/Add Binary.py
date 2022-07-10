class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        a_dec = 0
        A = int(a)
        for l in range(len(a)):
            next = A//10
            now = A%10
            a_dec += (now*pow(2,l))
            A = next
        b_dec = 0
        B = int(b)
        for l in range(len(b)):
            next = B//10
            now = B%10
            b_dec += (now*pow(2,l))
            B = next
        total = a_dec + b_dec
        result = ""
        while True:
            if total == 0:
                break
            next = total//2
            result = (str(total%2)+result)
            total = next
        return result
            
            
            
