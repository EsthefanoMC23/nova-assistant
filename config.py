import os

# === Configuración del asistente ===
ASSISTANT_NAME = "Nova"
LANGUAGE = "es"  # Idioma principal (puedes cambiar a 'en' u otros)
DEBUG_MODE = True

# === Configuración de voz ===
VOICE_INPUT_ENABLED = True
VOICE_OUTPUT_ENABLED = True
WAKE_WORDS = ["nova", "asistente", "hey nova"]

# === Configuración de la interfaz gráfica ===
SHOW_GUI = True
GUI_THEME = "dark"
ANIMATIONS_ENABLED = True

# === Configuración de reconocimiento biométrico (si aplica) ===
USE_BIOMETRIC_AUTH = True
USE_PASSWORD_FALLBACK = True

# === Seguridad y auditoría ===
AUDIT_LOG_ENABLED = True
SECURE_COMMANDS = ["enviar correo", "abrir whatsapp", "modificar sistema"]

# === Configuración de conexión a APIs externas ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "aqui_tu_clave_openai")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "aqui_tu_client_id")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "aqui_tu_secret")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "aqui_tu_clave_google")

# === Configuración de bases de datos ===
DB_PATH = "data/context_memory.db"
COMMANDS_PATH = "data/learned_commands.json"
LOG_FILE = "logs/audit.log"

# === Otras configuraciones ===
LEARNING_MODE_ENABLED = True
OBSERVATIONAL_LEARNING_ENABLED = False  # En pausa hasta tener memoria externa
MAX_MEMORY_DURATION_MINUTES = 60  # Duración de la memoria contextual
