import time

from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY, CounterMetricFamily, GaugeMetricFamily
from sense_hat import SenseHat

prefix = "sense_hat_"

sense = SenseHat()
sense.clear()


class SenseHatCollector(object):
    def __init__(self):
        pass

    def collect(self):
        humidity = GaugeMetricFamily(
            f"{prefix}humidity", "readings of humidity", labels=["sensor"]
        )
        humidity.add_metric(["humidity"], sense.get_humidity())
        yield humidity

        pressure = GaugeMetricFamily(
            f"{prefix}pressure", "readings of pressure", labels=["sensor"]
        )
        pressure.add_metric(["pressure"], sense.get_pressure())
        yield pressure

        temperature = GaugeMetricFamily(
            f"{prefix}temperature", "readings of temperature", labels=["sensor"]
        )
        temperature.add_metric(["humidity"], sense.get_temperature_from_humidity())
        temperature.add_metric(["pressure"], sense.get_temperature_from_pressure())
        yield temperature


if __name__ == "__main__":
    start_http_server(9000)
    REGISTRY.register(SenseHatCollector())
    while True:
        time.sleep(1)
