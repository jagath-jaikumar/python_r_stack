from flask import Flask, request, jsonify

app = Flask("py example")

@app.route("/echo")
def simple_get():
    name = request.args.get('msg')
    msg = "The message is: '{}''".format(name)
    return jsonify({"msg":[msg]})




@app.route("/sum", methods=["POST"])
def simple_post():
    data = request.get_json()
    print(data)
    a,b  = int(data["a"]), int(data["b"])
    return jsonify([sum(a,b)])


def sum(a,b):
    return a+b


if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5000)
