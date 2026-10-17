class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = [i for i in range(len(accounts))]
        rank = [0 for _ in range(len(accounts))]

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            rx, ry = find(u), find(v)
            if rx == ry: return False 
            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[ry] = rx
                rank[rx] += 1

            return True 

        emails_to_accounts = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emails_to_accounts:
                    union(emails_to_accounts[email], i)
                    continue 

                emails_to_accounts[email] = i 

        groups = defaultdict(list)
        for email, account in emails_to_accounts.items():
            leader = find(account)
            groups[leader].append(email)

        return [[accounts[leader][0]] + sorted(emails) for leader, emails in groups.items()]


