import win32com.client

speaker=win32com.client.Dispatch("SAPI.SpVoice")
l=["Jim"]

for i in l:
    speaker.speak(f"when i see you {l} i feel like i'm seeing heaven!")