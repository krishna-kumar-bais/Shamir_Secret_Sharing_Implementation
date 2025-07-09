# Shamir Secret Sharing Implementation 🔐

This project demonstrates a simple and clear implementation of **Shamir Secret Sharing (SSS)** using Python.

Shamir Secret Sharing is a cryptographic technique that allows a "secret" to be divided into multiple "shares", where only a minimum number of those shares (threshold `t`) are required to reconstruct the original secret. This is useful for secure key management and fault tolerance in distributed systems.

## 🔧 Files Overview

| File              | Description |
|-------------------|-------------|
| `sss_demo.py`     | Main script to generate and reconstruct a shared secret. |
| `shamir_utils.py` | Functions to generate Shamir shares using random polynomials. |
| `reconstruct.py`  | Functions to reconstruct the secret using Lagrange interpolation. |

---

## 📖 How It Works

1. **Secret Sharing:**
   - Given a secret (integer), it is embedded as the constant term of a randomly generated polynomial of degree `t - 1`.
   - The polynomial is evaluated at `n` different `x` values (typically 1 to n), generating `n` shares.

2. **Reconstruction:**
   - Using any `t` of the `n` shares, the secret can be recovered by evaluating the polynomial at `x = 0` using **Lagrange interpolation**.
   - Fewer than `t` shares reveal no information about the secret.

---

## 🚀 Run the Demo
```bash
python sss_demo.py


