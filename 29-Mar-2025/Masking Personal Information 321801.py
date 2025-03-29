# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:

        if "@" in s:  # Email case
            name, domain = s.split("@")
            return (name[0] + "*****" + name[-1] + "@" + domain).lower()
            
        # Phone number case
        digits = [c for c in s if c.isdigit()]
        local_number = "***-***-" + "".join(digits[-4:])
        country_code_length = len(digits) - 10

        if country_code_length == 0:
            return local_number
        return "+" + "*" * country_code_length + "-" + local_number
            