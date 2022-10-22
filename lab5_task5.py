from random import sample
def get_random_password(n: int = 8) -> str:
    population = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567'
    return ''.join(sample(population, n))

print(get_random_password())
