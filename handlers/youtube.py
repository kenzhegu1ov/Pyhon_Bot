from pytube import YouTube
import uuid

async def download_video(url: str, quality: str) -> str:
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4', res=quality).order_by('resolution').desc().first()
    stream.download()
    filename = stream.default_filename
    return filename

async def download_audio(url: str, quality: str) -> str:
    yt = YouTube(url)
    video_id = uuid.uuid4().fields[-1]
    yt.streams.filter(only_audio=True).first().download(
        "../media/audio", f'{video_id}.mp3'
    )
    return f'{video_id}.mp3'