from flask import Blueprint, render_template, request, jsonify

blue_print = Blueprint("main", __name__)


def translate_text(text, source_lang, target_lang):
    return f"TODO: Translate '{text}' from {source_lang} to {target_lang}"


@blue_print.route("/", methods=["GET"])
def index():
    return render_template("index.html", input_text="", output_text="", source_lang="en", target_lang="de", examples=[
        "Nice to meet you!", "What time is it?", "Where is the train station?"
    ])


@blue_print.route("/translate", methods=["POST"])
def translate():
    input_text = request.form.get("input_text", "")
    source_lang = request.form.get("source_lang", "en")
    target_lang = request.form.get("target_lang", "de")
    output_text = translate_text(input_text, source_lang, target_lang)

    return render_template("index.html", input_text=input_text, output_text=output_text,
                           source_lang=source_lang, target_lang=target_lang, examples=[
            "How are you?", "Good morning!", "I love learning German."
        ])


@blue_print.route("/api/translate", methods=["POST"])
def api_translate():
    data = request.get_json()
    input_text = data.get("input_text", "")
    source_lang = data.get("source_lang", "en")
    target_lang = data.get("target_lang", "de")
    output_text = translate_text(input_text, source_lang, target_lang)
    return jsonify({"output_text": output_text})
