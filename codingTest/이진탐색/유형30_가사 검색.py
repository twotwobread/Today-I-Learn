# 맨처음 인덱스가 ?인 경우
# => 절반 쪼개고 거기가 ?인 경우 - start = middle + 1, result = middle
#    ?가 아닌 경우 - end = middle - 1
# -> 맨 마지막 ?의 위치를 찾았으면 그거 다음부터 마지막 인덱스까지랑 단어의 위치랑 비교
# 맨마지막 인덱스가 ?인 경우
# => 절반 쪼개고 거기가 ?인 경우 - end = middle - 1, result = middle
#    ?가 아닌 경우 - start = middle + 1
# 둘다 ?인 경우 -> 길이만 같을 경우 count += 1

from bisect import bisect_left, bisect_right
# def solution(words, queries):
#     answer = []
#     for q in queries:
#         count = 0
#         start = 0
#         end = len(q) - 1
#         index = -1
#         if q[0] == '?':
#             for w in words:
#                 if len(q) == len(w):
#                     while start <= end:
#                         mid = (start + end)//2
#                         if q[mid] != '?':
#                             end = mid - 1
#                         else:
#                             index = mid
#                             start = mid + 1
#                             if q[start] != '?':
#                                 break
#                     if q[index+1:] == w[index+1:]:
#                         count += 1
#         elif q[-1] == '?':
#             for w in words:
#                 if len(q) == len(w):
#                     while start <= end:
#                         mid = (start + end) // 2
#                         if q[mid] != '?':
#                             start = mid + 1
#                         else:
#                             index = mid
#                             end = mid - 1
#                             if q[end] != '?':
#                                 break
#                     if q[0:index] == w[0:index]:
#                         count += 1
#         else:
#             for w in words:
#                 if len(q) == len(w):
#                     count += 1
#         answer.append(count)
#     return answer
# 기존 접근 방식 ( 위 )
# 기존 접근 방식은 모든 words를 돌면서 반복하여 시간이 오래 걸림.
# 다른 접근 방식인 아래는 미리 word를 length에 따라 나누고 query의 길이에 맞는 곳만
# 확인함 그리고 fro?? 인 경우 froaa ~ frozz 범위의 개수를 찾아서 더 빠르게 동작 가능.
# ??fro 인 경우엔 거꾸로 뒤집어 orfaa - orfzz 범위의 개수를 찾음.
def countSame(array, x, y):
    left = bisect_left(array, x)
    right = bisect_right(array, y)
    return right - left

def lower_binarySearch(array, goal, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] >= goal:
            end = mid
        else:
            start = mid + 1
    return end
def upper_binarySearch(array, goal, start, end):
    while start < end:
        mid = (start + end + 1) // 2
        if array[mid] <= goal:
            start = mid
        else:
            end = mid - 1
    return start
def countSameMine(array, x, y):
    if len(array) <= 0:
        return 0
    left = lower_binarySearch(array, x, 0, len(array)-1)
    right = upper_binarySearch(array, y, 0, len(array)-1)
    if left == right:
        if array[left] < x or array[right] > y:
            return 0
    return right - left + 1

def solution(words, queries):
    lenWords = [[] for _ in range(10001)]
    reverseLenWords = [[] for _ in range(10001)]
    answer = []
    for w in words:
        lenWords[len(w)].append(w)
        reverseLenWords[len(w)].append("".join(reversed(w)))
    for i in range(1, 10001):
        lenWords[i].sort()
        reverseLenWords[i].sort()

    for q in queries:
        if q[0] == '?':
            length = countSameMine(reverseLenWords[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            answer.append(length)
        elif q[-1] == '?':
            length = countSameMine(lenWords[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            answer.append(length)
        else:
            answer.append(len(lenWords[len(q)]))
    return answer

def solution(words, queries):
    answer = []
    for w in words:
        lenWords[len(w)].append(w)
        reverseLenWords[len(w)].append("".join(reversed(w)))
    for i in range(1, 10001):
        lenWords[i].sort()
        reverseLenWords[i].sort()

    for q in queries:
        if q[0] == '?':
            length = countSameMine(reverseLenWords[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            answer.append(length)
        elif q[-1] == '?':
            length = countSameMine(lenWords[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            answer.append(length)
        else:
            answer.append(len(lenWords[len(q)]))
    return answer

if __name__ == "__main__":
    lenWords = [[] for _ in range(10001)]
    reverseLenWords = [[] for _ in range(10001)]
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao", "zzzz", "yyyy", "aaaa", "aaab"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?", "????"]
    print(solution(words, queries))
