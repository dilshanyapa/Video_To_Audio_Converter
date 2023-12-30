import os
from tkinter import Tk, PhotoImage, filedialog
from tkinter import ttk
from moviepy.editor import VideoFileClip

class VideoToAudioConverter:
    def __init__(self, master):
        self.master = master
        master.title("Video to Audio Converter")
       
        self.label = ttk.Label(master, text="Select a video file:")
        self.label.pack()

        self.select_button = ttk.Button(master, text="Select File", command=self.select_file)
        self.select_button.pack(side="left",padx=30)

        self.convert_button = ttk.Button(master, text="Convert to Audio", command=self.convert)
        self.convert_button.pack(side="right",padx=30)
        
        

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        self.label.config(text=f"Selected file: {file_path}")
        self.input_video_path = file_path

    def convert(self):
        if hasattr(self, 'input_video_path'):
            output_audio_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                               filetypes=[("Audio files", "*.mp3")])
            convert_video_to_audio(self.input_video_path, output_audio_path)
            self.label.config(text=f"Conversion complete!\nAudio saved to: {output_audio_path}")
        else:
            self.label.config(text="Please select a video file first.")

def convert_video_to_audio(input_video, output_audio):
    video_clip = VideoFileClip(input_video)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio)

    video_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    root = Tk()
    root.geometry('400x200')
    root.configure(bg="lightblue")
    app = VideoToAudioConverter(root)
    root.mainloop()