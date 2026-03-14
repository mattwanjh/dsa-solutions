class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_options = 3 * pow(2, n - 1)
        result = []
        
        # impossible to have results
        if k > total_options:
            return ""

        # adjust for 0 indexing
        k -= 1

        # first selection, three options
        boundary = pow(2, n - 1)
        choice = k // boundary # 0, 1, 2
        if choice == 0:
            result.append("a")
        elif choice == 1:
            result.append("b")
        else:
            result.append("c")

        k -= choice * boundary
        n -= 1

        # remaining selections
        while n:
            boundary = pow(2, n - 1)
            choice = k // boundary # 0, 1

            if choice == 0:
                if result[-1] != "a":
                    result.append("a")
                else:
                    result.append("b")
            else: 
                if result[-1] != "c":
                    result.append("c")
                else:
                    result.append("b")

            k -= choice * boundary
            n -= 1

        
        return "".join(result)