'''Tratamento de ERROS

Erro sintático: erro de escrita .
Erro semântico: erro de significado.
Exceção é erro semântico. (Namerror, ValueError, ZeroDivisionError, TypeError, ModuleNotFoundError)

Comando try/except
Exception mostra o erro
'''

try:
    a = int(input('Numerador: '))
    b = int(input('Divisor: '))
    r = a / b
except Exception as erro:
    print(f'\033[0;31mInfelizmente tivemos um problema... :(    O erro foi {erro.__class__} \033[m')
else:
    print(f'O resultado é {r}.')
finally:
    print('Muito Obrigado!')
        
