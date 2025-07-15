import pyaudio
import asyncio

def main():
    recorder()

    # Debug statement to make sure nothing goes wrong and give me a slight hit of dopamine for not being stupid
    print("No errors")

# Had to make an entirely different async type function for recording because either async is weird, or I am stupid (prob 2nd)
async def recorder():
    # Create an instance of PyAudio and move PortAudio into system resources
    p = pyaudio.PyAudio()

    # Open raw audio file to write to
    bufferFile = open("audioBuffer.raw", "a")

    # Start stream in PyAudio with current device
    stream = p.open(input=True, output=False, rate=16000, channels=1, format="paInt16")

    # Hopefully.... write out... the microphone input???? I have no idea if this works. Gonna loop it 10 secs just in case.
    for i in range(10):
        bufferFile = stream.read()
        await asyncio.wait(1)

    # Close the device stream because I'm not stupid and going to leave the microphone on
    stream.close()

main()