"""权重:
起点-->A: 6
起点-->B: 2
B-->A: 3
B-->终点: 5
A-->终点: 1
解决这个问题需要三个散列表: graph, costs, parents
"""
# graph 记录了图的所有内容, 并且没一个节点中记录了
# 能够到达的节点以及其权重
graph = {}
# 权重保存在另一个散列表
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

# 保存每个节点的开销
infinity = float('inf') # 无穷大
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# 保存父节点
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# 一个数组用于保存已经处理过的节点
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # 在未处理的节点中找到开销最小的节点
while node is not None: # 这个循环在所有节点被处理之后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # 如果经当前节点前往该邻居更近, 
            costs[n] = new_cost #　就更新该邻居的开销
            parents[n] = node # 同时将该邻居的父节点设置为当前节点
    processed.append(node)
    node = find_lowest_cost_node(costs) # =找出接下来要处理的节点
    
print(parents)
print(costs["fin"])






