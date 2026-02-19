"""
Calculatrice Python - Projet CI/CD
Des fonctions arithmetiques de base avec gestion des erreurs.
"""


def add(a, b):
    """Additionne deux nombres."""
    return a + b


def subtract(a, b):
    """Soustrait b de a."""
    return a - b


def multiply(a, b):
    """Multiplie deux nombres."""
    return a * b


def divide(a, b):
    """Divise a par b."""
    if b == 0:
        raise ValueError("Division par zero impossible.")
    return a / b


if __name__ == "__main__":
    print("=== Calculatrice Python ===")
    print(f"  8 + 3  = {add(8, 3)}")
    print(f"  8 - 3  = {subtract(8, 3)}")
    print(f"  8 x 3  = {multiply(8, 3)}")
    print(f"  8 / 3  = {divide(8, 3):.2f}")
