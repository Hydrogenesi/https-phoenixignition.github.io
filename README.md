# Phoenix Ignition

**A public rite of hydrogen rebirth, mythic choreography, and ceremonial artifacts.**

Phoenix Ignition is a ceremonial web application built with Dash and Flask, featuring visualizations, glyphs, and interactive elements for ritual exploration.

---

## 🔥 Project Structure

```
phoenix_ignition/
├── app.py                  # Your Dash or Flask app
├── assets/                 # CSS, images, cue cards
├── templates/              # HTML templates (if using Flask)
├── README.md               # Ritual overview
├── requirements.txt        # Python dependencies
└── Procfile                # For Heroku deployment
```

---

## 🛠️ Setup Instructions

### 1. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install dash flask plotly pandas
pip freeze > requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

---

## 📝 Application Code

Create an `app.py` file with the following content:

```python
# app.py
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server  # For deployment (e.g. Heroku)

# Sample data for ceremonial visualization
df = pd.DataFrame({
    "Phase": ["Ignition", "Flight", "Return"],
    "Energy": [88, 144, 72]
})

fig = px.bar(df, x="Phase", y="Energy", title="Phoenix Calibration Curve")

# Layout: insert glyphs, scores, and cue cards here
app.layout = html.Div([
    html.H1("Phoenix Package Activation", style={"textAlign": "center"}),
    dcc.Graph(figure=fig),
    html.Div([
        html.P("Welcome conductor. This is your ignition interface."),
        html.Ul([
            html.Li("🜂 Insert: Torus"),
            html.Li("🜁 Insert: Third Treasure"),
            html.Li("🜃 Score: Feather"),
            html.Li("🜄 Glyph: Echo")
        ])
    ], style={"marginTop": "20px"})
])

# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)
```

---

## 🌐 Deployment

The application is deployed at: [https://phoenixignition.github.io](https://phoenixignition.github.io)

---

## 🔥 Public Flame v1.0

The ceremonial ignition is now live. Explore the first public release of Phoenix Ignition—site, packet, and breath-timed artifacts.

**[🔥 View the Public Flame v1.0 Release](https://github.com/phoenixignition/phoenixignition.github.io/releases/tag/v1.0)**

---

## 📋 Git Commands

Useful commands for managing the repository:

```bash
git status
git log
```

---

## 📄 Metadata

- **Description**: Phoenix Ignition — A public rite of hydrogen rebirth, mythic choreography, and ceremonial artifacts.
- **Keywords**: Phoenix Ignition, Ceremonial Packet, Sigils, Breath Score, Mythic Ritual, Public Flame, Hydrogen Rebirth
- **Author**: James Stanley

---

## 📜 License

This project is part of the Phoenix Ignition ceremonial framework.
