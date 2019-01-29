import functools

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        number_logs, text_logs = [], []
        
        for log in logs:
            if log[-1].isdigit(): 
                number_logs.append(log)
            else:
                text_logs.append(log)
                
        # sort text logs
        def sort_logs(log_one, log_two):
            log_one_id = log_one.split(' ')[0]
            log_two_id = log_two.split(' ')[0]
            
            l1, l2 = log_one[len(log_one_id):], log_two[len(log_two_id):]
            if l1 < l2:
                return -1
            elif l1 > l2:
                return 1
            else:
                if log_one_id < log_two_id:
                    return -1
                elif log_one_id > log_two_id:
                    return 1
                else:
                    return 0
                
        text_logs.sort(key=functools.cmp_to_key(sort_logs))
        
        
        return text_logs + number_logs