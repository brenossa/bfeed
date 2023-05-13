from flask import Flask, render_template, request, jsonify

class Feed:
	def __init__(self):
		self.posts = []

	def adicionar_post(self, novo_post):
		self.posts.append(novo_post)

	def alterar_post(self, identificador, novo_valor):
		self.posts[identificador] = novo_valor

	def deletar_post(self, identificador):
		del self.posts[identificador]


app = Flask(__name__)
meu_feed = Feed()

@app.route("/")
def feed():
	return render_template("feed.html", posts=meu_feed.posts)

@app.route("/posts", methods=["GET"])
def posts():
        return jsonify(meu_feed.posts)

@app.route("/postar", methods=["POST"])
def postar():
	data = request.get_json()
	meu_feed.adicionar_post(data)
	return jsonify({'message': 'Post adicionado'})

@app.route("/alterar/<int:identificador>", methods=["PUT"])
def alterar(identificador):
	data = request.get_json()
	meu_feed.alterar_post(identificador, data)
	return jsonify(data)

@app.route("/deletar/<int:identificador>", methods=["DELETE"])
def deletar(identificador):
	meu_feed.deletar_post(identificador)
	return jsonify({'message': 'Post excluido'})

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=80)
