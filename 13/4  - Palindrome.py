def isPalindrome(S):
   for i in range(len(S)//2):
      if S[i] != S[len(S)-i-1]:
         return False
   return True
