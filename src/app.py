from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_mantine_components as dmc
import joblib
import gspread
from datetime import datetime
from dotenv import load_dotenv, dotenv_values
import os
# Load the model


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
                {"label": "A", "value": "A"},
                {"label": "AB", "value": "AB"},
                {"label": "B", "value": "B"},
                {"label": "O", "value": "O"},
                {"label": "Tidak Tau", "value": "Tidak Tau"},
            ],
            value= 6,
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
                {"label": "Positif (+)", "value": "Positif (+)"},
                {"label": "Negatif (-)", "value": "Negatif (-)"},
                {"label": "Tidak Tau", "value": "Tidak Tau"},
            ],
            value= 6,
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
                {"label": "1", "value": 1},
                {"label": "2", "value": 2},
                {"label": "3", "value": 3},
                {"label": "4", "value": 4},
                {"label": "5 atau lebih", "value": 5},
            ],
            value=7,
            id="radioitems-inline-input_3",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('6. Jumlah Riwayat Caesar'), 
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "0", "value": 0},
                {"label": "1", "value": 1},
                {"label": "2", "value": 2},
                {"label": "3", "value": 3},
                {"label": "4 atau lebih", "value": 4},
            ],
            value=5,
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
                {"label": "0", "value": 0},
                {"label": "1", "value": 1},
                {"label": "2", "value": 2},
                {"label": "3 atau lebih", "value":3},
            ],
            value=5,
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
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            
            ],
            value=2,
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
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            ],
            value=3,
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
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            
            ],
            value=3,
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
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            ],
            value=3,
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
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            
            ],
            value=4,
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
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            ],
            value=3,
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
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            
            ],
            value=3,
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
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            ],
            value=3,
            id="radioitems-inline-input_13",
            inline=True,
        ),
        dbc.FormText(""),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
        dbc.Col([
            html.Label('16. Apakah Anda Memiliki Riwayat Kelainan Bawaan?'),
            html.Br(),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            
            ],
            value=3,
            id="radioitems-inline-input_14",
            inline=True,
        ),
        ], width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("17. Apakah Anda Memiliki Riwayat Alergi?"),
        dbc.RadioItems(
            options=[
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            ],
            value=3,
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
                {"label": "Ya", "value": "Ya"},
                {"label": "Tidak", "value": "Tidak"},
            
            ],
            value=3,
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
                    {"label": "Preeklampsi", "value": "Preeklampsi"},
                    {"label": "Lainnya", "value": 'Lainnya'},
                ],
                value=[],
                id="Checklist-inline-input_17",
                inline=True,
            ),
            dcc.Input(id='lainnya-input', placeholder='Enter custom penyakit', style={'display': 'none'}),
            dbc.FormText(""),
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
                    {"label": "Preeklampsi", "value": "Preeklampsi"},
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
            dmc.TextInput(id="nama-bidan", label="21. Info Dari Bidan:", error=False),
        ], width={'size': 12, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0})
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
    width={'size': 10, 'order': 1, 'offset': 1}, lg={'size': 6, 'order': 1, 'offset': 0}),
    
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
     State("your-usia-ibu-input-id", "value"), # usia_ibu_value
     State("your-usia-kandungan-input-id", "value"),# usia_ibu_value# usia_ibu_value
     State("radioitems-inline-input_1", "value"),# golongan darah
     State("radioitems-inline-input_2", "value"),# rhesus
     State("radioitems-inline-input_3", "value"),# hamil_ke_brp
     State("radioitems-inline-input_4", "value"),# riwayat_caesar
     State("radioitems-inline-input_5", "value"),# jumlah_keguguran
     State("radioitems-inline-input_6", "value"),# kehamilan_diinginkan
     State("radioitems-inline-input_7", "value"),# alkohol
     State("radioitems-inline-input_8", "value"),# rokok
     State("radioitems-inline-input_9", "value"),# narcoboy
     State("radioitems-inline-input_10", "value"),# polusi
     State("radioitems-inline-input_11", "value"),# riwayat_pendarahan
     State("radioitems-inline-input_12", "value"),# pedarahan_ketika
     State("radioitems-inline-input_13", "value"),# gadget
     State("radioitems-inline-input_14", "value"),# riwayat_kelainan
     State("radioitems-inline-input_15", "value"),# riwayat_alergi
     State("radioitems-inline-input_16", "value"),# pernah_caesar
     State("Checklist-inline-input_17", "value"),# riwayat_penyakit
     State("Checklist-inline-input_18", "value"),
     State("nama-bidan", "value")]# penyakit_turunan
)
def update_layout(selected_options_17, selected_options_18, n, is_open, usia_ibu_value, usia_kandungan_value, golongan_darah, rhesus, hamil_ke_brp, riwayat_caesar, jumlah_keguguran, kehamilan_diinginkan, alkohol, rokok, narkoba, polusi, riwayat_pendarahan, pedarahan_ketika, gadget, riwayat_kelainan, riwayat_alergi, pernah_caesar,riwayat_penyakit, penyakit_turunan, nama_bidan):
    # Callback for showing/hiding custom input
    style_lainnya_input = {'display': 'block'} if 'Lainnya' in selected_options_17 else {'display': 'none'}
    style_lainnya_input_turunan = {'display': 'block'} if 'Lainnya' in selected_options_18 else {'display': 'none'}

    # Callback for collapsing/expanding section
    if n:
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        config = dotenv_values("/etc/secrets/.env")
        client = gspread.service_account(filename=config)
        sheets = client.open_by_key('1UMOEJvUrcuCOWZPiMpWlpEcIMKIm3p8eSBq0HjaFsmI')
        x = sheets.get_worksheet(0)
        riwayat_penyakit_join = ', '.join(riwayat_penyakit)
        penyakit_turunan_join = ', '.join(penyakit_turunan)
        data_to_add = [formatted_datetime, nama_bidan, usia_ibu_value, usia_kandungan_value, golongan_darah, rhesus, hamil_ke_brp, riwayat_caesar, jumlah_keguguran, kehamilan_diinginkan, alkohol, rokok, narkoba, polusi, riwayat_pendarahan, pedarahan_ketika, gadget, riwayat_kelainan, riwayat_alergi, pernah_caesar ,riwayat_penyakit_join, penyakit_turunan_join]
        x.append_row(data_to_add)
        
        with open('rf_classifier.pkl', 'rb') as file:
            rf_classifier = joblib.load(file)

        usia_ibu_value = 2 if usia_ibu_value < 20 or usia_ibu_value > 40 else (1 if 31 <= usia_ibu_value <= 40 else 0)
        usia_kandungan_value = 2 if usia_kandungan_value == 1 else (1 if usia_kandungan_value == 2 else 0)
        golongan_darah = 3 if golongan_darah == 'O' else (0 if golongan_darah == 'A' else (4 if golongan_darah == 'Tidak Tau' else (2 if golongan_darah == 'B' else 1)))
        rhesus = 1 if rhesus == 'Positif (+)' else (2 if rhesus == 'Tidak Tau' else (0 if rhesus == 'Negatif (-)' else None))
        kehamilan_diinginkan = 1 if kehamilan_diinginkan == 'Ya' else (0 if kehamilan_diinginkan == "Tidak" else None)
        alkohol = 1 if alkohol == 'Ya' else (0 if alkohol == "Tidak" else None)
        rokok = 1 if rokok == 'Ya' else (0 if rokok == "Tidak" else None)
        narkoba = 1 if narkoba == 'Ya' else (0 if narkoba == "Tidak" else None)
        polusi = 1 if polusi == 'Ya' else (0 if polusi == "Tidak" else None)
        riwayat_pendarahan = 1 if riwayat_pendarahan == 'Ya' else (0 if riwayat_pendarahan == "Tidak" else None)
        pedarahan_ketika = 1 if pedarahan_ketika == 'Ya' else (0 if pedarahan_ketika == "Tidak" else None)
        gadget = 1 if gadget == 'Ya' else (0 if gadget == "Tidak" else None)
        riwayat_kelainan = 1 if riwayat_kelainan == 'Ya' else (0 if riwayat_kelainan == "Tidak" else None)
        riwayat_alergi = 1 if riwayat_alergi == 'Ya' else (0 if riwayat_alergi == "Tidak" else None)
        pernah_caesar = 1 if pernah_caesar == 'Ya' else (0 if pernah_caesar == "Tidak" else None)
        riwayat_penyakit = 0 if riwayat_penyakit[0] == 'Tidak Ada' else 1
        penyakit_turunan = 0 if penyakit_turunan[0] == 'Tidak Ada' else 1
        #print(usia_ibu_value, usia_kandungan_value, golongan_darah,rhesus,hamil_ke_brp,jumlah_keguguran,kehamilan_diinginkan,alkohol,rokok,narkoba,polusi,riwayat_pendarahan,pedarahan_ketika,gadget,riwayat_kelainan,riwayat_alergi,pernah_caesar,riwayat_caesar, riwayat_penyakit,penyakit_turunan)

        prediction = rf_classifier.predict([[usia_ibu_value, usia_kandungan_value, golongan_darah,rhesus,hamil_ke_brp,jumlah_keguguran,kehamilan_diinginkan,alkohol,rokok,narkoba,polusi,riwayat_pendarahan,pedarahan_ketika,gadget,riwayat_kelainan,riwayat_alergi,pernah_caesar,riwayat_caesar, riwayat_penyakit,penyakit_turunan]])
        prediction = 'Tinggi' if prediction == 0 else ('Normal' if prediction == 1 else 'Rendah')
        
        # output_text = f"Janin: {'Beresiko' if score >= 1 else 'Normal'}"
        output_text = f"Janin beresiko: {prediction}"

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
    app.run_server(port=8011)


