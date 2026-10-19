from uv_demo import invariant_mass


def test_particle_at_rest():
    assert invariant_mass(1.0, 0.0, 0.0, 0.0) == 1.0


def test_massless():
    assert invariant_mass(5.0, 3.0, 4.0, 0.0) == 0.0
