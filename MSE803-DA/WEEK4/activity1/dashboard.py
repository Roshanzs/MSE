"""Create a simple Matplotlib and Plotly dashboard for the happiness dataset."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from plotly.io import to_html
from plotly.subplots import make_subplots


ACTIVITY_DIR = Path(__file__).parent
DATA_FILE = ACTIVITY_DIR / "world_happiness_dataset.csv"
MATPLOTLIB_FILE = ACTIVITY_DIR / "matplotlib_top_three.png"
DASHBOARD_FILE = ACTIVITY_DIR / "happiness_dashboard.html"


def load_data() -> pd.DataFrame:
    """Load the cleaned CSV and validate the fields used by the dashboard."""
    data = pd.read_csv(DATA_FILE)
    required_columns = {
        "Country",
        "Happiness_Score",
        "Freedom_to_Make_Choices",
    }
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")
    return data


def create_matplotlib_chart(top_three: pd.DataFrame) -> None:
    """Save a clear static comparison of the three happiest countries."""
    chart_data = top_three.sort_values("Happiness_Score")
    figure, axis = plt.subplots(figsize=(8, 4.8))
    bars = axis.barh(
        chart_data["Country"],
        chart_data["Happiness_Score"],
        color=["#ef8354", "#4f9da6", "#173f5f"],
    )
    axis.set_title("Three Happiest Countries", loc="left", fontweight="bold")
    axis.set_xlabel("Happiness score")
    axis.set_xlim(0, max(chart_data["Happiness_Score"]) + 1)
    axis.grid(axis="x", alpha=0.25)
    axis.set_axisbelow(True)
    for bar in bars:
        axis.text(
            bar.get_width() + 0.05,
            bar.get_y() + bar.get_height() / 2,
            f"{bar.get_width():.2f}",
            va="center",
        )
    figure.tight_layout()
    figure.savefig(MATPLOTLIB_FILE, dpi=160, bbox_inches="tight")
    plt.close(figure)


def create_plotly_dashboard(
    top_three: pd.DataFrame, lowest_country: pd.Series
) -> None:
    """Build an interactive Plotly dashboard and write it as standalone HTML."""
    figure = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=("Happiness comparison", "Freedom summary"),
        horizontal_spacing=0.16,
    )
    figure.add_trace(
        go.Bar(
            x=top_three["Country"],
            y=top_three["Happiness_Score"],
            marker_color=["#173f5f", "#4f9da6", "#ef8354"],
            text=top_three["Happiness_Score"].map(lambda value: f"{value:.2f}"),
            textposition="outside",
            name="Happiness score",
            hovertemplate="%{x}<br>Happiness: %{y:.2f}<extra></extra>",
        ),
        row=1,
        col=1,
    )
    figure.add_trace(
        go.Bar(
            x=[lowest_country["Country"]],
            y=[lowest_country["Freedom_to_Make_Choices"]],
            marker_color="#ef8354",
            text=[f"{lowest_country['Freedom_to_Make_Choices']:.2f}"],
            textposition="outside",
            name="Freedom score",
            hovertemplate="%{x}<br>Freedom: %{y:.2f}<extra></extra>",
        ),
        row=1,
        col=2,
    )
    figure.update_yaxes(title_text="Score", range=[0, 8], row=1, col=1)
    figure.update_yaxes(title_text="Freedom score", range=[0, 1.1], row=1, col=2)
    figure.update_layout(
        title="World Happiness Dashboard",
        template="plotly_white",
        height=520,
        margin={"t": 90, "r": 35, "b": 55, "l": 60},
        showlegend=False,
    )

    top_names = ", ".join(top_three["Country"])
    chart_html = to_html(figure, full_html=False, include_plotlyjs=True)
    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>World Happiness Dashboard</title>
  <style>
    body {{ margin: 0; background: #f4f1ea; color: #173f5f; font-family: Georgia, serif; }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 42px 24px; }}
    h1 {{ margin-bottom: 8px; font-size: clamp(2rem, 5vw, 3.5rem); }}
    .intro {{ color: #49616a; font-family: Arial, sans-serif; }}
    .cards {{ display: flex; gap: 16px; flex-wrap: wrap; margin: 28px 0 12px; }}
    .card {{ background: white; border-left: 5px solid #ef8354; padding: 16px 20px; min-width: 190px; flex: 1; }}
    .label {{ color: #49616a; font: 700 0.76rem Arial, sans-serif; text-transform: uppercase; letter-spacing: 0.06em; }}
    .value {{ display: block; margin-top: 7px; font-size: 1.55rem; }}
    .plot {{ background: white; margin-top: 18px; }}
    .matplotlib {{ background: white; padding: 18px; margin-top: 18px; }}
    .matplotlib img {{ display: block; max-width: 100%; margin: auto; }}
    h2 {{ font-size: 1.15rem; margin: 0 0 12px; }}
  </style>
</head>
<body>
  <main>
    <h1>World Happiness Dashboard</h1>
    <p class="intro">Interactive ranking and freedom analysis built from the cleaned country dataset.</p>
    <section class="cards">
      <div class="card"><span class="label">Top three</span><span class="value">{top_names}</span></div>
      <div class="card"><span class="label">Lowest happiness</span><span class="value">{lowest_country['Country']}</span></div>
      <div class="card"><span class="label">Lowest country's freedom</span><span class="value">{lowest_country['Freedom_to_Make_Choices']:.2f}</span></div>
    </section>
    <div class="plot">{chart_html}</div>
    <section class="matplotlib"><h2>Matplotlib view: top-three comparison</h2><img src="matplotlib_top_three.png" alt="Bar chart comparing the three happiest countries"></section>
  </main>
</body>
</html>
"""
    DASHBOARD_FILE.write_text(page, encoding="utf-8")


def main() -> None:
    data = load_data()
    top_three = data.nlargest(3, "Happiness_Score").reset_index(drop=True)
    lowest_country = data.loc[data["Happiness_Score"].idxmin()]
    create_matplotlib_chart(top_three)
    create_plotly_dashboard(top_three, lowest_country)
    print("Top three happiest countries:")
    print(top_three[["Country", "Happiness_Score"]].to_string(index=False))
    print(
        f"Lowest happiness: {lowest_country['Country']} "
        f"(freedom score {lowest_country['Freedom_to_Make_Choices']:.2f})"
    )
    print(f"Created: {DASHBOARD_FILE.name} and {MATPLOTLIB_FILE.name}")


if __name__ == "__main__":
    main()