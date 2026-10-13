"""Statistics register map of the KOSPEL PPE4 (see PROTOCOL.md).

Every counter is a 32-bit value stored as a lo/hi register pair.
Energy counters are in Wh, water counters in 0.1 l.
"""
from __future__ import annotations

ENERGY_TODAY = 1450  # first of 31 daily pairs, today first
ENERGY_YEAR = 1514
ENERGY_TOTAL = 1518
ENERGY_MONTHS = 1520  # 12 monthly pairs of the current year, January first

WATER_TODAY = 1578
WATER_YEAR = 1642
WATER_TOTAL = 1646
WATER_MONTHS = 1648


def pair(data: dict[int, int], register: int) -> int | None:
    """Return the 32-bit counter starting at `register`, or None if not read yet."""
    lo = data.get(register)
    if lo is None:
        return None
    return lo + data.get(register + 1, 0) * 65536


def month_register(base: int, month: int) -> int:
    """Register of the given calendar month (1-12) in a January-first block."""
    return base + 2 * (month - 1)
