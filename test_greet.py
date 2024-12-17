"""'Docstring for gradio-demo.test_hello"""

from collections import Counter
from mylib.greet import greet


def test_hello_name():
    """'Docstring for test_hello_name"""
    name = "Bob"
    intensity = 2
    assert name in greet(name, intensity)


def test_hello_intensity():
    """'Docstring for test_hello_intensity"""
    name = "Bob"
    cnt = Counter(name)
    intensity = 2
    assert "!" * (int(intensity) + cnt["!"]) in greet(name, intensity)
