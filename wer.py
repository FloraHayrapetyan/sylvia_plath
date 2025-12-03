import numpy as np

def wer(reference: str, hypothesis: str) -> float:
    """Compute Word Error Rate (WER)."""
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    n, m = len(ref_words), len(hyp_words)
    d = np.zeros((n + 1, m + 1))

    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if ref_words[i - 1] == hyp_words[j - 1] else 1
            d[i][j] = min(
                d[i - 1][j] + 1,        # deletion
                d[i][j - 1] + 1,        # insertion
                d[i - 1][j - 1] + cost  # substitution
            )

    return d[n][m] / max(n, 1)


def cer(reference: str, hypothesis: str) -> float:
    """Compute Character Error Rate (CER)."""
    ref_chars = list(reference)
    hyp_chars = list(hypothesis)
    n, m = len(ref_chars), len(hyp_chars)
    d = np.zeros((n + 1, m + 1))

    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if ref_chars[i - 1] == hyp_chars[j - 1] else 1
            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + cost
                
            )


    return d[n][m] / max(n, 1)
