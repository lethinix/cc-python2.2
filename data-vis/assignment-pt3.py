import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Load and merge data
df_ozone = pd.read_csv("ozone_2024/ozone_2024.csv")
df_site = pd.read_csv("site/site.csv")  
top_ozone = df_ozone.nlargest(30, "OZONE").reset_index(drop=True)
top_ozone = pd.merge(top_ozone, df_site[["SITE_ID", "ELEVATION"]], on="SITE_ID", how="left")

# Create hover text
top_ozone["HOVER_TEXT"] = (
    "<b>Site:</b> " + top_ozone["SITE_ID"] + "<br>" +
    "<b>Date:</b> " + pd.to_datetime(top_ozone["DATE_TIME"]).dt.strftime("%b %d, %Y %H:%M") + "<br>" +
    "<b>Ozone:</b> " + top_ozone["OZONE"].round(2).astype(str) + " ppm<br>" +
    "<b>Elevation:</b> " + top_ozone["ELEVATION"].astype(str) + " m"
)

# Create Plotly figure
fig = go.Figure()

# Calculate normalized sizes (5 to 20 pixel range)
ozone_min = top_ozone["OZONE"].min()
ozone_max = top_ozone["OZONE"].max()
top_ozone["NORM_SIZE"] = 5 + 15 * ((top_ozone["OZONE"] - ozone_min) / (ozone_max - ozone_min))

# Add scatter plot (with white borders for visibility)
fig.add_trace(
    go.Scatter(
        x=top_ozone.index,
        y=top_ozone["ELEVATION"],
        mode='markers',
        marker=dict(
            size=top_ozone["NORM_SIZE"],
            color=top_ozone["OZONE"],
            colorscale="Viridis",
            showscale=True,
            opacity=0.8,
            line=dict(width=1, color='white')  # White borders for contrast
        ),
        hovertext=top_ozone["HOVER_TEXT"],
        hoverinfo="text",
        name="Ozone Measurement"
    )
)

# Add subtle trend line (now more visible)
z = np.polyfit(top_ozone.index, top_ozone["ELEVATION"], 1)
fig.add_trace(
    go.Scatter(
        x=top_ozone.index,
        y=np.poly1d(z)(top_ozone.index),
        mode='lines',
        line=dict(color='cyan', dash='dash', width=2),  # Cyan for better visibility
        opacity=0.5,
        name='Trend Line'
    )
)

# Dark theme layout
fig.update_layout(
    title="<b>Top 30 Ozone Levels vs. Elevation</b>",
    title_font=dict(color='white', size=20),
    xaxis=dict(
        title="Observation Index",
        title_font=dict(color='white'),
        tickvals=top_ozone.index,
        ticktext=top_ozone["SITE_ID"],  # Full site IDs
        tickangle=45,
        tickfont=dict(color='white'),
        gridcolor='rgba(100,100,100,0.5)',
        zerolinecolor='rgba(100,100,100,0.5)'
    ),
    yaxis=dict(
        title="Elevation (m)",
        title_font=dict(color='white'),
        tickfont=dict(color='white'),
        gridcolor='rgba(100,100,100,0.5)',
        zerolinecolor='rgba(100,100,100,0.5)'
    ),
    legend=dict(
        x=0.02,
        y=0.98,
        xanchor='left',
        bgcolor='rgba(30,30,30,0.8)',  # Darker semi-transparent
        bordercolor='lightgray',
        font=dict(color='white', size=12)
    ),
    coloraxis=dict(
        colorbar=dict(
            title="Ozone (ppm)",
            title_font=dict(color='white'),
            tickfont=dict(color='white'),
            x=1.1,
            thickness=15
        )
    ),
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    width=1200,  # Slightly wider for full IDs
    height=700,
    margin=dict(l=80, r=150, t=100, b=100)
)

# Custom grid lines
fig.update_xaxes(showgrid=True, gridwidth=0.5)
fig.update_yaxes(showgrid=True, gridwidth=0.5)

fig.show()