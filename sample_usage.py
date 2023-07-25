import logging
from src.telemetry_logger import TelemetryLogger
from src.monitoring_logger import MonitoringLogger

# Sample usage
if __name__ == "__main__":
    telemetry_logger = TelemetryLogger("my_app", log_dir="logs", log_level=logging.DEBUG)

    total_count = 100
    progress = 0.75
    status = "complete"
    data_dict = {"name": "John Doe", "age": 30}
    data_list = [1, 2, 3, 4]

    telemetry_logger.info("msg=Total num of problem solved=%d", total_count)
    telemetry_logger.info("msg=Progress is %f", progress)
    telemetry_logger.info("msg=Status is %s", status)
    telemetry_logger.info("msg=Data dictionary: %s", data_dict)
    telemetry_logger.info("msg=Data list: %s", data_list)

    # Log telemetry events
    telemetry_logger.log_event("user_login", username="john_doe", role="admin")
    telemetry_logger.log_event("purchase", product="laptop", price=1200.0, quantity=2)

    # Perform telemetry analytics
    telemetry_logger.perform_telemetry_analytics()

    # Aggregate telemetry data
    telemetry_logger.aggregate_telemetry_data()

    monitoring_logger = MonitoringLogger("my_app", log_dir="logs", log_level=logging.DEBUG, interval=5)
    # Start monitoring
    monitoring_logger.monitor()