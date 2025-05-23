import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

# === Asistente ===
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Nova")
LANGUAGE = os.getenv("LANGUAGE", "es")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False") == "True"

# === Voz ===
VOICE_INPUT_ENABLED = os.getenv("VOICE_INPUT_ENABLED", "True") == "True"
VOICE_OUTPUT_ENABLED = os.getenv("VOICE_OUTPUT_ENABLED", "True") == "True"
WAKE_WORDS = ["nova", "asistente", "hey nova"]

# === Interfaz gráfica ===
SHOW_GUI = os.getenv("SHOW_GUI", "True") == "True"
GUI_THEME = os.getenv("GUI_THEME", "dark")
ANIMATIONS_ENABLED = os.getenv("ANIMATIONS_ENABLED", "True") == "True"

# === Biometría y seguridad ===
USE_BIOMETRIC_AUTH = os.getenv("USE_BIOMETRIC_AUTH", "True") == "True"
USE_PASSWORD_FALLBACK = os.getenv("USE_PASSWORD_FALLBACK", "True") == "True"
AUDIT_LOG_ENABLED = os.getenv("AUDIT_LOG_ENABLED", "True") == "True"
SECURE_COMMANDS = os.getenv("SECURE_COMMANDS", "enviar correo,abrir whatsapp,modificar sistema").split(",")

# === Claves API ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# === Archivos y base de datos ===
DB_PATH = "data/context_memory.db"
COMMANDS_PATH = "data/learned_commands.json"
LOG_FILE = "logs/audit.log"

# === Aprendizaje ===
LEARNING_MODE_ENABLED = os.getenv("LEARNING_MODE_ENABLED", "True") == "True"
OBSERVATIONAL_LEARNING_ENABLED = os.getenv("OBSERVATIONAL_LEARNING_ENABLED", "False") == "True"
MAX_MEMORY_DURATION_MINUTES = int(os.getenv("MAX_MEMORY_DURATION_MINUTES", "60"))
