
def code_num(n):
    m = ''
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i+j) ==0:
                m += f'{i}{j}'
                continue
    return int(m)

for n in range(3, 21):
    m = code_num(n)
    print(f'{n} - {m}')
