# Chicken Gym
Projeto feito para fins de aprendizado utilizando Flask com Python3.
 
O projeto é um esboço de gerenciador para uma academia fictícia,
apresentará as views e o CRUD.

## Primeira Execução
* Instale o Python3 e o pip.
* Pelo terminal, vá para a pasta raiz do projeto
* Execute ```pip install -r requirements.txt``` para instalar as dependências.
* Execute os seguintes comandos para criar/migrar o banco:
    * ```python3 run.py db init```
    * ```python3 run.py db migrate```
    * ```python3 run.py db upgrade```
* Execute * ```python3 run.py runserver``` para iniciar a aplicação em localhost.
* Acesse <https://localhost:5000/> para ver a interface inicial

***OBS:*** *O programa cadastra o usuário **admin** com senha **admin** para fins de teste*.
