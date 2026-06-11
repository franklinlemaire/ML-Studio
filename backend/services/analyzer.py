import pandas as pd
import numpy as np

def analyze_dataset(df : pd.DataFrame) -> dict :
    """ Analyse complète du DataFrame - retourne tout ce dont le Frontend a besoin """

# -- Infos générales --
n_rows, n_cols = df.shape
missing = df.isnull().sum()
missing_pct = (missing / n_rows*100).round(2)

# -- Typage des colonnes --

col_types = {}
for col in df.columns:
    dtype = str(df[col].dtype)
    if dtype in ["int64", "float64"]:
        col_types[col] = "numérique"
    elif dtype=="bool":
        col_types[col] = "booléen"
    else:
        n_unique = df[col].nunique()
        col_types[col] = "catégoriel" if n_unique <= 20 else "texte"

# -- Stastiques par colonne --

columns_info = []

for col in df.columns:
    info ={
        "name" : col,
        "type" : col_types[col],
        "missing" : int(missing[col]),
        "missing_pct" : float(missing_pct[col]),
        "unique" : int(df[col].nunique())
    }
    if col_types[col] == "numérique":
            info.update({
                "mean": round(float(df[col].mean()), 4),
                "std":  round(float(df[col].std()),  4),
                "min":  round(float(df[col].min()),  4),
                "max":  round(float(df[col].max()),  4),
                "histogram": _histogram(df[col]),
            })
    else:
            info["top_values"] = df[col].value_counts().head(5).to_dict()

    columns_info.append(info)

    # --- Aperçu des premières lignes (NaN → None pour JSON) ---
    preview = df.head(10).where(pd.notnull(df.head(10)), None).to_dict(orient="records")

    return {
        "n_rows":      n_rows,
        "n_cols":      n_cols,
        "columns":     columns_info,
        "preview":     preview,
        "missing_total": int(missing.sum()),
    }


def _histogram(series: pd.Series, bins: int = 20) -> list:
    """Retourne les données d'un histogramme pour recharts."""
    series = series.dropna()
    counts, edges = np.histogram(series, bins=bins)
    return [
        {"x": round(float(edges[i]), 3), "count": int(counts[i])}
        for i in range(len(counts))
    ]