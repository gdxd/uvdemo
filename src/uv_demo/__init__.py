import numpy as np


def invariant_mass(E, px, py, pz):
    """Invariant mass m = sqrt(E^2 - |p|^2) (natural units)."""
    return np.sqrt(np.maximum(E**2 - (px**2 + py**2 + pz**2), 0.0))


def main() -> None:
    # Two photons from a pi0 decay at rest (GeV)
    E = np.array([0.0675, 0.0675])
    px = np.array([0.0675, -0.0675])
    py = pz = np.zeros(2)
    m = invariant_mass(E.sum(), px.sum(), py.sum(), pz.sum())
    print(f"Invariant mass: {m * 1000:.1f} MeV")
