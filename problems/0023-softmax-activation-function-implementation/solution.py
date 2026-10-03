import math

def softmax(scores: list[float]) -> list[float]:
    shifted = [i - max(scores) for i in scores]
    exp = [math.exp(v) for v in shifted]
    result = [v/sum(exp) for v in exp]
    return result