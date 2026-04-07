class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # checks to see if splitting the dots results in a valid IP address 
        # no leading 0
        # no numbers > 255
        def isValid(s, start, end) -> bool:
            ip = s[start:end]
            if ip[0] == "0" and len(ip) > 1:
                return False
            
            if int(ip) > 255:
                return False
            
            return True

        if len(s) > 12 or len(s) < 4: return []
        # the location where dots should appear
        a, b, c = 1, 2, 3
        ans = []
        # make sure that we don't exceed possible lengths
        # filtering possile placements
        while a <= 3 and isValid(s, 0, a):
            b = a + 1
            while b - a <= 3 and isValid(s, a, b):
                c = b + 1
                while c - b <= 3 and c < len(s) and isValid(s, b, c):
                    if len(s) - c <= 3 and isValid(s, c, len(s)):
                        ans.append(s[:a] + "." + s[a:b] + "." + s[b:c] + "." + s[c:])
                    c += 1
                b += 1
            a += 1
        return ans

            
        
"""
number of possible good values (3 ^ 3)
Runtime: O(3^4)
Time: O(1)
"""
