from GenerateShare import GenerateShare
from ReconstructSecret import ReconstructSecret


def main():
    # Example parameters
    secret = 1233456
    t = 3          # threshold
    n = 5          # total shares
    prime = 2147483647  # prime

    shares = GenerateShare(secret, t, n, prime)
    print("All shares:")
    for x, y in shares:
        print(f"(x={x}, y={y})")

    # Reconstruct the secret from any t shares (here: first t shares)
    subset = [shares[i] for i in range(0, t)] # share :0,1,..,t-1
    reconstructed = ReconstructSecret(subset, prime)
    print(f"\nReconstructed secret from {t} shares: {reconstructed}")


if __name__ == "__main__":
    main()


