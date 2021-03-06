# Setup

Instale o framework `serverless` :
```bash
$ curl -o- -L https://slss.io/install | bash
```

Crie um projeto a partir de um template
```bash
mkdir projeto/
cd projeto/

serverless create --template aws-python3
```

A estrutura ficará assim:
```bash
tree
.
├── handler.py
└── serverless.yml
```

Obs: Aqui estamos criando um projeto em python por ser uma linguagem que eu gosto. Porém o framework é poderoso e trabalha com outras linguagens e outras clouds. Para consultar as opções basta executar no terminal `serverless create --help`.

# Deploy

Para executar o deploy e acompanhar os logs do mesmo basta usar o seguinte comando: 
```bash
serverless deploy --verbose --stage dev
```

# Test

Para testar basta publicar uma nova mensagem no tópico SNS:
```bash
$ aws sns publish --topic-arn arn:aws:sns:sa-east-1:BIG_NUMBER:topic --message ":)" --region "sa-east-1" 

{
    "MessageId": "ccb5ed15-a8a0-5777-aba5-b5ed89b14657"
}
```
