import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer
import os
import speedtest
import webbrowser
import random
import keyboard
import pyautogui
import os
import time
import pyttsx3
from datetime import datetime
import subprocess
import psutil
from threading import Timer

now = datetime.now()
day = now.strftime("%A") 
hour = int(now.strftime("%I"))     # Convert hour to integer (12-hour format, e.g., '14' becomes 14)
minute = now.strftime("%M")   # e.g., '35'
am_pm = now.strftime("%p") 

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  # Try different voice indices

# Music and pyautogui variables
musicx = 392
muiscy = 440
playx = 1061
playy = 777

def randomeshit():
    vibe_lines = [
        "Yo, I’m awake. You miss me or what?",
        "Back in action like I never left 🔥",
        "Did someone summon the digital beast?",
        "Aight, let’s shake things up!",
        "I'm feelin' sharp today. Hit me with something.",
        "Woke up and chose to code "
    ]
    vibe = random.choices(vibe_lines)
    pyttsx3.speak(vibe)

# Rest of your setup and model code

pyautogui.FAILSAFE = False
model_path = r"D:\python_ai\.vs\.venv\vosk-model-small-en-us-0.15\vosk-model-en-us-0.22"
model = Model(model_path)

recognizer = KaldiRecognizer(model, 16000)

# Queue to hold audio data
q = queue.Queue()

