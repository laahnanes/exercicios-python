num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 10 % 10
m = num // 1000 % 10
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')