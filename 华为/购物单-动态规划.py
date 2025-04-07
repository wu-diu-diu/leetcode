while True:
    try:## 总金额，物品数量
        total, k = list(map(int, input().split()))
        ## 单价
        W = {}  ## 使用字典来构建表格，键为物品编号，值为[0,0,0]，分别存储主件，附件1，附件2的价格
        ## 价值
        V = {}
        total = int(total / 10)
        main_key = []
        for i in range(1, k+1):  ## W中的键从1开始，构建k行，每行的值为[0,0,0]，分别存储主件，附件1，附件2的价格
            W[i] = [0,0,0]
            V[i] = [0,0,0]  ## V中的键从1开始，构建k行，每行的值为[0,0,0]，分别存储主件，附件1，附件2的价值
        for i in range(k):
            ## 单价，重要度，类别
            v, p, q = list(map(int, input().split()))
            if q == 0:  ## 主件，存储在W和V的第一列
                W[i+1][0] = int(v/10)
                V[i+1][0] = int(v*p/10)
                main_key.append(i + 1)  ## 主件编号存储在main_key中
            else:
                if W[q][1] == 0:  ## 附件1，存储在W和V的第二列
                    W[q][1] = int(v/10)
                    V[q][1] = int(v*p/10)
                else:
                    W[q][2] = int(v/10)
                    V[q][2] = int(v*p/10)
        W_lst = []
        V_lst = []
        for key in W.keys():
            if key in main_key:
                W_lst.append(W[key])  ## 如果是主件，则将主件的价格存储在W_lst中，因为肯定有两个附件，所以
                ## W中一定有两行是全为0的，所以这里其实是将这两行去掉
                V_lst.append(V[key])
        m = len(W_lst)  ## m为主件的数量
        dp = [[0] * (total+1) for _ in range(m+1)]  ## 构建m+1行，total+1列的表格
        for i in range(1, m+1):
            w1 = W_lst[i-1][0]  ## 主件的价格
            w2 = W_lst[i-1][1]  ## 附件1的价格
            w3 = W_lst[i-1][2]  ## 附件2的价格
            v1 = V_lst[i-1][0]  ## 主件的价值
            v2 = V_lst[i-1][1]  ## 附件1的价值
            v3 = V_lst[i-1][2]  ## 附件2的价值
            for j in range(total+1):
                # 1. 不放入:
                dp[i][j] =dp[i-1][j]
                # 2. 放入一个主件
                if j-w1>=0:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-w1]+v1)
                # 3. 1个主件+附件1
                if j-w1-w2>=0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-w2-w1]+v1+v2)
                # 4. 一个主件+附件2
                if j-w1-w3>=0:
                    dp[i][j] =  max(dp[i][j], dp[i-1][j-w3-w1]+v1+v3)
                # 5. 一个主见+附件1+附件2
                if j-w1-w2-w3 >=0:
                    dp[i][j] =  max(dp[i][j], dp[i-1][j-w3-w2-w1]+v1+v2+v3)
        print(int(dp[m][total]*10))
    except:
        break
