class Logger:
    def log(self, message, level="info"):  # Default level is "info"
        if level.lower() == "error":
            print(f"[ERROR] {message}")
        elif level.lower() == "warning":
            print(f"[WARNING] {message}")
        else:
            print(f"[INFO] {message}")

# Creating an object of Logger
logger = Logger()

# Logging different types of messages
logger.log("System running smoothly.")        # Default info log
logger.log("Low disk space!", "warning")      # Warning log
logger.log("File not found!", "error")        # Error log
