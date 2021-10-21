def escreva(txt):
    risca = len(txt) + 2
    print('=' * risca)
    print(' ' + txt)
    print('=' * risca)


escreva('olá mundo')
escreva('por incrivel que pareça esse programa foi facil')
escreva(input('Deixe sua mensagem aqui: ').strip())
