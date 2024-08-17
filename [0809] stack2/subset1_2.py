# 합이 S 이하인 부분집합을 구하는!!!!!!

lst = [1, 2, 3, 4, 5]
N = 5
S = 10
print(lst)


# idx : 내가 현재 idx번째 원소를 고를지 말지 선택
# selected : 내가 고른 원소를 체크
# selected[x] == 1 : x번째 원소를 부분집합에 포함시킴
# selected[y] == 0: y번째 원소는 부분집합에 포함하지 않았다.
# n : 원소의 전체 개수
# s : 지금까지 구한 부분집합의 합
def make_subset(idx, selected, n, s):

    # 가지치기 해야됨 : 답이 될 가능성이 없으면 더 이상 진행 X
    if s > S:
        return

    # 종료 조건
    if idx == n:
        # n번 고민했다 -> 부분집합 구하기 완료
        subset = []
        for i in range(n):
            # i번째 원소를 골랐으면
            if selected[i]:
                # 부분집합에 넣기
                subset.append(lst[i])
        print(subset)
        return
    # 재귀 호출
    # idx번째 원소에 대해 부분집합에 idx원소를 포함하든가
    selected[idx] =1
    make_subset(idx+1, selected, n, s+lst[idx])

    # 부분집합에 idx번째 원소를 포함시키지 않든가
    selected[idx] = 0
    make_subset(idx+1, selected, n, s)

make_subset(0, [0]*N, N, 0)