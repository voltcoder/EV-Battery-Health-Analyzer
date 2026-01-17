from data_loader import load_data
from analysis import calculate_soh
from visualization import plot_battery_health

data = load_data("../data/battery_data.csv")
data = calculate_soh(data)
plot_battery_health(data)

