from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def bleu_score(reference: str, hypothesis: str) -> float:
    """Compute BLEU score between two sentences."""
    smoothie = SmoothingFunction().method4
    return sentence_bleu([reference.split()], hypothesis.split(), smoothing_function=smoothie)
