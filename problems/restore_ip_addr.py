class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        
        
          2           25           255
     /   |  \        / | \
   5     55  552    5  52 525
          
        """
        self.valids = []
        
        self._restore_ips(0, "", 0, s)
        
        return self.valids
    
    
    def _restore_ips(self, start_index, curr_ip, curr_pos, s):
        if curr_pos == 4:
            if start_index >= len(s):
                self.valids.append(curr_ip)
            return
        

        leading_zero = False
        next_ip_token = ""
        for i in range(start_index, start_index+3):
            
            if i < len(s) and not leading_zero:
                next_ip_token += s[i]
                if int(next_ip_token) <= 255:
                    new_ip = curr_ip + "." + next_ip_token if len(curr_ip) > 0 else next_ip_token
                    self._restore_ips(i+1, new_ip, curr_pos+1, s)
            
            if start_index < len(s) and s[start_index] == '0':
                leading_zero = True