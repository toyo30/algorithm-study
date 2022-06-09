'''
오름차순 리스트 coins에 대하여 coins[i+1] 가 coins[i]의 배수일 때,
거스름돈보다 작거나 같은 금액의 동전 중 가장 금액이 큰 동전을 이용해 최대 금액을 지불한 후
나머지 거스름돈에 대해서도 같은 과정을 반복하는 것이 최적의 해에 도달하는 방법이다

단, coins[i+1]가 coins[i]의 배수라는 조건이 성립하지 않는다면 위 방법으로 최적의 해에 도달할 수 없다
'''


def min_coins(num, coins):
	cnt = 0
	for coin in coins[::-1]: # 내림차순으로 정렬
		if num >= coin:
			# num보다 작거나 같은 동전 중 가장 큰 동전을 최대한 많이 사용한다
			cnt += num // coin 
			num %= coin
	
	return cnt

inp = int(input())
coins = [10, 50, 100, 500]

print(min_coins(inp, coins))