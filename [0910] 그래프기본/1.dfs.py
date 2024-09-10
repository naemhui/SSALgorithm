# page25. 연습문제1
import sys
sys.stdin = open("graph.txt", "r")

# 시작점: 1번부터
# 끝점: 1번에서 갈 수 있는 모든 정점을 방문하면 종료(visited처리 덕분에. 기저조건 없이도 자연히 종료)
def dfs(node):
    print(node, end=' ')  # 현재 노드 출력

    # 현재 정점에서 연결되어 있는(갈 수 있는) 노드들을 탐색
    # graph[node][::-1] : 숫자가 큰 노드부터 탐색(후보군을 뒤집어주기)
    for next_node in graph[node]:  # 이미 방문했다면 통과. visited 덕분.
        if visited[next_node]:
            continue

        visited[next_node] = 1  # 방문 처리
        dfs(next_node)          # 다음 정점으로 이동


N, M = map(int, input().split())
# 비어있는 리스트를 N+1번 반복하며 생성
# 1. 비어있는 리스트: 아직 갈 수 있는 곳이 없다
# 2. N+1번: 0번 인덱스를 버린다. (문제에서 노드 번호가 1부터 시작)
# -> 인접 리스트를 만들기 위해 아래와 같이 정의
graph = [[] for _ in range(N + 1)]

# 인접행렬이라면
# graph = [[0]*(N+1) for _ in range(N+1)]

visited = [0] * (N + 1)

# 연결 정보를 저장
for _ in range(M):
    s, e = map(int, input().split())
    # 양방향 그래프이므로, 시작<-> 끝점을 바꾸면서 저장
    graph[s].append(e)
    graph[e].append(s)  # 문제가 방향그래프라면, 바꾼 정보를 저장하면 버그 남

visited[1] = 1  #
dfs(1)