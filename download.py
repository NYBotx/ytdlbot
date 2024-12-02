import yt_dlp
import ffmpeg
import os

def process_download(url, resolution, download_dir):
    """Download video and merge audio if necessary."""
    ydl_opts = {
        "format": f"bestvideo[height<={resolution}]+bestaudio/best",
        "outtmpl": f"{download_dir}/%(title)s.%(ext)s",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
        title = info["title"]

    # Merge audio if required
    if resolution in ["720p", "1080p"]:
        audio_path = file_path.replace(".mp4", "_audio.mp3")
        merged_path = file_path.replace(".mp4", "_merged.mp4")

        # Extract audio and merge
        ffmpeg.input(file_path).output(audio_path).run(overwrite_output=True)
        ffmpeg.input(file_path).input(audio_path).output(merged_path).run(overwrite_output=True)

        os.remove(file_path)  # Cleanup original video
        file_path = merged_path

    return file_path, title
      
