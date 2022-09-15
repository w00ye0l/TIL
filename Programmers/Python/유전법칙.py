# def solution(queries):
#     result = []

#     for [n,p] in queries:
#         gen = []
#         answer = []
#         k = 0
#         if n == 1:
#             result.append('Rr')

#         else:
#             while True:
#                 gen.append(((p-1)//(4**(n-2))))
#                 if n == 2:
#                     break
#                 n -= 1

#             if len(gen) > 1:
#                 for i in range(1,len(gen)):
#                     gen[-i] -= gen[-i-1]*4


#             breaker = False
#             for num in gen:
#                 if num == 0:
#                     answer.append('RR')
#                     breaker = True
#                     break
#                 elif num == 3:
#                     answer.append('rr')
#                     breaker = True
#                     break
#             if breaker == False:
#                 answer.append('Rr')
#             result.append(*answer)
#     return result

def solution(queries):
    answer = []
    bean = ['RR', 'Rr', 'Rr', 'rr']

    for q in queries:
        n, p = q
        p -= 1

        if n == 1:
            answer.append('Rr')
        else:
            while True:
                d = p // (4 ** (n - 2))
                m = p % (4 ** (n - 2))

                if n == 2:
                    answer.append(bean[d])
                    break

                if d == 0:
                    answer.append(bean[d])
                    break
                elif d == 3:
                    answer.append(bean[d])
                    break
                else:
                    p = m

                n -= 1

    return answer


print(solution([[1, 1], [4, 26]]))
