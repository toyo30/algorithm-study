N = int(input())
coin = 0

if N >= 500: 
  coin += N // 500
  N %= 500
if N < 500 and N >=100:
  coin += N // 100
  N %= 100
if N < 100 and N >= 50:
  coin += N // 50
  N %= 50
if N < 50 and N >= 10:
  coin += N // 10
  N %= 10

print(coin)