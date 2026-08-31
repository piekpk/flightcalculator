import subprocess
import sys

from flight_calculator import calculate_flight_time, flight_time_table

def test_calculate_flight_time_zero():
    assert calculate_flight_time(0) == 180.0

def test_calculate_flight_time_500():
    assert calculate_flight_time(500) == 130.0

def test_flight_time_table():
    assert flight_time_table(100, 50) == [(0, 180.0), (50, 175.0), (100, 170.0)]

def test_negative_weight_raises():
    try:
        calculate_flight_time(-1)
        assert False
    except ValueError:
        pass


def test_cli_prints_flight_time_for_weight():
    result = subprocess.run(
        [sys.executable, "flight_calculator.py", "--weight", "500"],
        cwd=".",
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "130.0" in result.stdout