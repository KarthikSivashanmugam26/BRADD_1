
import pyttsx3

engine = None

def initialize_speaker():
    """Initializes the text-to-speech engine with a male voice."""
    global engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Find a male voice. This might need adjustment depending on the system.
    male_voice = next((voice for voice in voices if "male" in voice.name.lower() or "david" in voice.name.lower() or "zira" not in voice.name.lower()), voices[0])
    engine.setProperty('voice', male_voice.id)
    engine.setProperty('rate', 180)  # Adjust speech rate for a clear, calm tone

def speak(text):
    """Speaks the given text using the initialized engine."""
    if not engine:
        initialize_speaker()
    
    print(f"BRADD: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    # Example usage
    speak("Hello Sir. BRADD is online. How may I assist you?")
    speak("The core systems are now operational.")