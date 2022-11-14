# Frexco API
# Sobre o desafio

Esta foi uma API criada para o processo seletivo da Frexco. O desafio consiste em criar uma API com pelo menos dois endpoints. Onde seja possível cadastrar usuários utilizando
login, senha e data de nascimento. Caso a senha não seja fornecida uma senha aleatório será gerada.
É preciso também que seja possível consultar os usuários cadastrados no formato JSON.

# Tecnologias utilizadas
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
- Django Rest Framework

#O que se pode fazer com essa API
- Requisição POST para `[URL]/usuarios` contendo `{"login": "Login do Usuário", "senha": "Senha do Usuário", "dataDeNascimento": "Data de Nascimento do Usuário}` adiciona essa entrada no banco de dados.

Exemplo de resposta:
```
{
    "id": "8a65a07a-90cf-46b2-8aac-5e893dae01f7",
    "login": "Login do Usuário",
    "senha": "Senha do Usuário",
    "dataDeNascimento": "Data de Nascimento do Usuário"
}
```

- Requisição GET para `[URL]/usuarios` retorna uma lista de usuários do banco. É possível também enviar querys com esse endpoint para retornar usuários com valores especifícos em seu login, por exemplo: `[URL]/usuarios/?query=d` que retorna todos os usuários com a letra 'd' em seu login.

Exemplo de resposta:
```
[
  {
    "id": "8a65a07a-90cf-46b2-8aac-5e893dae01f7",
    "login": "Login do Usuário 1",
    "senha": "Senha do Usuário 1",
    "dataDeNascimento": "Data de Nascimento do Usuário 1"
  },
  {
    "id": "8a65a07a-90cf-46b2-8aac-5e893dae01f7",
    "login": "Login do Usuário 2",
    "senha": "Senha do Usuário 2",
    "dataDeNascimento": "Data de Nascimento do Usuário 1"
  }
]
```

- Requisição GET para `[URL]/usuario/[Login do Usuário]` retorna as informações do usuário com o login especificado.

Exemplo de resposta para: `[URL]/usuario/DaviidSantos`:
```
{
    "id": "8a65a07a-90cf-46b2-8aac-5e893dae01f7",
    "login": "DaviidSantos",
    "senha": "Senha do Usuário DaviidSantos",
    "dataDeNascimento": "Data de Nascimento do Usuário DaviidSantos"
}
```
  
 - Requisição PUT para `[URL]/usuario/[Login do Usuário]` atualiza o login e senha do usuário.
 
 - Requisição DELETE para `[URL]/usuario/[Login do Usuário]` apaga o usuário do banco de dados.


# Autor

David Pereira Santos

 [![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/daavidpsantos/)](https://www.linkedin.com/in/daavidpsantos/)

