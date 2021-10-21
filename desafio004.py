frase = input('me diga alguma coisa: ')
ciano = '\033[36m'
if type(frase) == str:
    print('sua mensagem é uma string')
else:
    print('sua mensagem não é uma string')
print('sua frase é: {}{}\033[m'.format(ciano, frase))
print('seu texto possui {}{}\033[m carcatéres'.format(ciano, len(frase)))
print('é um numero?', frase.isnumeric())
print('é alfabetico?', frase.isalpha())
print('é alfanumerico?', frase.isalnum())
print('está em minusculo?', frase.islower())
print('está em maiuscula?', frase.isupper())
print('são só espaços?', frase.isspace())
