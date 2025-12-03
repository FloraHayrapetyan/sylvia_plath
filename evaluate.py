from metrics.wer import wer, cer
from metrics.bleu import bleu_score

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def main():
    ref = load_text("reference.txt")
    hyp = load_text("hypothesis.txt")

    print("=== Evaluation Results ===\n")
    print(f"Reference: {ref[:100]}...")
    print(f"Hypothesis: {hyp[:100]}...\n")

    wer_score = wer(ref, hyp)
    cer_score = cer(ref, hyp)
    bleu = bleu_score(ref, hyp)

    print(f"WER  : {wer_score:.3f}")
    print(f"CER  : {cer_score:.3f}")
    print(f"BLEU : {bleu:.3f}")

if __name__ == "__main__":
    main()
