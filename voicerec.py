import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

test_filename = "ZOHAIR.WAV"
FILENAME_FROM_MIC = "RECORDING.WAV"
VOICE_TEXT_FILENAME = "VOICE_AS_TEXT.txt"

r = sr.Recognizer() # initialize the recognizer that can identify speech

def recognize_from_file(filename): # function recognize_from_file takes single argument filename
   with sr.AudioFile(filename) as source: # open the file
       audio_data = r.record(source) # listen for the data and store into audio.data
       try:
           text = r.recognize_google(audio_data) # recognize (convert from speech to text) using googles software 
       except sr.UnknownValueError:
           text = "Could not understand audio"
       return text # returns calculated text
    
def recognize_from_microphone(file_to_write): # function recognize_from_microphone takes single argument file_to_write
    SAMPLE_RATE = 44100 # sample rate of audio recording to 44100 Hz
    duration = 5 # number of seconds that audio will be recorded
    audio_recording = sd.rec(duration * SAMPLE_RATE, samplerate = SAMPLE_RATE, channels = 1, dtype = 'int32') # sd.rec is a function from sd library used to record audio
    print("Recording 5 seconds of audio...") # output this into terminal
    sd.wait() # pauses code execution until recording is finished
    print("Audio recording complete, playing audio...") # output this into terminal
    sd.play(audio_recording, SAMPLE_RATE) # plays back the recorded audio
    sd.wait() # pauses code execution until recording is finished playing
    print("Playing audio complete. Check txt and wav files!") # output this into terminal
    wav.write(file_to_write, SAMPLE_RATE, audio_recording) # takes recorded audio and converts it into a WAV file

def save_text_to_file(text, filename): # function save_text_to_file takes double argument text and filename
    with open(filename, 'w') as f: # opens the file in write mode
        f.write(text) # writes the text to the file

if __name__ == "__main__": # if the module that is being run is the main program, then the code within this if-block will be executed. otherwiseif imported as a module in another script, won't execute
    recognize_from_microphone(FILENAME_FROM_MIC) # calls function with argument FILENAME_FROM_MIC
    text_from_voice = recognize_from_file(FILENAME_FROM_MIC) # calls a function recognize_from_file with argument FILENAME_FROM_MIC and then stores text into text_from_voice
    save_text_to_file(text_from_voice, VOICE_TEXT_FILENAME) # calls function save_text_to_file with arguments text_from_voice and VOICE_TEXT_FILENAME

    

