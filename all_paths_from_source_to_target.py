class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last_node = len(graph)-1
        start_node = 0
        routes=[]
        self.findDepth(start_node, last_node, routes, [], graph)
        return(routes)

    def findDepth(self, curr_node, last_node, routes, curr_route, graph):
        if(curr_node==last_node):
            curr_route.append(curr_node)
            routes.append(curr_route)
            return
        curr_route.append(curr_node)
        for i in graph[curr_node]:
            a = curr_route.copy()
            self.findDepth(i, last_node, routes, a, graph)
