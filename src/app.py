from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_mantine_components as dmc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    dbc.Row([
       dbc.Col([
           html.H1("Fetus Prediction App", className="mb-4 mt-5 text-center")
       ], width=12)
    ], justify="center"),
    
    dbc.Row([
        dbc.Col([
        dmc.NumberInput(id="your-usia-ibu-input-id", label="1. Usia Ibu:",  min=10, max=50),
        ], width={'size': 12, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        
        dbc.Col([
            dmc.NumberInput(id="your-usia-kandungan-input-id", label="2. Usia Kandungan:",  min=1, max=40),
        ], width={'size': 12, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("3. Golongan Darah"),
        dbc.RadioItems(
            options=[
                {"label": "A", "value": 'A'},
                {"label": "AB", "value": 'AB'},
                {"label": "B", "value": 'B'},
                {"label": "O", "value": 'O'},
                {"label": "Tidak Tau", "value": 'Tidak Tau'},
            ],
            value="",
            id="radioitems-inline-input_1",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 12, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('4. Rhesus'),
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "Postitif (+)", "value": 'Postitif'},
                {"label": "Negatif (-)", "value": 'Negatif'},
                {"label": "Tidak Tau", "value": 'Tidak Tau'},
            ],
            value="",
            id="radioitems-inline-input_2",
            inline=True,
        ),
        ], width={'size': 12, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("5. Hamil ke Berapa"),
        dbc.RadioItems(
            options=[
                {"label": "1", "value": '1'},
                {"label": "2", "value": '2'},
                {"label": "3", "value": '3'},
                {"label": "4 atau lebih", "value": '4 atau lebih'},
            ],
            value="",
            id="radioitems-inline-input_3",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('6. Jumlah Persalinan'),
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "0", "value": '0'},
                {"label": "1", "value": '1'},
                {"label": "2", "value": '2'},
                {"label": "3", "value": '3'},
                {"label": "4 atau lebih", "value": '4 atau lebih'},
            ],
            value="",
            id="radioitems-inline-input_4",
            inline=True,
        ),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("7. Jumlah Keguguran"),
        dbc.RadioItems(
            options=[
                {"label": "0", "value": '0'},
                {"label": "1", "value": '1'},
                {"label": "2", "value": '2'},
                {"label": "3 atau lebih", "value": '3 atau lebih'},
            ],
            value="",
            id="radioitems-inline-input_5",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('8. Apakah Kehamilan Ini Diinginkan?'),
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            
            ],
            value="",
            id="radioitems-inline-input_6",
            inline=True,
        ),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("9. Apakah Anda Pengguna Alkohol? "),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            ],
            value="1",
            id="radioitems-inline-input_7",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('10. Apakah Anda Perokok?'),
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            
            ],
            value="",
            id="radioitems-inline-input_8",
            inline=True,
        ),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("11. Apakah Anda Pengguna Narkoba?"),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            ],
            value="1",
            id="radioitems-inline-input_9",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('12. Apakah Anda Sering Terpapar Polusi? (Asap Rokok, Mengendarai / Penumpang Motor)'),
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            
            ],
            value="",
            id="radioitems-inline-input_10",
            inline=True,
        ),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("13. Apakah Anda Memiliki Riwayat Pendarahan Pasca Lahir?"),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            ],
            value="",
            id="radioitems-inline-input_11",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('14. Apakah Anda Pernah Mengalami Pendarahan Ketika Hamil?'),
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            
            ],
            value="",
            id="radioitems-inline-input_12",
            inline=True,
        ),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("15. Apakah Anda Sering Menggunakan Gadget?"),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            ],
            value="",
            id="radioitems-inline-input_13",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('16. Apakah Anda Memilikin Riwayat Kelainan Bawaan?'),
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            
            ],
            value="",
            id="radioitems-inline-input_14",
            inline=True,
        ),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("17. Apakah Anda Memilikin Riwayat Alergi?"),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            ],
            value="",
            id="radioitems-inline-input_15",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('18. Apakah Anda Pernah Operasi Caesar?'),
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": 'Ya'},
                {"label": "Tidak", "value": 'Tidak'},
            
            ],
            value="",
            id="radioitems-inline-input_16",
            inline=True,
        ),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),
    

    dbc.Row([
        dbc.Col([
            html.Label("19. Riwayat Penyakit"),
            dbc.Checklist(
                options=[
                    {"label": "Tidak Ada", "value": 'Tidak Ada'},
                    {"label": "Diabetes", "value": 'Diabetes'},
                    {"label": "Anemia", "value": 'Anemia'},
                    {"label": "Hipertensi", "value": 'Hipertensi'},
                    {"label": "Paru-Paru", "value": 'Paru-Paru'},
                    {"label": "Ginjal", "value": 'Ginjal'},
                    {"label": "Lainnya", "value": 'Lainnya'},
                ],
                value=[],
                id="Checklist-inline-input_17",
                inline=True,
            ),
            dcc.Input(id='lainnya-input', placeholder='Enter custom penyakit', style={'display': 'none'}),
            dbc.FormText("Choose something in the box above"),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('20. Penyakit Turunan'),
            dbc.Checklist(
                options=[
                    {"label": "Tidak Ada", "value": 'Tidak Ada'},
                    {"label": "Diabetes", "value": 'Diabetes'},
                    {"label": "Anemia", "value": 'Anemia'},
                    {"label": "Hipertensi", "value": 'Hipertensi'},
                    {"label": "Paru-Paru", "value": 'Paru-Paru'},
                    {"label": "Ginjal", "value": 'Ginjal'},
                    {"label": "Lainnya", "value": 'Lainnya'},
                ],
                value=[],
                id="Checklist-inline-input_18",
                inline=True,
            ),
            dcc.Input(id='lainnya-input-turunan', placeholder='Enter custom penyakit turunan', style={'display': 'none'}),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Button("Prediksi", color="primary", className="mt-3 mb-3", id="collapse-button", n_clicks=0),
            dbc.Collapse(
                dbc.Card(dbc.CardBody(id="collapse-output")),
                id="collapse",
                is_open=False,
            ),
        ],
       width={'size': 10, 'order': 1, 'offset': 1}),
    ]),
])

