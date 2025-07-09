def lagrange_interpolation(x, x_s, y_s, prime):
    """
    Computes Lagrange interpolation at the point x given known points (x_s, y_s)
    under a finite field with modulo prime.
    """
    total = 0
    k = len(x_s)
    for i in range(k):
        xi, yi = x_s[i], y_s[i]

        # Compute the Lagrange basis polynomial L_i(x)
        li_num = 1
        li_den = 1
        for j in range(k):
            if i == j:
                continue
            xj = x_s[j]
            li_num = (li_num * (x - xj)) % prime
            li_den = (li_den * (xi - xj)) % prime

        # Modular inverse of denominator
        li = li_num * pow(li_den, -1, prime)
        li %= prime

        total += yi * li
        total %= prime

    return total

def reconstruct(shares, prime):
    """
    Reconstruct the original secret from the given shares using Lagrange interpolation.
    - shares: list of (x, y) tuples
    - prime: same prime number used during secret sharing
    Returns the recovered secret (an integer).
    """
    x_s, y_s = zip(*shares)
    return lagrange_interpolation(0, x_s, y_s, prime)
