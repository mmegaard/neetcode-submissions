class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        second = len(s) - 1
        while first <= second:
            firstChar = s[first].lower()
            secondChar = s[second].lower()
            if not firstChar.isalnum():
                first += 1
                continue
            if not secondChar.isalnum():
                second -= 1
                continue
            print('p1 -> ', firstChar, 'p2 -> ', secondChar )
            if first != second and firstChar != secondChar:
                return False
            first += 1
            second -= 1
        return True
