


def palindrome(text):
   left = 0
   right = len(text) -1

   while left < right:
       while left < right and not text[left].isalnum():
           left +=1
       while left < right and not text[right].isalnum():
           right -=1
       if text[left].lower() != text[right].lower():
           return False

       left +=1
       right -=1

   print True

print palindrome("A man, a plan, a canal: Panama")
