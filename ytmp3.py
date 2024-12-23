import os, re
from pytubefix import YouTube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print("{:.2f}".format(percentage_of_completion))


i = input()
vid = YouTube(i, use_oauth=True, allow_oauth_cache=True)

vid.register_on_progress_callback(on_progress)
audio = vid.streams.get_audio_only()
file_name = re.sub(r'[<>:"/\\|?*]', '-', "".join(audio.default_filename.split()[:-1]) + ".mp3")
audio.download(filename=file_name)
os.replace(os.getcwd() + "\\" + file_name, f"C:\\Users\\{os.getlogin()}\\Music\\" + file_name)
