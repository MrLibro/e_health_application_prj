import dash
import dash_core_components as dcc
import dash_html_components as html




layout_subject_number = html.Div(
    [
        html.I("Try typing in input 1 & 2, and observe how debounce is impacting the callbacks. Press Enter and/or Tab key in Input 2 to cancel the delay"),
        html.Br(),
        dcc.Input(id="medical_subject", type="text", placeholder=""),
        dcc.Input(id="numberOfPapers", type="text", placeholder="", debounce=True),
        html.Button(id='show_result_btn', n_clicks=0, children='Go'),
        html.Div(id="lookup_result"),
    ]
)