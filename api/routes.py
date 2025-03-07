from flask import Flask, request, jsonify
from services.abstractive import abstractive_summary
from services.extractive import extractive_summary
from services.pdf_processor import extract_text_from_pdf

app = Flask(__name__)

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")
    summary_type = data.get("type", "abstractive")  # Default to abstractive

    if summary_type == "extractive":
        summary = extractive_summary(text)
    else:
        summary = abstractive_summary(text)

    return jsonify({"summary": summary})

@app.route("/summarize_pdf", methods=["POST" ])
def summarize_pdf():
    data = request.json
    pdf_file = data.get("pdf_file", "")
    summary_type = data.get("type", "abstractive")  # Default to abstr
    text = extract_text_from_pdf(pdf_file)
    if summary_type == "extractive":
        summary = extractive_summary(text)
    else:
        summary = abstractive_summary(text)
        return jsonify({"summary": summary})
    return jsonify({"summary": summary})
