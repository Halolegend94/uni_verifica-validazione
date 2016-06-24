
import math

def trials_number(confidence, margin):
    """
    confidence: probability of not finding an error
    margin: lower bound to probability of error

    The probability that margin is an over-estimate is bounded by
    confidence.
    """
    assert 0.0 < confidence <= 1.0
    assert 0.0 < margin < 1.0
    return int(math.ceil(math.log(confidence) / math.log(1 - margin)))

