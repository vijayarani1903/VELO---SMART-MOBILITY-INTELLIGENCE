import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="VELO | Smart Mobility Intelligence",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. CUSTOM CSS - DARK VELO THEME
# ============================================================

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: #0b1220 !important;
    color: #eef5f4 !important;
}

header[data-testid="stHeader"] {
    background: #0b1220 !important;
    border-bottom: 1px solid #1d2b40 !important;
}

/* =========================================
   TOP RIGHT MENU - DARK THEME FIX
========================================= */

[data-testid="stToolbar"] {
    background-color: #0b1220 !important;
}

[data-testid="stMainMenu"] button {
    background-color: #142237 !important;
    color: #65d6ad !important;
    border: 1px solid #34475e !important;
    border-radius: 8px !important;
}

div[data-baseweb="popover"],
div[data-baseweb="popover"] > div,
div[data-baseweb="menu"],
[role="menu"],
[data-testid="stMainMenuPopover"] {
    background-color: #142237 !important;
    color: #eef5f4 !important;
    border-color: #34475e !important;
}

[role="menu"] *,
[role="menuitem"] *,
[data-testid="stMainMenuPopover"] * {
    color: #eef5f4 !important;
}

[role="menuitem"],
[role="menu"] > div,
div[data-baseweb="menu"] > div,
div[data-baseweb="menu"] li {
    background-color: #142237 !important;
}

[role="menuitem"]:hover,
[role="menuitem"]:hover *,
div[data-baseweb="menu"] li:hover {
    background-color: #254b49 !important;
    color: #65d6ad !important;
}

[role="menuitem"][aria-disabled="true"],
[role="menuitem"][aria-disabled="true"] * {
    background-color: #142237 !important;
    color: #a9c0c4 !important;
    opacity: 1 !important;
}

[data-testid="stAppDeployButton"] {
    background-color: #142237 !important;
    color: #65d6ad !important;
}

[data-testid="stAppDeployButton"] * {
    color: #65d6ad !important;
}

/* GENERAL LAYOUT */

[data-testid="stDecoration"] {
    display: none !important;
}

.block-container {
    padding-top: 1.4rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1450px;
}

/* SIDEBAR */

[data-testid="stSidebar"],
[data-testid="stSidebar"] > div:first-child {
    background: #101c2e !important;
}

[data-testid="stSidebar"] {
    border-right: 1px solid #25364b;
}

[data-testid="stSidebar"] label {
    color: #dce8f3 !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] p {
    color: #9aafc2;
}

[data-testid="stSidebar"] hr {
    border-color: #26384d !important;
}

/* DROPDOWNS */

[data-baseweb="select"] > div {
    background: #1a2a40 !important;
    border: 1px solid #34475e !important;
    border-radius: 10px !important;
    color: white !important;
}

