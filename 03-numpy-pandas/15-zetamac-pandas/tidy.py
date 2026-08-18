import pandas as pd

def load_raw(path):
    df = pd.read_csv("data/quant_prep_daily_log.csv", usecols=["Date", "Round 1", "Round 2", "Round 3"],
                     parse_dates=["Date"])
    return df

def tidy(df):
    long = df.melt(
        id_vars=["Date"],
        value_vars=["Round 1", "Round 2", "Round 3"],
        var_name="round",
        value_name="score",
    )

    long = long.dropna(subset=["score"])
    long["score"] = long["score"].astype(int)
    long["round"] = long["round"].str.replace("Round ", "").astype(int)

    long = long.rename(columns={"Date": "date"})
    long = long.sort_values(["date", "round"]).reset_index(drop=True)

    return long

def main():

    df = load_raw("data/quant_prep_daily_log.csv")
    long = tidy(df)

    long.to_csv("data/sessions.csv", index=False)


    print(len(long))
    print(long["date"].nunique())
    print(long["round"].value_counts())
    print(long["score"].describe())

if __name__ == "__main__":
    main()