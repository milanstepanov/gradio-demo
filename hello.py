"""'Docstring for gradio-demo.hello"""

import gradio as gr


def greet(name: str, intensity: int):
    """'Generate greeting.

    :param name: Name to greet.
    :type str:
    :param intensity:
    :type int:
    :return: Hello greeting.
    :rtype: str"""

    return f"Hello, {name}" + "!" * int(intensity)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
