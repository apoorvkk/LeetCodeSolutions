class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        
        ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        
        "test.email+alex@leetcode.com"
        
        (testemail, leetcode.com)
        """
        
        uniq_emails = set()
        
        for email in emails:
            local_name, domain = email.split('@')
            strp_local_name = self._parse_local_name(local_name)
            
            uniq_emails.add((strp_local_name, domain))
        
        return len(uniq_emails)
    
    def _parse_local_name(self, local_name):
        new_name = ""
        
        for char in local_name:
            if char == '.':
                continue
            if char == '+':
                break
            
            new_name += char
        
        return new_name