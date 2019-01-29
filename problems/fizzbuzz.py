class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def fizz_val(i):
            if i % 3 == 0 and i % 5 == 0:
                return "FizzBuzz"
            elif i % 3 == 0:
                return "Fizz"
            elif i % 5 == 0:
                return "Buzz"
            return str(i)
        return [fizz_val(i) for i in range(1, n+1)]
            