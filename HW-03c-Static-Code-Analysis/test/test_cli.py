import pytest
from src.main import main

def run_main_with_input(monkeypatch, capsys, inputs):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    main()
    return capsys.readouterr().out

def test_cli_valid_triangle(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, ["3", "4", "5"])
    assert "Welcome to the Triangle Classifier!" in output
    assert "classified as: Scalene and Right" in output

def test_cli_equilateral(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, ["2", "2", "2"])
    assert "classified as: Equilateral" in output

def test_cli_invalid_input(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, ["a", "2", "3"])
    assert "Invalid input. Please enter numeric values for the sides." in output

def test_cli_not_a_triangle(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, ["1", "2", "3"])
    assert "classified as: Not a triangle" in output