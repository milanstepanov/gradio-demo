''''Docstring for gradio-demo.mylib.greet'''

def greet(name: str, intensity: int):
    """'Generate greeting.

    :param name: Name to greet.
    :type str:
    :param intensity:
    :type int:
    :return: Hello greeting.
    :rtype: str"""

    return f"Hello, {name}" + "!" * int(intensity)
