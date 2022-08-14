import heapq
import sys
input = sys.stdin.readline

n = int(input())

s_heap = []                                     # 중간값 기준 작은 값들의 힙 (중간값 포함)
b_heap = []                                     # 중간값 기준 큰 값들의 힙
result = []                                     # 중간값 저장 리스트

for i in range(n):
    num = int(input())

    if len(s_heap) == len(b_heap):              # 양 힙의 길이가 같다면
        heapq.heappush(s_heap, (-num, num))     # 작은 힙(최대 힙)에 값을 추가 (중간값)
    else:                                       # 양 힙의 길이가 다르다면
        heapq.heappush(b_heap, (num, num))      # 큰 힙(최소 힙)에 값을 추가

    # 큰 힙에 값이 있고, 작은 힙의 루트값(첫 번째)이 큰 힙의 루트값(첫 번째)값보다 크면
    if b_heap and s_heap[0][1] > b_heap[0][0]:
        min_ = heapq.heappop(b_heap)[0]         # 중간값이 큰 힙에 있다는 것이기 때문에 서로를 교체
        # min_ == 큰 힙의 최솟값, max_ == 작은 힙의 최댓값
        max_ = heapq.heappop(s_heap)[1]
        heapq.heappush(s_heap, (-min_, min_))   # 큰 힙의 루트값을 작은 힙에 추가(최대 힙)
        heapq.heappush(b_heap, (max_, max_))    # 작은 힙의 루트값을 큰 힙에 추가(최소 힙)

    result.append(s_heap[0][1])                 # 중간값을 결과 리스트에 저장

for i in result:
    print(i)                                    # 반복마다 저장되는 중간값들을 하나씩 출력
