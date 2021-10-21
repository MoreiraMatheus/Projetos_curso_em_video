pt = int(input('me diga o primeiro termo de uma P.A.: '))
r = int(input('me diga a razão de uma P.A.:'))
for c in range(1, 11):
    pt += r
    print(' -', pt, end='')
