import pandas as pd

def load_sessions(path):
    df = pd.read_csv(path,parse_dates=["date"])
    return df

def add_derived(df):
    return df.assign(spq=120 / df["score"])

def main():
    df = load_sessions("data/sessions.csv")
    df = add_derived(df)


    print(df.head())
    print(df.shape)
    print(df.dtypes)
    df.info()
    print(df.describe())
    print(df["round"].value_counts())
    print(df["date"].nunique())
    print(df["date"].dt.day_name().head())

if __name__ == "__main__":
    main()