echo "# GroqSafetyTool

GroqSafetyTool is an enhanced Python tool designed to detect prompt injection attempts and flag unsafe content.  
This project integrates powerful local machine learning models (based on the transformers library) with Groq’s Llama Guard API to strengthen content safety by categorizing risks into specific hazard codes.

⚠ **Note:** This project is still evolving and does not guarantee complete protection against all prompt injection attacks.

---

## Important Notice

This project is a modified/forked version of the original **Pytector** by Max Melchior Lang.  
Significant modifications and extensions have been introduced to improve integration, usability, and customization, particularly in enterprise environments and AI governance contexts.

---

## Key Features

- **Enhanced Prompt Injection Detection:** Optimized local models like DeBERTa, DistilBERT, and ONNX for stronger accuracy.
- **Groq Llama Guard Integration:** Advanced API connection to detect sensitive risks such as violence, hate speech, or privacy breaches.
- **Improved Customization:** Flexible switching between local and cloud-based detection, with tunable thresholds.
- **Enterprise-Ready Extensions:** Adjusted for scalability, with better modularity and API handling for production settings.

---

## Installation

Using pip:
\`\`\`bash
pip install .
\`\`\`

For GGUF local model support:
\`\`\`bash
pip install .[gguf]
\`\`\`

Or install directly from source:
\`\`\`bash
git clone https://github.com/ZiadAlotibe/GroqSafetyTool.git
cd GroqSafetyTool
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

## License

This project is distributed under the MIT License, originally authored by Max Melchior Lang." > README.md

git add README.md
git commit -m "Rename project to GroqSafetyTool with updated README"
git push -u origin main
