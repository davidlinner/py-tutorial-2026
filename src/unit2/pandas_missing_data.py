import pandas as pd
import numpy as np

weather = pd.DataFrame(
    {
        "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "temperature": [18.5, np.nan, 21.0, 19.5, np.nan],
        "rain_mm": [0.0, 2.5, 0.0, 1.0, 0.0],
    }
)

weather["temperature_filled"] = weather["temperature"].fillna(weather["temperature"].mean())
weather["is_warm"] = weather["temperature_filled"] >= 20

warm_days = weather[weather["is_warm"]]

print("Weather table:", weather)
print("Warm days:", warm_days)
print("Average filled temperature:", round(weather["temperature_filled"].mean(), 2))
