import speech_recognition as sr
import openai

def reconocer_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="es-ES")
        print(f"Entendí: {texto}")
        return texto
    except Exception as e:
        print("No te entendí")
        return ""

def main():
    while True:
        comando = reconocer_voz()
        if comando:
            print(f"Procesando comando: {comando}")

if __name__ == "__main__":
    main()
