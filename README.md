# AI vs Human Text Classifier

This project is a Flask-based web application that uses Hugging Face's transformers library to classify whether a given text is **AI-generated** or **Human-generated**. It leverages the zero-shot classification model `facebook/bart-large-mnli`.

## Features
- **Zero-shot Classification**: Uses Hugging Face's `facebook/bart-large-mnli` model for zero-shot classification to identify whether a text is AI-generated or human-generated.
- **REST API**: Exposes a POST endpoint `/classify` that accepts text and returns the classification result.
- **Simple Frontend**: Includes a basic frontend where users can input text, and the app will classify it as AI-generated or human-generated.

## Demo
You can try the app by running it locally, and it will classify the text based on the model. The result will be shown on the frontend with a confidence score.

## Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.x** or higher
- **pip** (Python package installer)
- **Git** (if cloning the repository)

## Installation & Setup

### 1. Clone the Repository
Start by cloning this repository to your local machine:

```bash
git clone https://github.com/Saurasai/my-project.git
cd my-project
