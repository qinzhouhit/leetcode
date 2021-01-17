'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# O(N) for S and T, N as length of cpdomains
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []
        h = collections.defaultdict(int)
        for item in cpdomains:
            attrs = item.split(" ")
            ct = int(attrs[0])
            domains = attrs[1].split(".")
            for i in range(len(domains)):
                tmp = ".".join(domains[i:])
                h[tmp] += ct
        res = []
        for k, ct in h.items():
            res.append(str(ct) + " " + k)
        return res
            

    ##### without using split function
    def split_string(string, char):
        split_value = []
        tmp = ''
        for c in string:
            if c == char:
                split_value.append(tmp)
                tmp = ''
            else:
                tmp += c
        if tmp:
            split_value.append(tmp)
        return split_value  
    
    domain_map = defaultdict(int)
    for cpdomain in cpdomains:
        count, domain = split_string(cpdomain, ' ')
        count = int(count)
        domains = split_string(domain, '.')
        for i in range(len(domains)):
            domain_map['.'.join(domains[i:])] += count
    return ['{} {}'.format(v, k) for k, v in domain_map.items()]


    ##### official
    def subdomainVisits1(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in xrange(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]