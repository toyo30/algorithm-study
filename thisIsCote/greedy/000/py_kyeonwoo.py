N = int(input())
answer = 0
count = 0
if N%500 == 0:
    count += N//500
elif N%100 == 0:
    while N>0:
        N = N-100
        count += 1
        if N%500 == 0:
            count += N//500
            break
elif N%50 == 0:
    while N>0:
        N = N-50
        count += 1
        if N%500 == 0:
            count += N//500
            break
        elif N%100 == 0:
            while N>0:
                N = N-100
                count += 1
                if N%500 == 0:
                    count += N//500
                    break
            break
elif N%10 == 0:
    while N>0:
        N = N-10
        count += 1
        if N%500 == 0:
            count += N//500
            break
        elif N%100 == 0:
            while N>0:
                N = N-100
                count += 1
                if N%500 == 0:
                    count += N//500
                    break
            break
        elif N%50 == 0:
            while N>0:
                N = N-50
                count += 1
                if N%500 == 0:
                    count += N//500
                    break
                elif N%100 == 0:
                    while N>0:
                        N = N-100
                        count += 1
                        if N%500 == 0:
                            count += N//500
                            break
                    break
print(count)