# World Happiness Dashboard

## Approach

`dashboard.py` loads `world_happiness_dataset.csv` with pandas and computes the three highest happiness scores with `nlargest()`. It identifies the lowest score with `idxmin()`, then reads that row's `Freedom_to_Make_Choices` value.

The script creates two complementary outputs:

- `matplotlib_top_three.png`: a labelled horizontal bar chart comparing the three happiest countries.
- `happiness_dashboard.html`: a browser-openable dashboard containing interactive Plotly charts, summary cards, and the Matplotlib chart.

Run it from this folder with:

```bash
python dashboard.py
```

Open `happiness_dashboard.html` in a browser after the script finishes.

## Findings

The three happiest countries in this dataset are Canada (`7.34`), Brazil (`6.98`), and Finland (`6.67`). South Africa has the lowest happiness score (`3.53`) and a Freedom score of `0.90`.

## Most appropriate chart

A sorted horizontal bar chart is the most appropriate primary chart because the task compares a small number of categorical items using one quantitative measure. Sorting makes the ranking immediately visible, while data labels preserve the exact scores. The second bar chart is appropriate for the single-country Freedom summary because it makes the value easy to read against the `0` to `1` score scale. Plotly adds hover details and interactivity; Matplotlib provides a clear static figure for reports.