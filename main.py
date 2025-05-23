from gui.interface import launch_gui
from voice.recognition import start_voice_listener
from memory.context_manager import load_context

if __name__ == "__main__":
    load_context()
    launch_gui()
    start_voice_listener()
