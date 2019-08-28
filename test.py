class Solution(object):
    def catMouseGame(self, graph):
        N = len(graph)
        prin('haha')
        # 判断图一共有多少个节点
        MOUSE, CAT = 1, 2
        # mouse, cat, turn
        color = [[[0] * 3 for i in range(N)] for j in range(N)]
        # 这是个n*n*3的颜色矩阵，这个矩阵就记录着是猫还是老鼠赢，如果是1就是老鼠赢，如果是2就是猫赢，
        # 这里面的color为什么要用长度为3的数组呢，主要是因为第一个不用，index为1或2则表明当前是猫轮还是老鼠轮
        q = collections.deque()
        # 创建一个队列，这个队列中存储了所有猫赢或者老鼠赢的状态
        for i in range(1, N):
            for t in range(1, 3):
                color[0][i][t] = 1
                # 将第0行第i列的第1，2个颜色染色为1，即当前无论是猫轮还是老鼠轮，都是老鼠赢
                q.append((0, i, t))
                # 在队列中添加一个老鼠赢的状态
                color[i][i][t] = 2
                # 将第i行第i列的第1，2个颜色染色为2，即当前无论是猫轮还是老鼠轮，都是猫赢
                q.append((i, i, t))
                # 在队列中添加一个猫赢的状态
        # 上述操作是在队列中添加了所有的猫赢或者老鼠赢的状态, 其中包含了猫轮和老鼠轮
        while q:
            curStatus = q.popleft()
            # 取出队列中一个猫赢或者老鼠赢的状态
            cat, mouse, turn = curStatus
            # 猫的位置，老鼠的位置，该哪个走
            for preStatus in self.findAllPrevStatus(graph, curStatus):
                # 找到当前状态的所有父状态
                preCat, preMouse, preTurn = preStatus
                # 猫父状态，老鼠父状态，当前是什么轮，这个preTurn与curTurn的和为3
                if color[preCat][preMouse][preTurn] != 0:
                    # 如果父状态的颜色不为0，那么可能就是1或者2，那么检验下一个父状态，因为此时的父状态已经赢了
                    continue
                if color[cat][mouse][turn] == 3 - turn:
                    # 如果父状态颜色是0，并且当前状态的颜色正好与当前轮相反12,或21，也就是说当前是猫赢老鼠轮，或者老鼠赢猫轮
                    # 反之可以推理，如果当前颜色和当前轮分别为11，22，老鼠赢该老鼠走，也就是说父轮是猫走的，应该猫走，怎么可能让老鼠赢呢？
                    color[preCat][preMouse][preTurn] = preTurn
                    # 那么父状态就是该谁走谁赢赢的状态
                    q.append(preStatus)
                    # 在q中把当前赢的状态添加进去
                elif self.allNeighboursWin(color, graph, preStatus):
                    # 如果如果当前颜色和当前轮分别为11，22，老鼠赢该老鼠走，也就是说父轮是猫走的，应该猫走，怎么可能让老鼠赢呢？
                    # 所以这种情况下，虽然是该猫走，但是迫于无奈，猫已经被包围了，无论怎么走，都是老鼠赢
                    # 传入当前的颜色矩阵和当前的父节点
                    color[preCat][preMouse][preTurn] = 3 - preTurn
                    # 父状态就是该谁走，那么另一方赢，因为判断条件已经决定了，无论怎么走，都是另外一方赢，没办法了对吧
                    q.append(preStatus)
        return color[1][2][1]
    
    def findAllPrevStatus(self, graph, curStatus):
        ret = []
        # 创建一个ret来存储所有的父状态
        mouse, cat, turn = curStatus
        # 当前的猫和老鼠的位置以及是当前x轮
        if turn == 1:
            # 如果当前是老鼠轮，则父状态肯定是猫轮
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
        # status父节点的状态
        if turn == 1:
            # 如果当前是老鼠轮
            for nextMouse in graph[mouse]:
                # 那么当前既然是老鼠轮，那么老鼠就再走一步
                if color[nextMouse][cat][2] != 2:
                    # 如果不等于2，那么就是等于1或者0，即猫轮老鼠赢，或者无状态
                    # 接下来该猫走了，如果猫没有赢，返回错误
                    return False
        elif turn == 2:
            # 如果当前是猫轮
            for nextCat in graph[cat]:
                # 那么猫向前走一步
                if nextCat == 0:
                    # 如果老鼠在洞里，那么继续判断下一个点
                    continue
                if color[mouse][nextCat][1] != 1:
                    # 如果老鼠没有赢那么，返回错误
                    return False
        return True























