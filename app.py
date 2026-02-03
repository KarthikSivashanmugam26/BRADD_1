
import streamlit as st
from voice.speaker import speak, initialize_speaker
from voice.listener import listen
from core.brain import understand, act

def main():
    st.title("BRADD Engine")

    # Initialize the speaker once
    if 'speaker_initialized' not in st.session_state:
        initialize_speaker()
        st.session_state.speaker_initialized = True

    st.write("Welcome, sir. BRADD is online and ready to assist.")

    if st.button("Activate BRADD"):
        st.write("BRADD is now active. Listening for your command...")
        speak("How may I help you?")
        
        command = listen()

        if command:
            st.write(f"You said: {command}")
            action = understand(command)
            result = act(action)
            speak(result)
            st.write(f"BRADD says: {result}")
        else:
            st.write("Could not understand the command.")
            speak("I'm sorry, I could not understand the command.")

if __name__ == "__main__":
    main()