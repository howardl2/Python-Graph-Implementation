from collections import defaultdict
import heapq as pq


class Graph(object):
	""" Graph data structure, undirected by default. """

	def __init__(self, connections, directed=False, weighted=False):
		""" If weighted, connections should be a dict of tuple_pairs: int_edgeWeight, otherwise, a list of tuples"""
		self._graph = defaultdict(set)
		self._weights = defaultdict(int)
		self._directed = directed
		self._weighted = weighted
		if not self._weighted:
			self.add_connections(connections)
		else:
			self.add_weighted(connections)


	def add_connections(self, connections):
		""" Add connections (list of tuple pairs) to graph """
		for node1, node2 in connections:
			self.add(node1, node2)

	def add_weighted(self, connections):
		""" Add connections for a weighted graph """
		if type(connections) != dict:
			raise TypeError("A weighted graph must be initialized with a dict of pair keys and weight values.")
		for k, v in connections.items():
			self.add_Edges(k,v)

	def add(self, node1, node2):
		""" Add connection between node1 and node2 """
		self._graph[node1].add(node2)
		if not self._directed:
			self._graph[node2].add(node1)

	def add_Edges(self, pair, edge):
		""" Add connection for node pairs with weight of edge """
		self.add(pair[0],pair[1])
		self._weights[pair] = edge
		if not self._directed:
			self._weights[(pair[1],pair[0])] = edge

	# def remove(self, node):
	# 	""" Remove all references to node """

	# 	for n, cxns in self._graph.iteritems():
	# 		try:
	# 			cxns.remove(node)
	# 			except KeyError:
	# 			pass
	# 	try:
	# 		del self._graph[node]
	# 	except KeyError:
	# 		pass

	# 	for n, cxns in self._weights.iteritems():
	# 		try:
	# 			cxns.remove(node)
	# 			except KeyError:
	# 			pass
	# 	try:
	# 		del self._graph[node]
	# 	except KeyError:
	# 		pass


	def is_connected(self, node1, node2):
		""" Is node1 directly connected to node2 """

		return node1 in self._graph and node2 in self._graph[node1]

	def getNodes(self):
		return self._graph.keys()

	def getNeighbor(self, v):
		return self._graph[v]

	def getEdgeWeight(self, v, u):
		return self._weights[(v,u)]

	def findMin(self, array, weights):
		arbitrary = array.pop()
		minVertex = arbitrary
		minWeight = weights[minVertex]
		for i in array:
			if weights[i] < minWeight:
				minVertex = i
		array.add(arbitrary)
		return minVertex


	def dijkstras(self,source):
		Q = set()
		dist = dict()
		prev = dict()
		
		for v in self._graph:
			dist[v] = float("inf")
			prev[v] = None
			Q.add(v)
		dist[source] = 0

		while Q:
			u = self.findMin(Q,dist)
			Q.remove(u)
			neighbor = self.getNeighbor(u[0])
			for i in neighbor:
				alt = dist[u] + self.getEdgeWeight(u,i)
				if alt < dist[i]:
					dist[i] = alt
					prev[i] = u
		return (dist, prev)

	# def dijkstrasNP(self, v):
	# 	Q = set()
	# 	dist = dict()
	# 	prev = dict()

	# 	for i in self._graph:
	# 		dist[i] = float("inf")
	# 		prev[i] = None
	# 		Q.add(i)
	# 	dist



	def shortestPath(self,source, target):
		d,p = self.dijkstras(source)
		s = []
		u = target
		while p[u]:
			s = [u] + s
			u = p[u]
		s = [u] + s
		return s


	def closenessCentrality(self, v):
		sumpaths = 0
		d = self.dijkstras(v)
		for i in d[0].values():
			sumpaths += i
		return sumpaths


	def betweennessCentrality(self, v):
		numpath = 0
		for s in self.getNodes():
			if s != v:
				for t in self.getNodes():
					if t != s and t != v:
						path = self.shortestPath(s,t)
						if v in path:
							numpath += 1
		return numpath

	def __str__(self):
		return '{}({})'.format(self.__class__.__name__, dict(self._graph))


if __name__ == "__main__":
	connections = {("a","b"):22, ("a","c"):9, ("a","d"):12, ("b","c"):35, ("b","h"):34,\
		   ("b","f"):36, ("c","f"):42, ("c","e"):65, ("c","d"):4, ("d","e"):33,\
		   ("d","i"):30, ("e","f"):18, ("e","g"):23, ("f","h"):24,("f","g"):39,\
		   ("g","h"):25, ("g","i"):21, ("h","i"):19}

	# connections = {("a","e"):1,("b","e"):1,("c","e"):1,("d","e"):1,("e","a"):1,("e","b"):1,("e","c"):1,("e","d"):1,("b","a"):1,("c","b"):1}

	g = Graph(connections, weighted = True)
	print(g.shortestPath("g","d"))


	print("a", g.betweennessCentrality("a"))
	print("b", g.betweennessCentrality("b"))
	print("c", g.betweennessCentrality("c"))
	print("d", g.betweennessCentrality("d"))
	print("e", g.betweennessCentrality("e"))
	print("f", g.betweennessCentrality("f"))
	print("g", g.betweennessCentrality("g"))
	print("h", g.betweennessCentrality("h"))
	print("i", g.betweennessCentrality("i"))

	# print("a",g.closenessCentrality("a"))
	# print("b",g.closenessCentrality("b"))
	# print("c",g.closenessCentrality("c"))
	# print("d",g.closenessCentrality("d"))
	# print("e",g.closenessCentrality("e"))
	# print("f",g.closenessCentrality("f"))
	# print("g",g.closenessCentrality("g"))
	# print("h",g.closenessCentrality("h"))
	# print("i",g.closenessCentrality("i"))










	
