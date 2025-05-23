import os
import asyncio
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
    MULTIUSER_ENABLED
)

from modules.voice import VoiceAssistant
from modules.gui import GUIController
from modules.auth import Authenticator
from modules.logger import AuditLogger
from modules.commands import CommandProcessor
from modules.context import MemoryContext
from modules.learning import LearningEngine
from modules.integrations import AppIntegrator

# === Inicialización de componentes ===
authenticator = Authenticator(USE_BIOMETRIC_AUTH, USE_PASSWORD_FALLBACK)
audit_logger = AuditLogger(enabled=AUDIT_LOG_ENABLED)
voice_assistant = VoiceAssistant(language=LANGUAGE)
memory_context = MemoryContext(multiuser=MULTIUSER_ENABLED)
command_processor = CommandProcessor(memory=memory_context)
learning_engine = LearningEngine(context=memory_context)
app_integrator = AppIntegrator()
gui_controller = GUIController(show=SHOW_GUI, assistant_name=ASSISTANT_NAME)

# === Arranque principal ===
async def main():
    print(f"\n👋 Bienvenido a {ASSISTANT_NAME}")
    print(f"🌐 Idioma configurado: {LANGUAGE}")

    if not OPENAI_API_KEY:
        print("🚫 ERROR: Clave API de OpenAI no encontrada en .env")
        return

    if USE_BIOMETRIC_AUTH:
        auth_result = authenticator.authenticate_user()
        if not auth_result:
            print("❌ Autenticación fallida. Cerrando aplicación.")
            return

    if SHOW_GUI:
        gui_controller.show_status("Inicializando...")

    if VOICE_INPUT_ENABLED:
        await voice_assistant.listen_loop(
            on_command=command_processor.handle_command,
            on_unknown=learning_engine.learn_new_command,
            gui_feedback=gui_controller.update_state
        )
    else:
        while True:
            user_input = input("Escribe un comando: ")
            await command_processor.handle_command(user_input)

# === Punto de entrada ===
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Asistente finalizado por el usuario.")
