import random
from datetime import datetime

class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = random.uniform(18, 30)      # 도
        self.env_values["mars_base_external_temperature"] = random.uniform(0, 215)      # 도
        self.env_values["mars_base_internal_humidity"] = random.uniform(50, 60)         # %
        self.env_values["mars_base_external_illuminance"] = random.uniform(500, 715)    # W/m2
        self.env_values["mars_base_internal_co2"] = random.uniform(0.02, 0.1)           # %
        self.env_values["mars_base_internal_oxygen"] = random.uniform(4, 7)             # %

    def get_env(self):
        log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
        log += f"Internal Temp: {self.env_values['mars_base_internal_temperature']:.2f}도, "
        log += f"External Temp: {self.env_values['mars_base_external_temperature']:.2f}도, "
        log += f"Humidity: {self.env_values['mars_base_internal_humidity']:.2f}%, "
        log += f"Illuminance: {self.env_values['mars_base_external_illuminance']:.2f}W/m2, "
        log += f"CO2: {self.env_values['mars_base_internal_co2']:.4f}%, "
        log += f"O2: {self.env_values['mars_base_internal_oxygen']:.2f}%"

        # 로그
        print(log)

        return self.env_values


if __name__ == "__main__":
    ds = DummySensor()
    ds.set_env()
    env_data = ds.get_env()
