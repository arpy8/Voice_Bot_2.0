# Voice Command Using Google's Speech Recognition API and Python Libraries

![Voice Command](assets/banner.png)

## Table of Contents

1. [Introduction](#Introduction)
2. [Installation](#installation)
3. [Prerequisites](#prerequisites)
4. [Usage](#usage)
5. [Supported Commands](#supported-commands)
6. [Customization](#customization)
7. [License](#license)

## 1. Introduction

This project is a Voice Command application that utilizes Google's Speech Recognition API and various Python libraries to process and execute spoken commands. It allows users to interact with their computer using voice commands, enabling hands-free operation for various tasks.

The application provides a simple interface for capturing audio input, processing it through Google's Speech Recognition API, and executing the corresponding command based on the recognized speech.

## 2. Installation

To get started with the Voice Command application, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/voice-command.git
   cd voice-command
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## 3. Prerequisites

Before running the Voice Command application, you need to set up the following:

1. **Google Cloud API Credentials**: Obtain a Google Cloud API key with enabled Speech-to-Text API access. Save the API key to a secure location and set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the credentials file.

2. **Microphone Access**: Ensure that your system has access to the microphone or an external audio input device.

## 4. Usage

To run the Voice Command application, execute the following command in the project directory:

```
python voice_command.py
```

The application will start listening for your voice commands via the microphone. Simply speak one of the supported commands listed below, and the application will process and execute it accordingly.

To exit the application, press `Ctrl + C`.

## 5. Supported Commands

The Voice Command application currently supports the following commands:

1. **"Open browser"**: Opens the default web browser.
2. **"Search Google for <query>"**: Initiates a Google search with the specified query.
3. **"Play music"**: Starts playing your favorite music from a predefined playlist.
4. **"Check email"**: Launches the email client and opens the inbox.
5. **"Take a screenshot"**: Captures a screenshot of the entire screen and saves it to the desktop.
6. **"Close application"**: Closes the currently focused application.
7. **"Shutdown"**: Shuts down the computer.

## 6. Customization

Feel free to customize and extend this project according to your requirements. You can add more voice commands, implement new functionalities, or integrate with other APIs and services.

To add new commands, edit the `voice_command.py` file and add a new case in the `process_command` function to handle the speech recognition for the new command.

## 7. License

The Voice Command application is licensed under the [MIT License](LICENSE), which allows you to use, modify, and distribute the code freely. Refer to the LICENSE file for more information.

---

Thank you for using the Voice Command application. If you have any questions, feedback, or encounter any issues, please don't hesitate to reach out to us at support@voicecommandapp.com. Happy voice commanding!
