import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Read environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")  # Default to Gemini 2.5 Flash

# Validate configuration
if not GOOGLE_API_KEY:
    logger.error("GOOGLE_API_KEY is not set in the environment variables.")
    raise ValueError("GOOGLE_API_KEY must be set in the environment variables.")

logger.info(f"Configuration loaded successfully. Using model: {GEMINI_MODEL}")

# Configuration is available as module-level variables:
# GOOGLE_API_KEY - Google API key for Gemini
# GEMINI_MODEL - Gemini model name (defaults to gemini-2.5-flash)