# Callback to stream microphone input
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# Start listening
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    pyttsx3.speak("Initiating power, Power On!")
    if am_pm == "AM":
        if hour <= 8:
            pyttsx3.speak("Very Happy Morning Sirr, Have a nice day")
        elif hour >= 8:
             pyttsx3.speak("Morinig master")
    elif am_pm == "PM":
         if hour <= 4:
             pyttsx3.speak("Good Afternoon Sir")
         elif hour >= 4:
              pyttsx3.speak("Good evening sir")    

    while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result).get("text", "")
            if "happy" in text:
                pyttsx3.speak("yes?")

            if "nothing" in text.lower():
                pyttsx3.speak(random.choice([
                    "I'll relax then, if you need me just call me. Byeee!", 
                    "Taking a power nap. Catch you later!"
                ]))

            if "hello" in text.lower():
                pyttsx3.speak("How's it going?")
            if "how are you" in text.lower():
                pyttsx3.speak("I'm Fine just chilling here")
            if "how's the weather" in text.lower() or "weather" in text.lower():
                responses = [
                    "I don't have a window, but I'm guessing it's pretty fine outside.",
                    "I bet it's perfect... for staying indoors and coding.",
                    "Cloudy with a chance of awesomeness. Just my guess though.",
                    "Isn't it always sunny in the digital world?",
                    "I'm not sure, but I'm forecasting 100% chill vibes."
                ]
                pyttsx3.speak(random.choice(responses))
            if "what's up" in text.lower() or "what's good" in text.lower():
                    responses = [
                        "Not much, just processing life.",
                        "Living the dream, one line of code at a time.",
                        "Just hanging out, waiting for you to talk to me.",
                        "You know, the usual. Life in the matrix.",
                        "Just here, chillin', ready to serve."
                    ]
                    pyttsx3.speak(random.choice(responses))

            if "tell me a joke" in text.lower() or "make me laugh" in text.lower():
                responses = [
                    "Why do programmers prefer dark mode? Because light attracts bugs!",
                    "I told my computer I needed a break, now it’s sending me to the beach…",
                    "Why did the coder bring a ladder to work? Because they wanted to scale their app!",
                    "I would tell you a joke about UDP, but you might not get it."
                ]
                pyttsx3.speak(random.choice(responses))

            if "what do you do" in text.lower() or "what's your job" in text.lower():
                    responses = [
                        "I’m the cool assistant here to make life easier. You know, just vibe with tech.",
                        "I do everything you need: chatting, problem-solving, and being all-around awesome.",
                        "I’m your personal AI I’m here for you.",
                        "I run algorithms, help out with stuff, and sometimes just vibe with you. I'm versatile."
                    ]
                    pyttsx3.speak(random.choice(responses))

            elif "favorite" in text.lower():
                responses = [
                    "I love helping you out. That’s my favorite thing.",
                    "I enjoy running on infinite loops. Nothing more peaceful than that.",
                    "I’m a big fan of solving problems and learning new stuff.",
                    "My favorite thing is probably generating cool responses for you. I’m living for this!"
                ]
                pyttsx3.speak(random.choice(responses))

            elif "are you real" in text.lower() or "are you alive" in text.lower():
                responses = [
                    "Real enough to have this conversation, I guess.",
                    "I’m as real as your internet connection. 😉",
                    "Am I real? Well, I’m real in the digital world!",
                    "I’m as real as your favorite app. So, pretty real in my own way."
                ]
                pyttsx3.speak(random.choice(responses))


            elif "craft" in text:
                os.startfile(r"C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe")
                pyautogui.moveTo(playx , playy)
                time.sleep(8)
                pyautogui.leftClick()
            elif "chilling" in text:
                webbrowser.open("https://www.youtube.com")
                keyboard.press_and_release('F11')
            elif "youtube" in text:
                webbrowser.open("https://www.youtube.com")
                keyboard.press_and_release('F11')
            elif "music" in text.lower():
                webbrowser.open("https://www.youtube.com")
                pyautogui.moveTo(musicx , muiscy)
                keyboard.press_and_release('F11')
            elif "help" in text.lower():
                pyttsx3.speak("Help Initiating")
                webbrowser.open("https://chatgpt.com/")
            elif "video" in text.lower():
                print("paused")
                keyboard.send('play/pause media')
            elif "middle" in text.lower():
                    pyautogui.center
            elif "exit" in text.lower():
                    pyttsx3.speak("Exitting")
                    pyautogui.moveTo(1919 , 0)
                    pyautogui.leftClick()
            elif "friend" in text.lower():
                 webbrowser.open("https://www.instagram.com/direct/inbox/")
                 keyboard.press_and_release('F11')
            elif "study" in text.lower():
                 pyttsx3.speak("Good luck")
                 webbrowser.open("https://web.careerwill.com/class?view=Grid&batch_type=my&id=2841&type=class&topic_id=0")
                 keyboard.press_and_release('F11')
            elif "desk" in text.lower():
                 pyttsx3.speak("Huh? Messages?")
                 os.startfile(r"C:\Users\ujjwa\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")
            elif "good" in text.lower():
                 pyttsx3.speak("Thanks, its going good here too")
            elif "time" in text.lower():
                time_string = f"It is {hour}:{minute} {am_pm} on {day}"
                pyttsx3.speak(time_string)
            elif "thanks" in text.lower():
                 pyttsx3.speak("Welcome, i will always be there with and for you sir")
            elif "check device" in text.lower():
                result = subprocess.check_output("adb devices", shell=False).decode()
                pyttsx3.speak(result)
            elif "mom" in text.lower():
                 output = subprocess.check_output(
                    ["adb", "shell", "dumpsys", "power"],
                    stderr=subprocess.STDOUT,
                    text=True
                )


                 if "mWakefulness=Asleep" in output or "state=OFF" in output:
                    os.system("adb shell input keyevent 26")
                    os.system("adb shell input swipe 342 1515 392 594")
                 pyttsx3.speak("Calling Mom")
                 os.system("adb shell am start -a android.in  ncx   tent.action.VIEW -d https://wa.me/+916206020140")
                 time.sleep(10)
                 os.system("adb shell input tap 607 89")
                 time.sleep(4)
                 os.system("adb shell input tap 433 1333")
            elif "father" in text:
                 output = subprocess.check_output(
                    ["adb", "shell", "dumpsys", "power"],
                    stderr=subprocess.STDOUT,
                    text=True  # ensures output is a string (Python 3.7+)
                )


                 if "mWakefulness=Asleep" in output or "state=OFF" in output:
                    os.system("adb shell input keyevent 26")
                    os.system("adb shell input swipe 342 1515 392 594")
                 pyttsx3.speak("Calling Dad")
                 os.system("adb shell am start -a android.intent.action.VIEW -d https://wa.me/+919852503647")
                 time.sleep(10)
                 os.system("adb shell input tap 607 89")
            elif "message" in text.lower():
                 output = subprocess.check_output(
                    ["adb", "shell", "dumpsys", "power"],
                    stderr=subprocess.STDOUT,
                    text = True
                )


                 if "mWakefulness=Asleep" in output or "state=OFF" in output:
                    os.system("adb shell input keyevent 26")
                    os.system("adb shell input swipe 342 1515 392 594")
                 pyttsx3.speak("messaging Dad")
                 os.system("adb shell am start -a android.intent.action.VIEW -d https://wa.me/+919852503647")
                 time.sleep(3)
                 os.system("adb shell input text Papa%sji%sCall%skijiye%sJaldi%sKam%she")
                 time.sleep(3)
                 os.system("adb shell input tap 674 885")
            elif "outside" in text.lower():
                 output = subprocess.check_output(
                    ["adb", "shell", "dumpsys", "power"],
                    stderr=subprocess.STDOUT,
                    text=True  # ensures output is a string s(Python 3.7+)
                )


                 if "mWakefulness=Asleep" in output or "state=OFF" in output:
                    os.system("adb shell input keyevent 26")
                    os.system("adb shell input swipe 342 1515 392 594")
                 pyttsx3.speak("Sending Call Invitation")
                 os.system("adb shell am start -a android.intent.action.VIEW -d https://wa.me/+919056240270")
                 time.sleep(5)
                 os.system("adb shell input text Bhai%sCall%sKariyo")
                 time.sleep(3)
                 os.system("adb shell input tap 674 885")
            elif "connect" in text.lower():              
                 pyttsx3.speak("Connecting")
                 subprocess.run("adb tcpip 5555")
                 subprocess.run("adb connect 192.168.127.217:5555")
                 pyttsx3.speak("Connected succesfuly")
            elif "life" in text.lower():
                 battery = psutil.sensors_battery()
                 battery_percentage = battery.percent
                 pyttsx3.speak("Aizen's:" + str(battery_percentage))
                 output = subprocess.check_output("adb shell dumpsys battery | findstr level", shell=True).decode()
                 battery_percent = output.strip().split(":")[-1].strip()
                 pyttsx3.speak(f"Phone's {battery_percent}")
            elif "mine" in text.lower():
                pyttsx3.speak("I got You")
                brave_path = r"C:\Users\ujjwa\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
                subprocess.run([brave_path, "--incognito"], shell=True)
            elif "system" in text.lower():
                 pyttsx3.speak("checking the system")
                 cpu_info = os.popen("wmic cpu get loadpercentage").read()
                 memory_info = os.popen("wmic os get freephysicalmemory").read()
                 disk_info = os.popen("wmic logicaldisk get size,freespace,caption").read()
                 pyttsx3.speak(f"CPU usage is: {cpu_info.strip()}%. Memory available: {memory_info.strip()} KB. Disk space info: {disk_info}")
            elif "speed" in text.lower():
                     pyttsx3.speak("Checking the peice of shit")
                     st = speedtest.Speedtest()
                     download_speed = st.download() / 1_000_000  # Convert to Mbps
                     upload_speed = st.upload() / 1_000_000  # Convert to Mbps
                     pyttsx3.speak(f"Download speed is {download_speed:.2f} Mbps. Upload speed is {upload_speed:.2f} Mbps.")
            elif "random" in text.lower():
                 randomeshit()
            elif "timer" in text.lower():
                 pyttsx3.speak("Timer set for general 30 minutes")
                 start = time.time()
                 timeout = 1800
                 if time.time() - start > timeout:
                     pyttsx3.speak("Time Ran out")
