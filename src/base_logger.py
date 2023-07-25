import logging
import json
import os
from datetime import datetime


class KeyValueFormatter(logging.Formatter):
    """
    Custom log formatter to parse and format log messages with key-value pairs.

    Log messages with the format "key=value" will be parsed and stored as attributes in the log record.
    """

    def format(self, record):
        extra = record.__dict__.get('extra', {})
        custom_msg = extra.get('custom_msg', None)

        if custom_msg is None:
            return super().format(record)

        pattern = r"(\w+)=(\S+)"
        matches = re.findall(pattern, custom_msg)
        key_values = {key: self._convert_value(value) for key, value in matches}

        record.message = record.getMessage()
        for key, value in key_values.items():
            setattr(record, key, value)

        return super().format(record)

    def _convert_value(self, value):
        try:
            return json.loads(value)
        except (json.JSONDecodeError, ValueError):
            return value


class BaseLogger(logging.Logger):
    """
    BaseLogger provides a base class for logging with key-value formatting.

    It creates log directories, files, and handlers based on the log directory and base log path.
    """

    def __init__(self, name, log_dir="logs", base_log_path="", log_level=logging.DEBUG, log_format=None,
                 log_handlers=None):
        """
        Initialize the BaseLogger.

        :param name: The name of the logger.
        :param log_dir: The directory to store log files. Default is "logs".
        :param base_log_path: The base path for log files.
        :param log_level: The logging level. Default is DEBUG.
        :param log_format: The log message format. Default is None (uses KeyValueFormatter).
        :param log_handlers: List of log handlers to use. Default is None (file and console handlers).
        """
        super(BaseLogger, self).__init__(name, log_level)

        current_date = datetime.now()
        year_dir = os.path.join(log_dir, str(current_date.year))
        month_dir = os.path.join(year_dir, str(current_date.month))

        if base_log_path:
            base_log_path = os.path.join(base_log_path, month_dir)
        else:
            base_log_path = month_dir

        # Create base log directories if they don't exist
        if not os.path.exists(base_log_path):
            os.makedirs(base_log_path)

        log_file = os.path.join(base_log_path, f"{current_date.day}.log")

        if log_format is None:
            log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        formatter = KeyValueFormatter(log_format)

        if log_handlers is None:
            log_handlers = [logging.FileHandler(log_file), logging.StreamHandler()]
        for handler in log_handlers:
            handler.setFormatter(formatter)
            self.addHandler(handler)



