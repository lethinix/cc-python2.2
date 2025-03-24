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

# Add scatter plot (PROPERLY SCALED)
fig.add_trace(
    go.Scatter(
        x=top_ozone.index,
        y=top_ozone["ELEVATION"],
        mode='markers',  # Fixed typo: was 'markers'
        marker=dict(
            size=top_ozone["NORM_SIZE"],
            color=top_ozone["OZONE"],
            colorscale="Viridis",
            showscale=True,
            opacity=0.8,
            line=dict(width=1, color='DarkSlateGrey')
        ),
        hovertext=top_ozone["HOVER_TEXT"],
        hoverinfo="text",
        name="Ozone Measurement"
    )
)

# Add subtle trend line
z = np.polyfit(top_ozone.index, top_ozone["ELEVATION"], 1)
fig.add_trace(
    go.Scatter(
        x=top_ozone.index,
        y=np.poly1d(z)(top_ozone.index),
        mode='lines',
        line=dict(color='red', dash='dash', width=1.5),
        opacity=0.3,
        name='Trend Line'
    )
)

# Clean layout
fig.update_layout(
    title="<b>Top 30 Ozone Levels vs. Elevation</b>",
    xaxis=dict(
        title="Observation Index",
        tickvals=top_ozone.index,
        ticktext=top_ozone["SITE_ID"].str[:4] + "...",
        tickangle=45
    ),
    yaxis=dict(title="Elevation (m)"),
    hovermode="closest",
    width=1000,
    height=600,
    legend=dict(
        x=0.02,
        y=0.98,
        xanchor='left',
        bgcolor='rgba(255,255,255,0.7)',
        font=dict(size=10)
    ),
    coloraxis=dict(
        colorbar=dict(
            x=1.1,
            title="Ozone (ppm)",
            thickness=15
        )
    ),
    margin=dict(l=50, r=200, t=80, b=100),
    plot_bgcolor='white'
)

fig.update_xaxes(showgrid=True, gridcolor='lightgray')
fig.update_yaxes(showgrid=True, gridcolor='lightgray')

fig.show()