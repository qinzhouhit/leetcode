'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


class Solution:

	# O(C) for S and T, C as total content of emails
	# https://leetcode.com/problems/unique-email-addresses/discuss/186798/JavaPython-3-7-and-6-liners-with-comment-and-analysis.
	def numUniqueEmails(self, emails: List[str]) -> int:
		seen = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)


	# self-made
    def numUniqueEmails(self, emails: List[str]) -> int:
        def local_name_convert(s):
            local, domain = s.split("@")
            tmp = []
            for c in local:
                if c == '.':
                    continue
                elif c == '+':
                    break
                tmp.append(c)
            return ''.join(tmp) + '@' + domain
        
        res = set([])
        for email in emails:
            email_con = local_name_convert(email)
            res.add(email_con)
        # print (res)
        return len(res)