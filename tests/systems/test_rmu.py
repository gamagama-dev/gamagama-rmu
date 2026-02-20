import argparse
from unittest.mock import patch
from gamagama.rmu.system import RMUSystem


def _create_system():
    """Helper to create an RMUSystem instance."""
    return RMUSystem()


def test_roll_rmu_normal():
    """Tests d%! in normal range (06-95)."""
    system = _create_system()

    with patch("random.randint", return_value=50):
        result = system.dice.roll(100, explode=True)

    assert result == 50


def test_roll_rmu_explode_up():
    """Tests d%! exploding upwards (96-100)."""
    system = _create_system()

    # 96 (explode) -> 50 (stop) = 146
    with patch("random.randint", side_effect=[96, 50]):
        result = system.dice.roll(100, explode=True)

    assert result == 146


def test_roll_rmu_explode_up_recursive():
    """Tests d%! exploding upwards recursively."""
    system = _create_system()

    # 99 (explode) -> 98 (explode) -> 10 (stop) = 207
    with patch("random.randint", side_effect=[99, 98, 10]):
        result = system.dice.roll(100, explode=True)

    assert result == 207


def test_roll_rmu_explode_down():
    """Tests d%! exploding downwards (01-05)."""
    system = _create_system()

    # 04 (explode down) -> 50 (stop subtraction) = 4 - 50 = -46
    with patch("random.randint", side_effect=[4, 50]):
        result = system.dice.roll(100, explode=True)

    assert result == -46


def test_roll_rmu_explode_down_recursive():
    """Tests d%! exploding downwards recursively."""
    system = _create_system()

    # 02 (explode down) -> 99 (continue subtraction) -> 50 (stop subtraction)
    # Result: 2 - (99 + 50) = 2 - 149 = -147
    with patch("random.randint", side_effect=[2, 99, 50]):
        result = system.dice.roll(100, explode=True)

    assert result == -147
