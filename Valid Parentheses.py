#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.




class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2!=0:
            return False
        
        my_dict = {'(':')','{':'}','[':']'}
        stack = []
        
        for i in range(len(s)):
            
            if s[i] in my_dict.keys():
                stack.append(s[i])
                continue

            if len(stack)==0 and s[i] not in my_dict.keys():
                return False
            
            prev = stack.pop()
            
            if my_dict[prev] != s[i]:
                return False
        
        if len(stack)>0:
            return False
        
        return True
