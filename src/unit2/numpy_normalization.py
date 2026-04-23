import numpy as np

sensor_a = np.array([12.0, 15.5, 14.0, 18.0, 21.5])
sensor_b = np.array([10.0, 11.0, 13.5, 17.0, 19.0])

combined = np.vstack([sensor_a, sensor_b])
mins = combined.min(axis=1, keepdims=True)
maxs = combined.max(axis=1, keepdims=True)

normalized = (combined - mins) / (maxs - mins)

difference = sensor_a - sensor_b

print("Combined data:", combined)
print("Normalized rows:", normalized)
print("Difference between sensors:", difference)
print("Average difference:", difference.mean())
