"""'Docstring for gradio-demo.hello"""

import gradio as gr
from mylib.greet import greet

demo = gr.Interface(
    fn=greet,
    inputs=["text", gr.Slider(value=2, minimum=1, maximum=10, step=1)],
    outputs=[gr.Textbox(label="greeting", lines=3)],
)

demo.launch()
