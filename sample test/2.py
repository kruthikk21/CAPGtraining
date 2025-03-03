n = int(input("Enter number of coins: "))
coins = []

for i in range(n):
    coin = int(input("Enter the coin: "))
    coins.append(coin)

for coin in set(coins):
    print(f"{coin} {coins.count(coin)} ")
