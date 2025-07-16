import pyaudio
import asyncio
import librosa

def collectBuffer():
    asyncio.run(recorder())

    # Debug statement to make sure nothing goes wrong and give me a slight hit of dopamine for not being stupid
    print("No errors")

# Had to make an entirely different async type function for recording because either async is weird, or I am stupid (prob 2nd)
async def recorder():
    # Create an instance of PyAudio and move PortAudio into system resources
    p = pyaudio.PyAudio()

    # Open raw audio file to write to
    bufferFile = open("audioBuffer.raw", "wb") # Write in binary mode

    # Start stream in PyAudio with current device
    stream = p.open(input=True, output=False, rate=16000, channels=1, format=pyaudio.paInt16)


    chunk_duration = 0.1 # Seconds per sample

    # Num of samples per chunk
    chunk_size = int(16000 * chunk_duration)

    # Hopefully.... write out... the microphone input???? I have no idea if this works. Gonna loop it 10 secs just in case.
    for i in range(int(10 / chunk_duration)):
        data = stream.read(chunk_size)
        bufferFile.write(data)
        await asyncio.sleep(chunk_duration) # Save every 0.1 secs

    # Close the device stream because I'm not stupid and going to leave the microphone on
    stream.close()
    bufferFile.close()