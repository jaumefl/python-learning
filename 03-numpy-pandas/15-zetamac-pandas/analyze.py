import numpy as np
from load import load_sessions, add_derived

def build_daily(df):
    daily = df.groupby("date").agg(
        avg=("score", "mean"),
        best=("score","max"),
        worst=("score","min"),
    ).reset_index()

    daily["roll7"] = daily["avg"].rolling(window=7).mean()
    daily["day_num"] = (daily["date"] - daily["date"].min()).dt.days

    return daily

def fit_trend(daily):
    slope, intercept = np.polyfit(daily["day_num"], daily["avg"], 1)
    return slope, intercept


def main():
    df = add_derived(load_sessions("data/sessions.csv"))
    daily = build_daily(df)
    slope, intercept = fit_trend(daily)

    print(f"First week average:  {daily['avg'].head(7).mean():.2f}")
    print(f"Last week average:   {daily['avg'].tail(7).mean():.2f}")
    print(f"Trend:               {slope:+.2f} points/day")

    best_round = df.loc[df["score"].idxmax()]
    print(f"Best single round:   {best_round['score']} on {best_round['date']:%Y-%m-%d}")

    best_day = daily.loc[daily["avg"].idxmax()]
    print(f"Best single day:     {best_day['avg']} on {best_day['date']:%Y-%m-%d}")



if __name__ == "__main__":
    main()