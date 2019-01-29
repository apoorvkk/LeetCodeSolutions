class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self._is_interleave(s1, s2, s3, set(), 0, 0, 0)

    
    def _is_interleave(self, s1, s2, s3, memo, s1_start, s2_start, s3_start):
        if s3_start >= len(s3):
            return s1_start >= len(s1) and s2_start >= len(s2)
        
        encoding = str(s1_start) + '|' + str(s2_start) + '|' + str(s3_start)
        if encoding in memo:
            return False

        s1_counter = s1_start if s1_start < len(s1) else None
        s2_counter = s2_start if s2_start < len(s2) else None
        
        
        def _find_prefix(counter, p, other_start):
            for i in range(s3_start, len(s3)):
                if counter is not None:
                    if s3[i] == p[counter]:
                        if s1 == p:
                            if self._is_interleave(s1, s2, s3, memo, counter+1, other_start, i+1):
                                return True
                        else:
                            if self._is_interleave(s1, s2, s3, memo, other_start, counter+1, i+1):
                                return True
                        counter += 1
                    else:
                        counter = None

                if counter is not None and counter >= len(p):
                    counter = None
        
        if _find_prefix(s1_counter, s1, s2_start):
            return True
        if _find_prefix(s2_counter, s2, s1_start):
            return True
        
        memo.add(encoding)
        return False
        