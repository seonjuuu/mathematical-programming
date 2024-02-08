g2_list =[[],[2,4],[1,3],[2,6],[1,5,7],[4,8],[3,9],[4,8],[5,7],[6]]

g2_mat =[[0,0,0,0,0,0,0,0,0,0],[0,0,1,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,1,0,0,0],[0,1,0,0,0,1,0,1,0,0],[0,0,1,0,1,0,0,0,1,0],
[0,0,0,1,0,0,0,0,0,1],[0,0,0,0,1,0,0,0,1,0],[0,0,0,0,0,1,0,1,0,0],[0,0,0,0,0,0,1,0,0,0]]


## DFS ##
def dfs_list(graph, v, visited):
    visited[v]=True
    print(v,'-',end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs_list(graph, i, visited)

visited = [False]*10
dfs_list(g2_list,1,visited)
print("")


def dfs_mat(graph,v,visited):
    if visited[v]==True:
        return
    visited[v]=True
    print(v,'-',end=' ')
    for i in range(0, len(graph[v])):
        if graph[v][i]==1:
            dfs_mat(graph,i,visited)
            
visited = [False]*10
dfs_mat(g2_mat,1,visited)
print("")

## BFS ##
def bfs_list(graph,v,visited):
    q =[]
    q.append(v)
    visited[v] = True
    while len(q)!=0:
        n=q.pop(0)
        print(n,'-',end=' ')
        for i in graph[n]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
                
visited = [False]*10                
bfs_list(g2_list,1,visited)
print("")

def bfs_mat(graph, v ,visited):
    q=[]
    q.append(v)
    visited[v]=True
    while len(q)!=0:
        n = q.pop(0)
        print(n,'-',end=' ')
        for i in range(0, len(graph[n])):
            if graph[n][i] == 1 and visited[i]==False:
                q.append(i)
                visited[i]=True       
                       
visited = [False]*10                
bfs_mat(g2_mat,1,visited)


##review1
g3_list = [[1,2,3],[0,3],[0],[0,1],[5],[4]]
#case 1
def is_has_path(g,start,end,path=None):
    if path is None :
        path = []
    path.append(start)
    print(path)
    if start == end :
        return 1
    for i in g[start]:
        if i not in path:
            if is_has_path(g,i,end,path): #is_has_path=1이면 return 1 끝(즉, start=end면 끝)
                return 1
    return 0

##case2(dfs이용한 경로(dfs_sub)안에 end가 존재하는지)
def dfs_sub(g,v,visited,ret):
    visited[v] = True
    ret.append(v)
    for i in g[v]:
        if not visited[i]:
            dfs_sub(g,i,visited,ret)
            
def is_has_path_2(g,start,end):
    ng = len(g)
    visited = [False]*ng  #visited 초기화
    ret = []
    dfs_sub(g,start,visited,ret)
    print("ret:",ret)
    
    if end in ret :
        return 1
    else:
        return 0
    
print(is_has_path(g3_list,1,2))
print("======")
print(is_has_path_2(g3_list,1,2,))

##2
L = [3,2,7,8,1,4,5,6]
def is_cycle(L,start,visited):
    visited[start]=1
    n = L[start]
    if visited[n]==0:
        is_cycle(L,n,visited)
        
def cnt_cycle(L):
    tmp = [0]       #L[1]번째에 3이 연결되어있다는 것을 더 알아보기 쉽게 앞에 0을 추가해줌
    tmp = tmp+L     # [0, 3, 2, 7, 8, 1, 4, 5, 6]
    visited = [0]*(len(tmp))
    ret = 0       #cycle 갯수 
    for i in range(1,len(tmp)):
        if visited[i] == 0:      #i를 방문하지 않았을때만
            is_cycle(tmp,i,visited)
            ret = ret + 1
    return ret

print("number of cycle?",cnt_cycle(L))
