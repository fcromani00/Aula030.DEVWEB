from flask import Flask, request, make_response, redirect, abort;
app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>Avaliação contínua: 030</h1>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/FelipeRomani">Identificação</a></li>
      <li><a href="/contextorequisicao">Contexto da requisição</a></li>
    <ul>'''

@app.route('/FelipeRomani')
def user():
    return '''<h1>Avaliação contínua: 030</h1>
  <h2>Aluno: Felipe Christofaro Romani</h2>
  <h2>Prontuário: PT3020223</h2>
  <h2>Instituição: IFSP</h2>
  <p>
    <a href="/">Voltar</a>
  </p>''';

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    client_ip = request.remote_addr
    client_host = request.host
    return f'''<h1>Avaliação contínua: 030</h1>
    <h2> Seu navegador é: {format(user_agent)}</h2>
    <h2>Seu endereço IP é: {format(client_ip)}</h2>
    <h2>Seu host é: {format(client_host)}</h2>
    <p>
    <a href="/">Voltar</a>
    </p>''';

if __name__ == '__main__':
    app.run(debug=True)