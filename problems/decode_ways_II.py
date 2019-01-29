class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) > 0 and s[0] == '0') or len(s) == 0:
            return 0
        lookup = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        prev = 1
        curr = None
        if s[0].isdigit():       
            curr = 1
        else:
            curr = 9
        
        for i in range(2, len(s)+1):
            last_digit = s[i-1]
            second_last_digit = s[i-2]
            new_total = 0
            
            # last digit
            if last_digit.isdigit() and 1 <= lookup[last_digit] <= 9:
                new_total += curr
            
            elif last_digit == '*':
                new_total += curr * 9
                
            # last two digits
            if last_digit.isdigit() and second_last_digit.isdigit():
                if 10 <= lookup[second_last_digit] * 10 + lookup[last_digit] <= 26:
                    new_total += prev
            
            elif last_digit == '*' and second_last_digit == '*':
                new_total += prev * 15
            
            elif second_last_digit == '*' and last_digit.isdigit():
                if 0 <= lookup[last_digit] <= 6:
                    new_total += prev * 2
                else:
                    new_total += prev
                
            elif second_last_digit.isdigit() and last_digit == '*':
                if lookup[second_last_digit] == 1:
                    new_total += prev * 9
                elif lookup[second_last_digit] == 2:
                    new_total += prev * 6
            
            prev = curr
            curr = new_total
        
        return curr % (10**9 + 7)
       