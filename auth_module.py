import os
import time
import json
import hashlib
from datetime import datetime, timedelta
from modules.utils.biometric import biometric_authenticate, fallback_password_check
from modules.memory.context_memory import load_temp_authorizations, save_temp_authorizations

# Tiempo válido de autorización temporal (ej: 10 minutos)
TEMP_AUTH_DURATION = timedelta(minutes=10)

# Rutas
AUTH_LOG_PATH = "logs/auth_log.json"
TEMP_AUTH_PATH = "data/temp_auth.json"


def check_user_authorization(command_name, user_id):
    """
    Verifica si el usuario tiene autorización temporal para un comando sensible.
    """
    auth_data = load_temp_authorizations(TEMP_AUTH_PATH)
    if user_id in auth_data and command_name in auth_data[user_id]:
        expires = datetime.fromisoformat(auth_data[user_id][command_name])
        if datetime.now() < expires:
            return True
    return False


def register_authorization(command_name, user_id):
    """
    Registra autorización temporal y loguea el acceso.
    """
    auth_data = load_temp_authorizations(TEMP_AUTH_PATH)
    if user_id not in auth_data:
        auth_data[user_id] = {}
    auth_data[user_id][command_name] = (datetime.now() + TEMP_AUTH_DURATION).isoformat()
    save_temp_authorizations(TEMP_AUTH_PATH, auth_data)
    log_authorization(command_name, user_id, granted=True)


def request_authorization(command_name, user_id):
    """
    Solicita autenticación biométrica o fallback para comandos sensibles.
    """
    print("Solicitando autenticación para:", command_name)
    success = biometric_authenticate()
    if not success:
        print("Biometría fallida. Solicite contraseña...")
        success = fallback_password_check(user_id)

    if success:
        register_authorization(command_name, user_id)
        return True
    else:
        log_authorization(command_name, user_id, granted=False)
        return False


def log_authorization(command_name, user_id, granted):
    """
    Guarda un log con fecha, comando, usuario y estado.
    """
    os.makedirs(os.path.dirname(AUTH_LOG_PATH), exist_ok=True)
    if not os.path.exists(AUTH_LOG_PATH):
        with open(AUTH_LOG_PATH, 'w') as f:
            json.dump([], f)
    with open(AUTH_LOG_PATH, 'r') as f:
        logs = json.load(f)

    logs.append({
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "command": command_name,
        "granted": granted
    })

    with open(AUTH_LOG_PATH, 'w') as f:
        json.dump(logs, f, indent=2)
