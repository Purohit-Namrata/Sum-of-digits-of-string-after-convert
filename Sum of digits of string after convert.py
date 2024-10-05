
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numeric_string = ''.join(str(ord(char) - ord('a') + 1) for char in s)
      
        for _ in range(k):
            sum_of_digits = sum(int(digit) for digit in numeric_string)
            numeric_string = str(sum_of_digits)
      
        return int(numeric_string)

s=Solution()
print(s.getLucky("iiii",1))