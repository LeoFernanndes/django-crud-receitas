# Django Crud Receitas

Crud de um app para caderno de receitas virtual


## Arquitetura

Aplicação web constituida de uma aplicação django fazendo frontend e backend end juntamente com um banco postgres e um 
servidor nginx. \
Para entender melhor a configuração dos serviços, veja: [docker-compose.yml](./docker-compose.yml).


## Dependências

Docker version 20.10.8 \
Docker-compose version 1.29.2 \
Django version 3.1.5 \
Gunicorn version 20.1.0 

Para uma lista completa das dependências do projeto, vá para [requirements.txt](./requirements.txt)

## Instalação

Obs.: Para rodar o app, você precisa do docker-compose instalado.

1. Clone a branch master localmente. 
    ```git clone https://github.com/LeoFernanndes/django-crud-receitas.git```
2. Verifique se existem processos rodando na porta 80.
3. Para subir o servidor com todas as dependências necessárias: \
   ```sudo docker-compose up --build``` \
    O comando deve ser executado como sudo pois o container do postgres é dono dos próprios processos.
