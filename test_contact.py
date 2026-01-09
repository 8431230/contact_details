import subprocess
import sys


def test_no_input():
    result = subprocess.run(
        [sys.executable, "contact.py"],
        capture_output=True,
        text=True
    )
    assert "no input given - using default values:" in result.stdout


def test_local_contact():
    result = subprocess.run(
        [
            sys.executable,
            "contact.py",
            "soumya",
            "9876543210",
            "soumyal@gmail.com",
            "Hubballi",
            "auto"
        ],
        capture_output=True,
        text=True
    )
    assert "Local Contact" in result.stdout


def test_non_local_contact():
    result = subprocess.run(
        [
            sys.executable,
            "contact.py",
            "Anita",
            "8888888888",
            "anita@gmail.com",
            "Bangalore",
            "auto"
        ],
        capture_output=True,
        text=True
    )
    assert "Non-Local Contact" in result.stdout