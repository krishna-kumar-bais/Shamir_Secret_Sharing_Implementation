from shamir_utils import secret_share
from reconstruct import reconstruct

# Step 1: Define helper to pick the next prime greater than the secret
def next_prime(n):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True

    while True:
        n += 1
        if is_prime(n):
            return n

# Step 1: Define parameters
secret = 123423             # The secret to be shared
t = 5                       # Minimum number of shares needed to reconstruct the secret
n = 10                      # Total number of shares to generate
prime = next_prime(secret)  # Prime modulus

print(f"Original secret: {secret}")
print(f"Threshold: {t}, Total shares: {n}, Prime: {prime}")

# Step 2: Generate shares
shares = secret_share(secret, t, n, prime)
print("\nGenerated Shares:")
for idx, (x, y) in enumerate(shares, start=1):
    print(f"Share {idx}: (x={x}, y={y})")

# Step 3: Choose specific shares by index (0-based indexing)
selected_indices = [0, 2, 3, 4, 5]  # Corresponds to shares 1, 3, 4, 5, 6
selected_shares = [shares[i] for i in selected_indices]

print(f"\nUsing shares at indices: {[i + 1 for i in selected_indices]} to reconstruct:")

# Step 4: Reconstruct the secret
recovered_secret = reconstruct(selected_shares, prime)
print(f"\n✅ Reconstructed secret: {recovered_secret}")

# Step 5: Check correctness
assert recovered_secret == secret, "❌ Reconstruction failed! Mismatch!"
print("✅ Secret successfully reconstructed!")
