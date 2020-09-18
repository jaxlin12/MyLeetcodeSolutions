#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def ipaddress(self, s, n):
        if s == "":
            return []
        if n == 3:
            if len(s) > 3 or int(s) > 255 or (int(s) == 0 and len(s) != 1) or (s[0] == "0" and int(s) != 0):
                return []
            else:
                return [s]

        ret = []
        if s[0] == "0":
            result = self.ipaddress(s[1:], n+1)
            for sol in result:
                ret.append("0." + sol)
            return ret

        result = self.ipaddress(s[1:], n+1)
        for sol in result:
            ret.append(s[:1] + '.' + sol)

        result = self.ipaddress(s[2:], n+1)
        for sol in result:
            ret.append(s[:2] + '.' + sol)

        if 0< int(s[0:3]) < 256:
            result = self.ipaddress(s[3:], n+1)
            for sol in result:
                ret.append(s[:3] + '.' + sol)
        return ret
            
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.ipaddress(s, 0)
        
# @lc code=end