@app.callback(
    [Output('lainnya-input', 'style'),
     Output('lainnya-input-turunan', 'style'),
     Output("collapse", "is_open"),
     Output("collapse-output", "children"),
     Output('Checklist-inline-input_17', 'value'),
     Output('Checklist-inline-input_17', 'disabled'),
     Output('Checklist-inline-input_18', 'value'),
     Output('Checklist-inline-input_18', 'disabled')],
    [Input('Checklist-inline-input_17', 'value'),
     Input('Checklist-inline-input_18', 'value'),
     Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open"),
     State("your-usia-ibu-input-id", "value"),
     State("your-usia-kandungan-input-id", "value"),
     State("Checklist-inline-input_17", "value"),
     State("Checklist-inline-input_18", "value"),
     State("radioitems-inline-input_1", "value"),
     State("radioitems-inline-input_2", "value"),
     State("radioitems-inline-input_3", "value"),
     State("radioitems-inline-input_4", "value"),
     State("radioitems-inline-input_5", "value")]
)
def update_layout(selected_options_17, selected_options_18, n, is_open, usia_ibu_value, usia_kandungan_value, riwayat_penyakit, penyakit_turunan, golongan_darah, rhesus, hamil_ke_brp, jumlah_persalinan, jumlah_keguguran):
    # Callback for showing/hiding custom input
    style_lainnya_input = {'display': 'block'} if 'Lainnya' in selected_options_17 else {'display': 'none'}
    style_lainnya_input_turunan = {'display': 'block'} if 'Lainnya' in selected_options_18 else {'display': 'none'}

    # Callback for collapsing/expanding section
    if n:
        score = 0
        if usia_ibu_value < 20 or usia_ibu_value > 35:
            score += 1
        if usia_kandungan_value < 4:
            score += 1
        if golongan_darah == 'Tidak Tau':
             score += 1
        if rhesus == 'Tidak Tau':
             score += 1
        if hamil_ke_brp == '4 atau lebih':
             score += 1
        if jumlah_persalinan == '4 atau lebih':
             score += 1
        if jumlah_keguguran == '3 atau lebih':
             score += 1
        if "Tidak Ada" not in  riwayat_penyakit:
            score += 1
        if "Tidak Ada" not in  penyakit_turunan:
            score += 1 
        
        
        output_text = f"Janin: {'Beresiko' if score >= 1 else 'Normal'}"


        # If 'Tidak Ada' is selected for Riwayat Penyakit, uncheck other options
        if 'Tidak Ada' in selected_options_17:
            selected_options_17 = ['Tidak Ada']
            disabled_17 = True
        else:
            disabled_17 = False

        # If 'Tidak Ada' is selected for Penyakit Turunan, uncheck other options
        if 'Tidak Ada' in selected_options_18:
            selected_options_18 = ['Tidak Ada']
            disabled_18 = True
        else:
            disabled_18 = False

        return style_lainnya_input, style_lainnya_input_turunan, not is_open, output_text, selected_options_17, disabled_17, selected_options_18, disabled_18

    # If 'Tidak Ada' is selected for Riwayat Penyakit, uncheck other options
    if 'Tidak Ada' in selected_options_17:
        selected_options_17 = ['Tidak Ada']
        disabled_17 = True
    else:
        disabled_17 = False

    # If 'Tidak Ada' is selected for Penyakit Turunan, uncheck other options
    if 'Tidak Ada' in selected_options_18:
        selected_options_18 = ['Tidak Ada']
        disabled_18 = True
    else:
        disabled_18 = False

    return style_lainnya_input, style_lainnya_input_turunan, is_open, None, selected_options_17, disabled_17, selected_options_18, disabled_18


if __name__ == '__main__':
    app.run_server(port=8002)
