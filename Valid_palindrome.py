import re

def validPalindrome(s):
    s = re.sub(r'\W+', '', s)
    print(s)
    if s.lower() == s.lower()[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    s = 'ab_a'
    print(validPalindrome(s))