# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 0018 14:37
# @Author  : DZY
# @File    : Bfs.py
# @Software: PyCharm
#github
#bfs,首先一个结点入队列，然后让它出队，当它出队时，与之相连接的结点一股脑全进入
     #队列，然后先进的就先出，先出的结点再把与之相连接的结点全部入队，重复上面的
     #过程，直接所有的点都出队
#bfs通过队列来保证层的顺序
def bfs(graph,s):
	#queue中间介质，所有数据都是先通过这个队列然后出来
	queue = []
	#visited放入已经走过的结点,因为结点不能重复，所以这里用set
	visited = set()
	#先往队列中插入一个结点
	queue.append(s)
	#第一次放入队列后就直接出队，进入visited,然后再将所有联接点入队列
	visited.add(s)
	#只要队列不空就开始处理
	while len(queue) > 0:
		#先进先出
		#vertex对应的图中结点
		vertex = queue.pop(0)
		#遍历队中结点(查看结点的关联结点用graph[vertex])，有结点出队，与出队结点相关联的结点入队，没有
		#入队的就继续让结点出队，
		for node in graph[vertex]:
			if node not in visited:
				queue.append(node)
				visited.add(node)

		print('vertex：{}'.format(vertex))

graph = {
	"A":["B","C"],
	"B":["A","C","D"],
	"C":["A","B","D","E"],
	"D":["B","C","E","F"],
	"E":["C","D"],
	"F":["D"]
}


bfs(graph,"E")




