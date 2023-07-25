import time
import psutil
import logging
from src.base_logger import BaseLogger


class BaseMonitor:
    """
    BaseMonitor provides a base class for monitoring functionality.

    It allows monitoring various aspects of the application with a defined interval.
    """

    def __init__(self, logger=None, interval=60):
        """
        Initialize the BaseMonitor.

        :param logger: The logger instance to use for logging monitoring data.
        :param interval: The interval (in seconds) between consecutive monitoring actions. Default is 60 seconds.
        """
        self.logger = logger
        self.interval = interval

    def monitor(self):
        """
        Start the monitoring loop.

        This method continuously collects metrics at the defined interval and logs them using the logger.
        """
        while True:
            try:
                self.collect_metrics()
                time.sleep(self.interval)
            except Exception as e:
                if self.logger:
                    self.logger.error(f"Error during monitoring: {e}")
                else:
                    print(f"Error during monitoring: {e}")

    def collect_metrics(self):
        """
        Collect monitoring metrics.

        Implement specific monitoring logic in this method, depending on your application's requirements.
        """
        raise NotImplementedError("Please implement 'collect_metrics()' method in your subclass.")


class MonitoringLogger(BaseLogger, BaseMonitor):
    """
    MonitoringLogger extends BaseLogger and BaseMonitor to provide monitoring functionality.
    It allows monitoring various aspects of the application such as CPU and memory usage.
    """

    def __init__(self, name, log_dir="logs", base_log_path="", log_level=logging.DEBUG, log_format=None,
                 log_handlers=None, interval=60):
        BaseLogger.__init__(self, name, log_dir, base_log_path, log_level, log_format, log_handlers)
        BaseMonitor.__init__(self, logger=self, interval=interval)

    def collect_metrics(self):
        """
        Collect monitoring metrics.

        This method retrieves and logs real-time CPU and memory usage.
        """
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent

        self.info("msg=CPU Usage - %f%%", cpu_usage)
        self.info("msg=Memory Usage - %f%%", memory_usage)
