class Solution:
    def wordPatternMatch(self, pattern, text):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        {
            "a": asd
         }
         
         asdasdasd
            3   
            ""        
        """
        return self._find_match(pattern, text, 0, 0, {}, set())
    
    def _find_match(self, pattern, text, start_text, curr_pattern_index, pattern_mapping, used_patterns):
        if start_text >= len(text):
            return curr_pattern_index >= len(pattern)
        if curr_pattern_index >= len(pattern):
            return start_text >= len(text)    
        
        if pattern[curr_pattern_index] not in pattern_mapping: # select a prefix            
            prefix = ""
            for i in range(start_text, len(text)):
                prefix += text[i]
                if prefix in used_patterns:
                    continue
                    
                pattern_mapping[pattern[curr_pattern_index]] = prefix
                used_patterns.add(prefix)
                
                if self._find_match(pattern, text, i+1, curr_pattern_index+1, pattern_mapping, used_patterns):
                    return True
                
                used_patterns.remove(prefix)
                del pattern_mapping[pattern[curr_pattern_index]] 
        else:
            expected_prefix = pattern_mapping[pattern[curr_pattern_index]]
            if start_text+len(expected_prefix) > len(text):
                return False
            prefix = text[start_text: start_text+len(expected_prefix)]

            if prefix == expected_prefix:
                return self._find_match(pattern, text, start_text+len(expected_prefix), curr_pattern_index+1, pattern_mapping, used_patterns)
        
        return False
            
            
        