# Shamir Secret Sharing Implementation 🔐

This repo demonstrates a simple and clear implementation of **Shamir Secret Sharing (SSS)**.
Shamir Secret Sharing is a cryptographic technique that allows a "secret" to be divided into multiple "shares", where only a minimum number of those shares (threshold `t`) are required to reconstruct the original secret. This is useful for secure key management and fault tolerance in distributed systems.

## 🔧 Files Overview

| File              | Description |
|-------------------|-------------|
| `main.py`         | Main script to generate and reconstruct a shared secret. |
| `shamir_utils.py` | Functions to generate Shamir shares using random polynomials. |
| `reconstruct.py`  | Functions to reconstruct the secret using Lagrange interpolation. |

---

## 🚀 Run the Demo
```bash
python main.py


