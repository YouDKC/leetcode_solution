class Solution(object):
    # pycharm 同步成功啦！
    def catMouseGame(self, graph):
        N = len(graph)
        prin('haha')
        # 判断图一共有多少个节点
        MOUSE, CAT = 1, 2
        # mouse, cat, turn
        color = [[[0] * 3 for i in range(N)] for j in range(N)]
        # 这是个n*n*3的颜色矩阵，这个矩阵就记录着是猫还是老鼠赢，如果是1就是老鼠赢，如果是2就是猫赢
        q = collections.deque()
        # 创建一个队列
        for i in range(1, N):
            for t in range(1, 3):
                color[0][i][t] = 1
                # 将第0行第i列的第1，2个颜色染色为1，
                q.append((0, i, t))
                # 在队列中添加一个老鼠赢的状态
                color[i][i][t] = 2
                # 将第i行第i列的第1，2个颜色染色为2，
                q.append((i, i, t))
                # 在队列中添加一个毛赢的状态
        # 上述操作是在队列中添加了所有的猫赢或者老鼠赢的状态, 其中包含了猫轮和老鼠轮
        while q:
            curStatus = q.popleft()
            # 取出队列中第一个状态
            cat, mouse, turn = curStatus
            # 猫的位置，老鼠的位置，该哪个走
            for preStatus in self.findAllPrevStatus(graph, curStatus):
                # 找到当前状态的所有父状态
                preCat, preMouse, preTurn = preStatus
                # 猫父状态，老鼠父状态，当前是什么轮
                if color[preCat][preMouse][preTurn] != 0:
                    # 如果父状态的颜色不为0，那么检验下一个父状态
                    continue
                if color[cat][mouse][turn] == 3 - turn:
                    # 如果父状态的颜色不为0，那么可能就是1或者2，如果颜色是1即老鼠赢，并且是猫轮，或者颜色是2即猫赢，当前是老鼠轮
                    color[preCat][preMouse][preTurn] = preTurn
                    # 那么父状态就是赢的状态
                    q.append(preStatus)
                    # 在q中添加相应的状态
                elif self.allNeighboursWin(color, graph, preStatus):
                    # 传入当前的颜色矩阵和当前的父节点
                    color[preCat][preMouse][preTurn] = 3 - preTurn
                    q.append(preStatus)
        return color[1][2][1]
    
    def findAllPrevStatus(self, graph, curStatus):
        ret = []
        mouse, cat, turn = curStatus
        if turn == 1:
            # 如果当前是老鼠轮
            for preCat in graph[cat]:
                # 对于当前猫的位置所有的连接点
                if preCat == 0:
                    # 如果猫的连接点是0，则下一个，因为猫的上一个不可能在洞里
                    continue
                ret.append((mouse, preCat, 2))
                # 如果猫的连接点不在洞里，那么就在状态中添加一个父节点
        else:
            # 如果当前是猫轮
            for preMouse in graph[mouse]:
                # 对于所有与老鼠相连的节点
                ret.append((preMouse, cat, 1))
                # 状态中添加新状态
        return ret
    
    def allNeighboursWin(self, color, graph, status):
        mouse, cat, turn = status
        # 父节点的状态
        if turn == 1:
            # 如果当前是老鼠轮
            for nextMouse in graph[mouse]:
                # 那么对于每一个老鼠的相邻节点
                if color[nextMouse][cat][2] != 2:
                    # 如果老鼠相邻节点的
                    return False
        elif turn == 2:
            # 如果当前是猫轮
            for nextCat in graph[cat]:
                # 那么对于每一个猫的相邻节点
                if nextCat == 0:
                    # 如果老鼠在洞里，那么继续判断
                    continue
                if color[mouse][nextCat][1] != 1:
                    # 如果
                    return False
        return True























