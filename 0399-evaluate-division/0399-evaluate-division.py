from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Step 1: Build the directed weighted graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations , values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        # Step 2: DFS function to find path product from start to target
        def dfs(curr, target, product, visited):
            if curr == target:
                return product

            visited.add(curr)

            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    res = dfs(neighbor, target, product * weight, visited)
                    if res != -1.0:
                        return res

            return -1.0
        
        # Step 3: Evaluate each query
        results = []
        for src, dst in queries:
            if src not in graph or dst not in graph:
                results.append(-1.0)
            elif src == dst:
                results.append(1.0)
            else:
                results.append(dfs(src, dst, 1.0, set()))
        return results