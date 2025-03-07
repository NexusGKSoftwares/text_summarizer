# Text Summarizer

A web application for summarizing text and PDF documents using both extractive and abstractive summarization techniques.

## Features

- Summarize plain text input.
- Summarize text extracted from PDF files.
- Choose between extractive and abstractive summarization methods.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:

```bash
python app.py
```

2. Use the following API endpoints:

### Summarize Text

- **Endpoint**: `/summarize`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "text": "Your text here",
    "type": "abstractive"  // Optional, defaults to "abstractive"
  }
  ```
- **Response**:
  ```json
  {
    "summary": "The summarized text."
  }
  ```

### Summarize PDF

- **Endpoint**: `/summarize_pdf`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "pdf_file": "path/to/your/file.pdf",
    "type": "abstractive"  // Optional, defaults to "abstractive"
  }
  ```
- **Response**:
  ```json
  {
    "summary": "The summarized text from the PDF."
  }
  ```

## License

This project is licensed under the MIT License.
