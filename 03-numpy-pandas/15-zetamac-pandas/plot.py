import matplotlib.pyplot as plt
from load import load_sessions, add_derived
from analyze import build_daily, fit_trend

RAW = "#9aa0a6"
SMOOTH = "#0072b2"
TREND = "#d55e00"


def make_plot(df, daily, slope, intercept, out_path):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.scatter(df["date"], df["score"],
               s=18, alpha=0.35, color=RAW, label="individual rounds")

    ax.plot(daily["date"], daily["avg"],
            linewidth=1, alpha=0.5, color=RAW, label="daily average")

    ax.plot(daily["date"], daily["roll7"],
            linewidth=2.5, color=SMOOTH, label="7-day rolling average")

    ax.plot(daily["date"], slope * daily["day_num"] + intercept,
            linewidth=1.5, linestyle="--", color=TREND,
            label=f"trend {slope:+.2f} pts/day")

    ax.set_title("Zetamac score, 2026-07-20 to 2026-08-18")
    ax.set_ylabel("correct answers per 120s")
    ax.grid(axis="y", alpha=0.25)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(frameon=False, loc="lower right")

    fig.autofmt_xdate()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    return fig


def main():
    df = add_derived(load_sessions("data/sessions.csv"))
    daily = build_daily(df)
    slope, intercept = fit_trend(daily)
    make_plot(df, daily, slope, intercept, "progress.png")
    print("wrote progress.png")


if __name__ == "__main__":
    main()