"""
explanation_module.py
----------------------
Uses the lightweight, local LaMini-Flan-T5-783M model to generate
simple, easy-to-understand explanations of any concept.
Runs on CPU, so no GPU is required (works fine on Mac M1 too).
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load the instruction-tuned model for explanations (downloads once, then cached)
explain_tokenizer = AutoTokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
explain_model = AutoModelForSeq2SeqLM.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")


def explain_topic(topic: str) -> str:
    """Generate a simple explanation of a topic for a school-level learner."""
    input_text = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
    inputs = explain_tokenizer(input_text, return_tensors="pt")

    outputs = explain_model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        do_sample=True
    )

    explanation = explain_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return explanation
