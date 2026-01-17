import matplotlib.pyplot as plt

def plot_battery_health(df):
    plt.plot(df["cycle"], df["SOH (%)"])
    plt.xlabel("Charge Cycles")
    plt.ylabel("State of Health (%)")
    plt.title("EV Battery Health Degradation")
    plt.grid()
    plt.show()

