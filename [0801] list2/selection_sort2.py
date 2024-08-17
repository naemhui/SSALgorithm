def selection_sort(lst, N):
    # lst : 정렬 대상
    # N: 정렬 대상의 길이(원소 개수)

    for i in range(N-1):
        # i번 인덱스의 자리 주인을 찾을 건데
        # 남은 원소들 중에서 제일 작은 원소를 찾을 것이다
        min_idx = i

        for j in range(i+1, N):
            # i+1부터 제일 작은 원소 찾기 시작
            if lst[min_idx] > lst[j]:  # 내 예상 최솟값 > 현재 내 위치
                min_idx = j

        # 찾은 최솟값의 인덱스를 사용하여 자리 바꿔주기
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

lst = [5, 1, 2, 9, 4, 3]
selection_sort(lst, len(lst))
print(lst)