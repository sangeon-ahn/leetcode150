class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        dic = {1:"I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

        idx = len(nums) - 1
        symbols = []
        while idx >= 0:
            if nums[idx] <= num:
                symbols.append(dic[nums[idx]])
                num -= nums[idx]
            else:
                idx -= 1
        
        ans = ''.join(symbols)

        return ans

sol = Solution()
ans = sol.intToRoman(1994)

            