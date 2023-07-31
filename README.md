# Voice Assistant

This is a simple voice assistant script written in Python that can perform various tasks based on voice commands. The script uses the SpeechRecognition library to convert speech to text and then responds accordingly. The assistant can perform tasks like sending WhatsApp messages, opening the camera, telling jokes, setting reminders, playing songs on Spotify, and more.

## Prerequisites

Before running the voice assistant, make sure you have the following libraries installed:

- `pyautogui`: Used for simulating keyboard input to write or type text.
- `speech_recognition`: Used for speech recognition and converting speech to text.
- `pyttsx3`: Used for text-to-speech conversion to provide audio responses.
- `pygame`: Used for playing sound effects.
- `spotipy`: Used for controlling the Spotify app to play songs.

## Setup

1. Clone the repository or download the script.

2. Install the required libraries using the following command:
   ```
   pip install pyautogui speech_recognition pyttsx3 pygame spotipy
   ```

3. Make sure you have the necessary dependencies for Spotify API interaction. Refer to the Spotify documentation for more details.

4. Run the script using the following command:
   ```
   python voice_assistant.py
   ```

## Usage

Once the script is running, the voice assistant will listen for a wake word ("hey," "hi," "hello," or "over"). When the wake word is detected, the assistant will respond with a greeting and start listening for your commands.

Some of the commands the assistant can understand are:

- **"pause"**: Pauses the current session. To resume, say the wake word again.

- **"write" or "type"**: Allows you to type text using voice commands.

- **"whatsapp"** or **"contact"**: Sends a WhatsApp message to a specified contact.

- **"camera"** or **"open"** or **"click"** or **"picture"**: Opens the camera and clicks a picture.

- **"gallery"**: Opens the gallery.

- **"joke"** or **"dad"**: Tells a random dad joke.

- **"change"** or **"name"**: Updates the name (of the assistant?).

- **"set"** or **"reminder"**: Sets a reminder based on the provided text.

- **"time"** or **"right"**: Tells the current time.

- **"play"** or **"spotify"** or **"song"**: Plays a song on Spotify.

- **"shutdown"** or **"system"**: Shuts down the system.

## Note

Please note that the functionality related to WhatsApp and Spotify may require additional configurations and authentication, depending on your setup.

Feel free to customize the script or add more features as per your requirements!

Happy voice commanding!