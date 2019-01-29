class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        
        name = "saeed", typed = "ssaaedd"
        """
        if len(typed) < len(name):
            return False
        
        if len(typed) == len(name):
            return typed == name
        next_letter = 0
        
        for j in range(len(typed)):
            if typed[j] == name[next_letter]:
                next_letter += 1
            
            if next_letter == len(name):
                break
            
        return not next_letter < len(name)