import logging
import psutil
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SystemMetricsCollector:
    def __init__(self):
        logger.info("System metrics collector initialized successfully")

    def collect_system_metrics(self):
        """Collect system-level metrics"""
        try:
            # CPU Usage
            cpu_percent = psutil.cpu_percent()
            
            # Memory Usage
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            
            logger.debug(f"System metrics collected - CPU: {cpu_percent}%, Memory: {memory_percent}%")
            return {
                'cpu_usage': cpu_percent,
                'memory_usage': memory_percent,
                'timestamp': time.time()
            }
        except Exception as e:
            logger.error(f"Failed to collect system metrics: {e}")
            return None

    def get_detailed_system_info(self):
        """Get detailed system information"""
        try:
            return {
                'cpu_count': psutil.cpu_count(logical=False),
                'cpu_count_logical': psutil.cpu_count(logical=True),
                'memory_total': psutil.virtual_memory().total / (1024 * 1024 * 1024),  # GB
                'boot_time': psutil.boot_time()
            }
        except Exception as e:
            logger.error(f"Failed to get system info: {e}")
            return {}

# Create a global instance
system_metrics = SystemMetricsCollector()
