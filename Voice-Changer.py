'''This code loads an audio file named "input.wav", changes the pitch by 2 semitones (making it higher), and then exports the modified audio to a file named "output.wav". You can adjust the amount of pitch change by modifying the octaves variable. To make the pitch lower, use a negative value for octaves.'''


from pydub import AudioSegment

# Load the audio file
sound = AudioSegment.from_wav("input.wav")

# Change the pitch by 2 semitones (higher)
octaves = 2
new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
high_pitched_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
high_pitched_sound = high_pitched_sound.set_frame_rate(sound.frame_rate)

# Export the modified audio file
high_pitched_sound.export("output.wav", format="wav")
