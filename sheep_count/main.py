def count_sheep(n):
    i = 1
    sheep = ''
    while i <= n:
        sheep_count = f'{i} sheep...'
        sheep += sheep_count
        i+=1
    return sheep

n = int(input('Digite um numero:'))
print(count_sheep(n))