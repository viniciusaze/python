# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

login = input('Login: ')
senha = input('Senha: ')
if login == 'vinicius' and senha == 'vinicius12345':
    print('Acesso liberado!')
    print(f'Bem-vindo {login}!')
else:
    print('Usuário ou senha inválidos!')