# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 0018 15:03
# @Author  : DZY
# @File    : Dfs.py
# @Software: PyCharm
#https://www.bilibili.com/video/BV1Ks411579J/?spm_id_from=333.788.videocard.0
#Dfs 用栈，下一个要走的结点一定是上一个结点的邻结点,当走到实在无法往前走的时候
#就会回溯到前面的某一个结点（如果从栈中拿出的那个结点没有邻结点时，就继续从栈中取元素）
#过程：先让图中某一结点入栈，然后就让它出栈，出栈后将与之相关联的结点全部入栈，
#然后再将最后一个入栈的结点出栈，再将出栈结点相关联的结点全部入栈，然后重复上述
#过程，直到栈为空，即所有结点都已处理
def dfs(graph,s):
	stack = []
	visited = set()
	#找一个结点，先入栈，然后马上出栈，再将其关联结点全部入栈
	stack.append(s)
	visited.add(s)

	while len(stack) > 0:
		vertex = stack.pop()
		for node in graph[vertex]:
			if node not in visited:
				stack.append(node)
				visited.add(node)
		print(vertex)


graph = {
	"A":["B","C"],
	"B":["A","C","D"],
	"C":["A","B","D","E"],
	"D":["B","C","E","F"],
	"E":["C","D"],
	"F":["D"]
}



dfs(graph,'E')






















