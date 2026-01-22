class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_string = str(abs(x))[::-1];
        reverse_num = int(reverse_string);
        return True if reverse_num == x else False;