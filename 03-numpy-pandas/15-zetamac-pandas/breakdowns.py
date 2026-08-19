from load import load_sessions, add_derived

def add_weekday(df):
    return df.assign(weekday=df["date"].dt.day_name())

def by_round(df):
    return df.groupby("round")["score"].agg(["mean", "std", "min", "max"])

def round_effect(df):
    df = df.assign(day_avg=df.groupby("date")["score"].transform("mean"))
    df = df.assign(dev=df["score"] - df["day_avg"])
    return df.groupby("round")["dev"].agg(["mean", "std"])

def by_weekday(df):
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return df.groupby("weekday")["score"].agg(["mean", "count"]).reindex(order)

def main():
    df = add_weekday(add_derived(load_sessions("data/sessions.csv")))

    print("=== Score by round ===")
    print(by_round(df).round(2))

    print("\n=== Round effect, deviation from that day's average ===")
    print(round_effect(df).round(2))

    print("\n=== Score by weekday ===")
    print(by_weekday(df).round(2))

    print("\n=== Daily scores by round ===")
    print(df.pivot(index="date", columns="round", values="score").head(10))


if __name__ == "__main__":
    main()