import pyaudio
import asyncio
import librosa
import numpy as np
import random

def startAudioStream():
    asyncio.run(recorder())

# Had to make an entirely different async type function for recording because either async is weird, or I am stupid (prob 2nd)
async def recorder():
    print("Starting.")

    # Create an instance of PyAudio and move PortAudio into system resources
    p = pyaudio.PyAudio()

    sampleRate = 16000 # Sampling at 16000 htz

    # Start stream in PyAudio with current device
    stream = p.open(input=True, output=False, rate=sampleRate, channels=1, format=pyaudio.paInt16)

    chunk_duration = 0.1 # Seconds per sample

    # Num of samples per chunk
    chunk_size = int(sampleRate * chunk_duration)

    while True:
        data = stream.read(chunk_size, exception_on_overflow=False)

        audio_np = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0

        f0 = librosa.yin(audio_np, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'), sr=sampleRate)
        pitch = np.median(f0[np.isfinite(f0)]) if np.any(np.isfinite(f0)) else None

        if pitch:
            note = librosa.hz_to_note(pitch)
            print(f"Current pitch: {pitch:.2f} Hz ({note})")
        else:
            select = random.randint(0, 4)
            swears = ["Fuck", "God damnit", "Sigh.", "...I'm sorry", "WHY, WHY WAS I CREATED, WHYYY"]
            print(f"{swears[select]}")

        await asyncio.sleep(chunk_duration)

    # Close the device stream because I'm not stupid and going to leave the microphone on
    stream.close()
    p.terminate()

startAudioStream()