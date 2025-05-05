from collections import defaultdict

def kosaraju(graph, functions):
    visited = set()
    order = []
    reverse = defaultdict(list)
    
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for u in graph[node]:
                dfs(u)
            order.append(node)

    for func in functions:
        if func not in visited:
            dfs(func)
    
    for u in graph:
        for v in graph[u]:
            reverse[v].append(u)
    
    visited.clear()
    sccs = []
    
    for func in reversed(order):
        if func not in visited:
            stack = [func]
            visited.add(func)
            scc = []
            while stack:
                node = stack.pop()
                scc.append(node)
                for n in reverse.get(node, []):
                    if n not in visited:
                        visited.add(n)
                        stack.append(n)
            sccs.append(scc)
    
    return sccs

#data = input()

data = '''
foo: bar, baz, qux
bar: baz, foo, bar
qux: qux
'''

graph = defaultdict(list)
functions = set()
for line in data.split('\n'):
    if not line.strip():
        continue
    func, deps = line.split(':')
    func = func.strip()
    functions.add(func)
    deps = [dep.strip() for dep in deps.split(',')]
    for dep in deps:
        graph[func].append(dep)

sccs = kosaraju(graph, functions)
    
max_scc = max(sccs, key=lambda x: len(x)) if sccs else []
recursive = []
for scc in sccs:
    if len(scc) > 1 or (len(scc) == 1 and scc[0] in graph.get(scc[0], [])):
        recursive.extend(scc)

print(*max_scc)
print(*recursive)

