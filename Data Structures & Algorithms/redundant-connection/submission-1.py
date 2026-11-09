class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [x for x in range(len(edges) + 1)] #1 indexed

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x 

        def union(x, y):
            if find(x) != find(y):
                parent[find(y)] = find(x)
        
        removed = []

        for u, v in edges:
            ru, rv = find(u), find(v)

            if(ru == rv):
                removed.append([u,v])
            else:
                union(u, v)

        return removed[-1]