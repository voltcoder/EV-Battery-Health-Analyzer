def calculate_soh(df):
    max_voltage = df["voltage"].max()
    df["SOH (%)"] = (df["voltage"] / max_voltage) * 100
    return df
