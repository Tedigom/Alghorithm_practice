graph = {'A' : set(['B', 'C', 'E']),
		 'B' : set(['A', 'D', 'F']),
		 'C' : set(['A', 'G']),
		 'D' : set(['B']),
		 'E': set(['A', 'F']),
         'F': set(['B', 'E']),
         'G': set(['G'])
         }

def dfs(graph, root):
	visited = [] #각 꼭지점이 방문되었는지를 기록
	stack = [root, ]

	while stack: #stack이 비게 되면 탐색 끝
		vertex = stack.pop() # 방문되어지고 있는 꼭지점
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

print(dfs(graph, 'A'))