import random

def eval_polynomial(coeffs, x, prime):
    """Evaluates a polynomial at x with coefficients over a finite field (mod prime)."""
    result = 0
    for power, coeff in enumerate(coeffs):
        result += coeff * pow(x, power, prime)
        result %= prime
    return result

def secret_share(secret, t, n, prime):
    """
    Generates n Shamir secret shares.
    - secret: integer to share
    - t: threshold number of shares needed to reconstruct
    - n: total number of shares to generate
    - prime: a prime number larger than secret
    Returns: list of (x, y) tuples
    """
    if secret >= prime:
        raise ValueError("Secret must be less than prime.")

    # Generate random coefficients for a degree-(t-1) polynomial
    coeffs = [secret] + [random.randint(0, prime - 1) for _ in range(t - 1)]
    
    # Create n shares
    shares = []
    for i in range(1, n + 1):
        x = i
        y = eval_polynomial(coeffs, x, prime)
        shares.append((x, y))

    return shares
