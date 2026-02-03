
import speech_recognition as sr

def listen():
    """
    Listens for a command from the user and returns the transcribed text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-us')
        print(f"User said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    command = listen()
    if command:
        print(f"Command received: {command}")