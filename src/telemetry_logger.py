import json
from datetime import datetime
from src.base_logger import BaseLogger


class TelemetryLogger(BaseLogger):
    """
    TelemetryLogger extends BaseLogger to provide logging and analytics for telemetry events.
    It allows logging telemetry events with associated data and performing telemetry analytics.
    """

    def log_event(self, event_name, **kwargs):
        """
        Log a telemetry event with associated data.

        :param event_name: The name of the telemetry event.
        :param kwargs: Additional key-value pairs representing the telemetry event data.
        """
        event_data = {
            "event_name": event_name,
            "timestamp": str(datetime.now()),
            "data": kwargs
        }

        self.info("msg=Telemetry event - %s", json.dumps(event_data))

    def perform_telemetry_analytics(self):
        """
        Perform telemetry analytics.

        Implement specific analytics logic within this method, depending on your application's requirements.
        """
        self.info("msg=Performing telemetry analytics")

    def aggregate_telemetry_data(self):
        """
        Aggregate telemetry data.

        Implement data aggregation logic in this method as needed.
        """
        self.info("msg=Aggregating telemetry data")
