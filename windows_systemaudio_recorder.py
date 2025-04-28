import soundcard as sc
import soundfile as sf
import numpy as np
import signal
import sys

# Define variables
output_file_name = "continuous_recording.wav"
sample_rate = 16000
buffer_seconds = 1  # Size of each buffer to read (smaller for more frequent updates)
is_recording = True


# Handle Ctrl+C gracefully
def signal_handler(sig, frame):
    global is_recording
    print("\nStopping recording...")
    is_recording = False


signal.signal(signal.SIGINT, signal_handler)

print(f"Recording system audio continuously to {output_file_name}.")
print("Press Ctrl+C to stop recording.")

try:
    # Open the microphone
    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(
            samplerate=sample_rate) as system_audio:
        # Initialize an empty array to store all audio data
        all_data = np.array([]).reshape(0, 1)

        # Record until Ctrl+C is pressed
        while is_recording:
            # Record a small buffer
            buffer_data = system_audio.record(numframes=sample_rate * buffer_seconds)
            # Keep only the first channel
            buffer_data_mono = buffer_data[:, 0].reshape(-1, 1)
            # Append to our full recording
            all_data = np.vstack((all_data, buffer_data_mono))

            # Optional: Print recording duration
            duration = len(all_data) / sample_rate
            print(f"\rRecording: {duration:.2f} seconds", end="")

        # Save the complete recording
        print("\nSaving recording...")
        sf.write(file=output_file_name, data=all_data, samplerate=sample_rate)
        print(f"Recording saved to {output_file_name}")

except Exception as e:
    print(f"\nError occurred: {e}")
    # Try to save whatever we have
    if 'all_data' in locals() and len(all_data) > 0:
        sf.write(file="emergency_save.wav", data=all_data, samplerate=sample_rate)
        print("Partial recording saved to emergency_save.wav")
