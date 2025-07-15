import pyaudio

def main():
    # Create an instance of PyAudio and move PortAudio into system resources
    p = pyaudio.PyAudio()

    # Open raw audio file to write to
    bufferFile = open("audioBuffer.raw", "a")

    # Start stream in PyAudio with current device
    stream = p.open(input=True, output=False, rate=16000, channels=1, format="paInt16")

    bufferFile = stream.read()

    stream.close()

    print("No errors")

main()