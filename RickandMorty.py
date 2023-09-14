import requests
URL = 'https://rickandmortyapi.com/api/character'
req = requests.get(URL)

if req.status_code == 200:
      dados = req.json()
for Personagem  in dados['results']:
        print('Nome:',Personagem['name'])
        print('Especie:',Personagem['species'])
        print('\n')

   
if req.status_code == 404:
    print('Não encontrado')               
