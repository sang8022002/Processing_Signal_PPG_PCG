
import winsound
import time

frequency = 400  # Frequency in Hz
duration = 2000  # Duration in milliseconds (2 seconds)

start_time = time.time()
winsound.Beep(frequency, duration)
end_time = time.time()

playback_duration = end_time - start_time
print("Playback duration:", playback_duration, "seconds")