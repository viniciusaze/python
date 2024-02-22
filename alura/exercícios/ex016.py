class Musica:
    nome = ''
    artista = ''
    duracao = int

musica_sert = Musica()
musica_sert.nome = 'Sertanejo'
musica_sert.artista = 'Gusttavo Lima'
musica_sert.duracao = 3

print(vars(musica_sert))