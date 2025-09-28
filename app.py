from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return '<h1>Olá, Mundo! A imagem Docker foi atualizada para a versão mais nova!</h1>'
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 