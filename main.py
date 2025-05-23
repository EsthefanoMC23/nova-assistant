import os
from config import (
    ASSISTANT_NAME,
    LANGUAGE,
    DEBUG_MODE,
    VOICE_INPUT_ENABLED,
    SHOW_GUI,
    OPENAI_API_KEY,
    USE_BIOMETRIC_AUTH,
    USE_PASSWORD_FALLBACK,
    AUDIT_LOG_ENABLED,
    SECURE_COMMANDS,
)

# === Carga inicial del asistente ===
def iniciar_asistente():
    print(f"👋 Bienvenido, soy {ASSISTANT_NAME}")
    print(f"🌐 Idioma: {LANGUAGE}")
    if DEBUG_MODE:
        print("🛠️ Modo Debug ACTIVADO")

    # Seguridad
    if USE_BIOMETRIC_AUTH:
        print("🔐 Autenticación biométrica habilitada")
        if USE_PASSWORD_FALLBACK:
            print("🛡️ Modo de respaldo por contraseña habilitado")
    
    if AUDIT_LOG_ENABLED:
        print("📋 Registro de auditoría activo")

    # Voz
    if VOICE_INPUT_ENABLED:
        print("🎙️ Reconocimiento de voz habilitado")

    # Interfaz
    if SHOW_GUI:
        print("🖼️ Modo gráfico activo")

    # Revisión de API key
    if not OPENAI_API_KEY:
        print("🚫 ERROR: No se encontró la clave de API de OpenAI en el .env")
        return

    print(f"✅ {ASSISTANT_NAME} está listo para ayudarte.")

if __name__ == "__main__":
    iniciar_asistente()
