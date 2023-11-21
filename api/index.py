from flask import Flask, request, jsonify

from api.transliterator import convert

app = Flask(__name__)


@app.route("/transliterate")
def transliterate():
    if not request.args:
        return jsonify({"result": "No term provided"})

    to_convert = request.args.get("term")
    input_orthography = request.args.get("input_orthography", "fr")

    if not to_convert:
        result = "No term provided"

    result = convert(to_convert, start=input_orthography)
    return jsonify({"result": result.strip()})
