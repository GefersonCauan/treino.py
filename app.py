from flask import Flask, request, jsonify

app= Flask(__name__)


usuarios = []


@app.route('/')
def home():
    return "Bem vindo a APi do cauan gostoso"

@app.route('/usuarion', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()


    nome = data.get('nome')
    idade = data.get('idade')


    if nome and idade:
        usuario = {"nome": nome, "idade": idade}
        usuarios.append(usuario)
        return jsonify({"mensagem": "Usuario cadastrado"}), 201
    return jsonify({"mensagem": "dados invalidos"}), 400


@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)


@app.route('/usuraios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    if 0 <= id < len(usuarios):
        usuario = usuarios.pop(id)
        return jsonify({"mensagem": "usuarios nao encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)