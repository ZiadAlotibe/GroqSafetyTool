echo "# Groq Pytector Project

This is a Python tool designed for detecting prompt injection attacks and unsafe content.  
It supports local model inference and integrates with Groq’s Llama Guard API for advanced content safety detection.

## Features
- Detect prompt injection in text inputs.
- Integrate with Groq’s Llama Guard API for risk categorization.
- Switch between local and API-based detection.

## Installation
\`\`\`bash
pip install .
\`\`\`

## Usage
\`\`\`python
from pytector import PromptInjectionDetector

detector = PromptInjectionDetector(model_name_or_url=\"deberta\")
is_injection, probability = detector.detect_injection(\"Your input here\")
print(is_injection, probability)
\`\`\`

## License
This project is currently not under an open-source license." > README.md

git add README.md
git commit -m "Add clean README"
git push -u origin main