[data-baseweb="select"] * {
    color: white !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"],
[role="listbox"],
[role="option"] {
    background: #17263a !important;
    color: white !important;
}

[role="option"]:hover {
    background: #284b51 !important;
}

/* SLIDERS */

[data-testid="stSlider"] [role="slider"] {
    background: #65d6ad !important;
    border-color: #65d6ad !important;
}

/* BUTTONS */

div.stButton > button,
[data-testid="stDownloadButton"] button {
    background: #65d6ad !important;
    color: #09221d !important;
    border: none !important;
    border-radius: 11px !important;
    min-height: 46px;
    font-weight: 800 !important;
}

div.stButton > button:hover,
[data-testid="stDownloadButton"] button:hover {
    background: #8aefca !important;
    color: #09221d !important;
}

[data-testid="stDownloadButton"] button {
    width: 100%;
}

/* HEADER */

.velo-brand {
    color: #65d6ad;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 3px;
}

.velo-hero {
    color: #f0f6f5;
    font-size: clamp(30px, 4vw, 44px);
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 4px 0;
}

.velo-hero span {
    color: #65d6ad;
}

.velo-description {
    color: #9aafc2;
    font-size: 15px;
    margin-bottom: 28px;
}

/* SECTIONS */

.velo-section {
    color: #eef5f4;
    font-size: 19px;
    font-weight: 700;
    margin: 12px 0 15px;
}

/* OVERVIEW CARDS */

.velo-card {
    background: #142237;
    border: 1px solid #26384d;
    border-radius: 16px;
    padding: 19px;
    min-height: 137px;
    box-sizing: border-box;
}

.velo-card-label {
    color: #92a6b8;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .8px;
}

.velo-card-value {
    color: #65d6ad;
    font-size: 26px;
    font-weight: 800;
    margin-top: 10px;
}

.velo-card-note {
    color: #9aafc2;
    font-size: 12px;
    margin-top: 7px;
}

/* PREDICTION RESULT */

.velo-result {
    background: linear-gradient(130deg, #153d3b, #142b36);
    border: 1px solid #2a6257;
    border-radius: 20px;
    padding: 28px;
}

.velo-result-label {
    color: #a8c7bd;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 700;
}

.velo-result-number {
    color: #75e6bd;
    font-size: clamp(42px, 6vw, 60px);
    font-weight: 800;
    letter-spacing: -2px;
    margin: 8px 0;
}

.velo-result-level {
    color: #75e6bd;
    font-size: 24px;
    font-weight: 800;
    margin: 4px 0;
}

.velo-result-note {
    color: #b5d0c7;
    font-size: 14px;
}

/* INSIGHTS */

.velo-insight {
    background: #142237;
    border: 1px solid #26384d;
    border-radius: 12px;
    padding: 13px 15px;
    margin-bottom: 9px;
    color: #dce8f3;
    font-size: 13px;
}

.velo-muted {
    color: #9aafc2;
    font-size: 13px;
}

/* FOOTER */

.velo-footer {
    text-align: center;
    padding: 27px 15px;
    background: #101c2e;
    border: 1px solid #26384d;
    border-radius: 16px;
    margin-top: 18px;
}

.velo-footer-brand {
    color: #65d6ad;
    font-size: 27px;
    font-weight: 800;
}

.velo-footer-tag {
    color: #8fa6bd;
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: 700;
}

.velo-footer-line {
    color: #dce8f3;
    font-size: 14px;
    margin-top: 18px;
}

.velo-footer-small {
    color: #71869a;
    font-size: 12px;
    margin-top: 17px;
}

[data-testid="stDataFrame"] {
    border: 1px solid #26384d;
    border-radius: 12px;
}

</style>
""")

# ============================================================
# 3. LOAD TUNED XGBOOST MODEL AND FEATURE NAMES
# ============================================================

@st.cache_resource
def load_artifacts():
    """Load the tuned XGBoost model and its saved input feature order."""
    loaded_model = joblib.load("bike_rental_xgboost_model.pkl")
    loaded_features = joblib.load("bike_rental_features.pkl")
    return loaded_model, loaded_features


try:
    model, feature_names = load_artifacts()

    if not isinstance(feature_names, list) or len(feature_names) == 0:
        raise ValueError("The saved feature list is empty or invalid.")

except Exception as exc:
    st.error(
        "Could not load the XGBoost model or feature list. "
        "Keep these files in the same folder as app.py: "
        "bike_rental_xgboost_model.pkl and bike_rental_features.pkl."
    )
    st.exception(exc)
    st.stop()


# ============================================================
# 4. SIDEBAR BRANDING
# ============================================================

st.sidebar.html("""
<div style="padding:10px 0 18px;">

    <div style="
        font-size:30px;
        font-weight:800;
        color:#65d6ad;
    ">
        🚲 VELO
    </div>

    <div style="
        font-size:10px;
        color:#8298ae;
        letter-spacing:2px;
    ">
        SMART MOBILITY INTELLIGENCE
    </div>

</div>
""")

st.sidebar.divider()


# ============================================================
# 5. DATE AND TIME
# ============================================================

st.sidebar.markdown("### 📅 Date & Time")

year = st.sidebar.selectbox(
    "🗓️ Year",
    [2011, 2012]
)

month = st.sidebar.selectbox(
    "📆 Month",
    list(range(1, 13)),
    format_func=lambda value:
        pd.Timestamp(2024, value, 1).strftime("%B")
)

weekday_names = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

weekday = st.sidebar.selectbox(
    "📍 Weekday",
    list(range(7)),
    format_func=lambda value: weekday_names[value]
)

hour = st.sidebar.slider(
    "🕒 Select Hour",
    0,
    23,
    12,
    format="%d:00"
)

st.sidebar.divider()


# ============================================================
# 6. WEATHER AND ENVIRONMENT
# ORIGINAL NORMALIZED VALUES
# ============================================================

st.sidebar.markdown("### 🌤️ Weather & Environment")

temp = st.sidebar.slider(
    "🌡️ Temperature (normalized)",
    0.0, 1.0, 0.5,
    step=0.01
)

atemp = st.sidebar.slider(
    "🤗 Feels-like Temperature (normalized)",
    0.0, 1.0, 0.5,
    step=0.01
)

hum = st.sidebar.slider(
    "💧 Humidity (normalized)",
    0.0, 1.0, 0.5,
    step=0.01
)

windspeed = st.sidebar.slider(
    "💨 Windspeed (normalized)",
    0.0, 1.0, 0.2,
    step=0.01
)

weather = st.sidebar.selectbox(
    "☁️ Weather Condition",
    ["Clear", "Mist", "Light Snow", "Heavy Rain"]
)

season = st.sidebar.selectbox(
    "🍃 Season",
    ["springer", "summer", "winter", "fall"],
    format_func=lambda value: value.title()
)

st.sidebar.divider()


# ============================================================
# 7. DAY INFORMATION
# ============================================================

st.sidebar.markdown("### 🏢 Day Information")

holiday = st.sidebar.selectbox(
    "🎉 Is it a Holiday?",
    ["No", "Yes"]
)

workingday = st.sidebar.selectbox(
    "💼 Working Day?",
    ["Working Day", "Not Working Day"]
)

st.sidebar.divider()

st.sidebar.html("""
<div style="
    background:#172a3c;
    padding:15px;
    border-radius:12px;
    border:1px solid #2b4555;
">

    <div style="
        color:#65d6ad;
        font-weight:800;
    ">
        ✨ VELO AI
    </div>

    <div style="
        font-size:12px;
        color:#a7bacb;
        margin-top:7px;
        line-height:1.6;
    ">
        Adjust your conditions and generate an intelligent
        bike demand forecast.
    </div>

</div>
""")


# ============================================================
# 8. AUTOMATIC FEATURE ENGINEERING
# ============================================================

is_weekend = int(weekday in [0, 6])

is_rush_hour = int(
    hour in [7, 8, 9, 17, 18, 19]
)

if 5 <= hour < 12:
    time_period = "Morning"

elif 12 <= hour < 17:
    time_period = "Afternoon"

elif 17 <= hour < 21:
    time_period = "Evening"

else:
    time_period = "Night"


# ============================================================
# 9. MODEL INPUT FEATURES
# ============================================================

input_data = {

    "yr": int(year == 2012),

    "mnth": month,

    "hr": hour,

    "weekday": weekday,

    "temp": temp,

    "atemp": atemp,

    "hum": hum,

    "windspeed": windspeed,

    "is_weekend": is_weekend,

    "is_rush_hour": is_rush_hour,

    "month_from_date": month,

    "season_springer": int(season == "springer"),

    "season_summer": int(season == "summer"),

    "season_winter": int(season == "winter"),

    "holiday_Yes": int(holiday == "Yes"),

    "workingday_Working Day": int(
        workingday == "Working Day"
    ),

    "weathersit_Heavy Rain": int(
        weather == "Heavy Rain"
    ),

    "weathersit_Light Snow": int(
        weather == "Light Snow"
    ),

    "weathersit_Mist": int(
        weather == "Mist"
    ),

    "time_period_Evening": int(
        time_period == "Evening"
    ),

    "time_period_Morning": int(
        time_period == "Morning"
    ),

    "time_period_Night": int(
        time_period == "Night"
    )

}


# ============================================================
# 10. PREDICTION FUNCTION
# ============================================================

def predict_demand(features):

    # Create one row using the values selected in the sidebar.
    input_frame = pd.DataFrame([features])

    # Check that every feature expected by the trained model is present.
    missing_features = [
        name for name in feature_names
        if name not in input_frame.columns
    ]

    if missing_features:
        raise ValueError(
            "Missing model features: " + ", ".join(missing_features)
        )

    # Match the exact feature order used when the model was trained.
    input_frame = input_frame[feature_names]

    prediction = model.predict(input_frame)[0]

    return max(0, round(float(prediction)))


# ============================================================
# 11. MAIN HEADER
# ============================================================

st.html("""
<div class="velo-brand">
    VELO / MOBILITY INTELLIGENCE
</div>

<div class="velo-hero">
    Predict the <span>Ride.</span>
</div>

<div class="velo-description">
    An intelligent bike-sharing demand forecasting platform.
    Explore conditions, predict demand, and make smarter mobility decisions.
</div>
""")


# ============================================================
# 12. RIDE CONDITIONS OVERVIEW
# ============================================================

st.html("""
<div class="velo-section">
    ✨ Your Ride Conditions
</div>
""")

month_name = pd.Timestamp(
    2024, month, 1
).strftime("%B")

overview_cards = [

    ("📅 DATE", f"{month:02d}/{year}", month_name),

    ("🕒 TIME", f"{hour:02d}:00", f"{time_period} session"),

    ("🌡️ TEMPERATURE", f"{temp:.2f}", "Normalized value"),

    ("💧 HUMIDITY", f"{hum:.2f}", "Normalized value")

]

columns = st.columns(4)

for column, (label, value, note) in zip(
    columns, overview_cards
):

    with column:

        st.html(f"""
        <div class="velo-card">

            <div class="velo-card-label">
                {label}
            </div>

            <div class="velo-card-value">
                {value}
            </div>

            <div class="velo-card-note">
                {note}
            </div>

        </div>
        """)

st.write("")

extra_cards = [

    ("🤗 Feels-like Temperature", f"{atemp:.2f}"),

    ("💨 Windspeed", f"{windspeed:.2f}"),

    ("☁️ Weather", weather)

]

extra_columns = st.columns(3)

for column, (label, value) in zip(
    extra_columns, extra_cards
):

    with column:

        st.html(f"""
        <div class="velo-insight">
            {label}: <strong>{value}</strong>
        </div>
        """)


# ============================================================
# 13. GENERATE PREDICTION
# ============================================================

left, right = st.columns([2, 1])

with left:

    st.html("""
    <div class="velo-section">
        🤖 Demand Forecast
    </div>
    """)

with right:

    generate = st.button(
        "✦ Generate Prediction",
        use_container_width=True
    )


if generate:

    try:

        with st.spinner(
            "VELO AI is analyzing your ride conditions..."
        ):

            prediction = predict_demand(input_data)

        st.session_state["prediction"] = prediction

        st.session_state["prediction_inputs"] = (
            input_data.copy()
        )

        st.session_state["human_inputs"] = {

            "year": year,

            "month": month_name,

            "hour": f"{hour:02d}:00",

            "weekday": weekday_names[weekday],

            "temperature_normalized": temp,

            "feels_like_temperature_normalized": atemp,

            "humidity_normalized": hum,

            "windspeed_normalized": windspeed,

            "weather": weather,

            "season": season.title(),

            "holiday": holiday,

            "workingday": workingday,

            "time_period": time_period,

            "is_rush_hour": is_rush_hour,

            "is_weekend": is_weekend

        }

        st.success(
            "Prediction generated successfully!"
        )

    except Exception as exc:

        st.error(f"Prediction failed: {exc}")


# ============================================================
# 14. DISPLAY PREDICTION RESULTS
# ============================================================

if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]

    if prediction < 100:

        demand_level = "Low Demand"

        demand_note = (
            "A quieter bike-sharing period is expected."
        )

    elif prediction < 300:

        demand_level = "Moderate Demand"

        demand_note = (
            "A steady level of rental activity is expected."
        )

    elif prediction < 600:

        demand_level = "High Demand"

        demand_note = (
            "A busy period for bike-sharing is expected."
        )

    else:

        demand_level = "Very High Demand"

        demand_note = (
            "Strong rental activity is expected."
        )

    st.divider()

    st.html("""
    <div class="velo-section">
        🎯 Prediction Results
    </div>
    """)

    st.html(f"""
    <div class="velo-result">

        <div class="velo-result-label">
            AI PREDICTED BIKE RENTALS
        </div>

        <div class="velo-result-number">
            {prediction:,}
        </div>

        <div class="velo-result-level">
            ✨ {demand_level}
        </div>

        <div class="velo-result-note">
            {demand_note}
        </div>

    </div>
    """)

    st.write("")

    chart_column, insights_column = st.columns(2)

    # ========================================================
    # 15. DEMAND GAUGE
    # ========================================================

    with chart_column:

        st.html("""
        <div class="velo-section">
            📊 Demand Indicator
        </div>
        """)

        gauge_max = max(
            1000,
            prediction * 1.2
        )

        gauge = go.Figure(
            go.Indicator(

                mode="gauge+number",

                value=prediction,

                number={
                    "font": {
                        "color": "#65d6ad",
                        "size": 35
                    },
                    "valueformat": ",.0f"
                },

                gauge={

                    "axis": {
                        "range": [0, gauge_max],
                        "tickcolor": "#8d9bad"
                    },

                    "bar": {
                        "color": "#65d6ad"
                    },

                    "bgcolor": "#142237",

                    "bordercolor": "#26384d",

                    "steps": [

                        {
                            "range": [
                                0,
                                gauge_max * 0.25
                            ],
                            "color": "#203047"
                        },

                        {
                            "range": [
                                gauge_max * 0.25,
                                gauge_max * 0.65
                            ],
                            "color": "#254b49"
                        },

                        {
                            "range": [
                                gauge_max * 0.65,
                                gauge_max
                            ],
                            "color": "#356a58"
                        }

                    ]

                }

            )
        )

        gauge.update_layout(

            height=280,

            margin=dict(
                l=25,
                r=25,
                t=30,
                b=15
            ),

            paper_bgcolor="#142237",

            font={
                "color": "#edf5f3"
            }

        )

        st.plotly_chart(
            gauge,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )


    # ========================================================
    # 16. RIDE INSIGHTS
    # ========================================================

    with insights_column:

        st.html("""
        <div class="velo-section">
            💡 Ride Insights
        </div>
        """)

        saved = st.session_state["human_inputs"]

        insights = [

            f"📅 {saved['weekday']} selected",

            f"🕒 {'Rush hour' if saved['is_rush_hour'] else 'Outside rush hour'}",

            f"🌤️ Weather: {saved['weather']}",

            f"🍃 Season: {saved['season']}",

            f"🌡️ Temperature: {saved['temperature_normalized']:.2f}",

            f"💧 Humidity: {saved['humidity_normalized']:.2f}",

            f"💨 Windspeed: {saved['windspeed_normalized']:.2f}"

        ]

        for insight in insights:

            st.html(f"""
            <div class="velo-insight">
                {insight}
            </div>
            """)


    # ========================================================
    # 17. PREDICTION DETAILS
    # ========================================================

    st.divider()

    st.html("""
    <div class="velo-section">
        📋 Prediction Details
    </div>
    """)

    report_data = {

        **st.session_state["human_inputs"],

        **st.session_state["prediction_inputs"],

        "predicted_rentals": prediction,

        "demand_level": demand_level

    }

    report_frame = pd.DataFrame([report_data])

    st.dataframe(
        report_frame,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # 18. DOWNLOAD REPORT
    # ========================================================

    st.divider()

    st.html("""
    <div class="velo-section">
        📥 Export Your Prediction
    </div>

    <div class="velo-muted">
        Download your prediction and selected ride conditions
        as a CSV report.
    </div>
    """)

    csv_bytes = report_frame.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(

        label="⬇️ Download Prediction Report (CSV)",

        data=csv_bytes,

        file_name="VELO_Bike_Demand_Report.csv",

        mime="text/csv",

        use_container_width=True

    )


# ============================================================
# 19. EMPTY STATE
# ============================================================

else:

    st.html("""
    <div class="velo-card"
         style="text-align:center;padding:38px 22px;">

        <div style="font-size:42px;">
            🚲
        </div>

        <div style="
            font-size:22px;
            font-weight:800;
            color:#65d6ad;
            margin-top:8px;
        ">
            Ready to Forecast?
        </div>

        <div class="velo-muted" style="margin-top:10px;">
            Adjust your conditions in the sidebar and generate
            a prediction to explore expected bike rental demand.
        </div>

    </div>
    """)


# ============================================================
# 20. FOOTER
# ============================================================

st.divider()

st.html("""
<div class="velo-footer">

    <div class="velo-footer-brand">
        🚲 VELO
    </div>

    <div class="velo-footer-tag">
        MOBILITY INTELLIGENCE
    </div>

    <div class="velo-footer-line">
        Predict the ride. Understand the demand. Move smarter.
    </div>

    <div class="velo-footer-small">
        Powered by Machine Learning &amp; Streamlit
    </div>

</div>
""")
