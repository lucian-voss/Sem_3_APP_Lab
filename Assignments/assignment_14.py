import logging

# Configure logging system
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("program.log", mode="w"),
        logging.StreamHandler()
    ],
    force=True
)

# Create logger
log = logging.getLogger()

# Display messages of different severity levels
log.debug("Debugging information displayed.")
log.info("Application started successfully.")
log.warning("Warning: Check the application.")
log.error("Error occurred during execution.")
log.critical("Critical: Application failure detected!")

print("\nAll log messages saved successfully.")
print("Check the program.log file for saved logs.")