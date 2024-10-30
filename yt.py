import ffmpeg, os
from pytubefix import YouTube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print("{:.2f}".format(percentage_of_completion))


i = input()
vid = YouTube(i, use_oauth=True, allow_oauth_cache=True)

video = vid.streams.filter(resolution=("1080p" or "1440p" or "2160p")).last() or vid.streams.order_by("resolution").last()
vid_name = "a.mp4"
print("Video Located")


vid.register_on_progress_callback(on_progress)
video.download(filename = vid_name)

if not video.is_progressive:
    audio = vid.streams.get_audio_only()
    aud_name = "b.mp4"
    audio.download(filename = aud_name)
    ffmpeg.output(ffmpeg.input(vid_name), ffmpeg.input(aud_name), filename=audio.default_filename, f="mp4", codec="copy").run()
    os.remove(vid_name)
    os.remove(aud_name)