import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import time


num_data_points = 100
log_file = 'data.csv'


def get_ultrasonic_data():
    return random.uniform(0, 10)


def get_temperature_data():
    return random.uniform(15, 30)


timestamps = []
ultrasonic_readings = []
temperature_readings = []


for _ in range(num_data_points):
    timestamp = time.time()
    ultrasonic_data = get_ultrasonic_data()
    temperature_data = get_temperature_data()

    timestamps.append(timestamp)
    ultrasonic_readings.append(ultrasonic_data)
    temperature_readings.append(temperature_data)

    time.sleep(0.1)

data = {
    'Timestamp': timestamps,
    'Ultrasonic': ultrasonic_readings,
    'Temperature': temperature_readings
}
df = pd.DataFrame(data)
df.to_csv(log_file, index=False)


plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(timestamps, ultrasonic_readings, label='Ultrasonic Sensor', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.title('Ultrasonic Sensor Data')
plt.legend()


plt.subplot(2, 1, 2)
plt.plot(timestamps, temperature_readings, label='Temperature Sensor', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Sensor Data')
plt.legend()

plt.tight_layout()
plt.show()
