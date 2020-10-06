'''keys: Solutions:Similar: T:S:'''from typing import Listimport collectionsimport itertoolsclass Solution:    # T: O(R*C^2), R and C as rows and cols    # S: O(C^2)    # for each row, find a pair of ones, for another row, if corresponding     # pair of ones found, then found a rectangle    def countCornerRectangles(self, grid: List[List[int]]) -> int:        h = collections.defaultdict(int)        res = 0        for row in grid:            for c1, val in enumerate(row):                if val:                    for c2 in range(c1+1, len(row)):                        if row[c2]:                            res += h.get((c1, c2), 0)                            h[(c1, c2)] += 1        return res        # T: O(N*sqrt(N) + R*C)    # S: O(N + R + C^2)    def countCornerRectangles1(self, grid):        rows = [[c for c, val in enumerate(row) if val]                for row in grid]        N = sum(len(row) for row in grid)        SQRTN = int(N**.5)        ans = 0        count = collections.Counter()        for r, row in enumerate(rows):            if len(row) >= SQRTN:                target = set(row)                for r2, row2 in enumerate(rows):                    if r2 <= r and len(row2) >= SQRTN:                        continue                    found = sum(1 for c2 in row2 if c2 in target)                    ans += found * (found - 1) / 2            else:                for pair in itertools.combinations(row, 2):                    ans += count[pair]                    count[pair] += 1        return ans