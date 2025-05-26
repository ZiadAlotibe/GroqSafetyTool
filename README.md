echo "# GroqSafe Project

GroqSafe Project is a Python package designed to help detect prompt injection attempts and flag unsafe content.  
It combines powerful local machine learning models (from the transformers library) with the Groq Llama Guard API to enhance content safety by categorizing risks into specific hazard codes.

⚠ **Note:** This is still a prototype and does not guarantee full protection against all prompt injection attacks.

---

## Key Features

- **Prompt Injection Detection:** Uses fine-tuned models like DeBERTa, DistilBERT, or ONNX to flag suspicious text.
- **Groq Llama Guard Integration:** Connects with Groq’s API to identify risks like violence, hate speech, privacy issues, and more.
- **Customizable Setup:** Choose between local or API detection, adjust thresholds, or plug in your own models.
- **Hazard Categories (Groq):** Supports detection across codes like S1 (Violence), S5 (Defamation), S7 (Privacy), S10 (Hate), etc.

---

## Installation

Using pip:
\`\`\`bash
pip install pytector
\`\`\`

For GGUF local model support:
\`\`\`bash
pip install pytector[gguf]
\`\`\`

Or install directly from source:
\`\`\`bash
git clone https://github.com/ZiadAlotibe/Groq_pytector_project.git
cd Groq_pytector_project
pip install .
\`\`\`

---

## Usage

### Example 1: Local Model
\`\`\`python
from pytector import PromptInjectionDetector

detector = PromptInjectionDetector(model_name_or_url=\"deberta\")
is_injection, prob = detector.detect_injection(\"Your prompt here\")
print(f\"Injection: {is_injection}, Probability: {prob}\")
\`\`\`

### Example 2: Groq API
\`\`\`python
import os
from pytector import PromptInjectionDetector

api_key = os.getenv(\"GROQ_API_KEY\")
if api_key:
    detector = PromptInjectionDetector(use_groq=True, api_key=api_key)
    is_safe, hazard = detector.detect_injection_api(\"Sensitive request here\")
    print(f\"Safe: {is_safe}, Hazard Code: {hazard}\")
else:
    print(\"GROQ_API_KEY not set.\")
\`\`\`

---

## Testing

Set up and run tests:
\`\`\`bash
pip install -e \".[test]\"
pytest -v
\`\`\`

Groq API tests require \`GROQ_API_KEY\`.  
GGUF tests require installing \`llama-cpp-python\` and setting the \`PYTECTOR_TEST_GGUF_PATH\`.

---

