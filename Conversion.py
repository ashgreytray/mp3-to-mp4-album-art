import moviepy.editor as mp
import easygui
import os
import eyed3

audio_types = ['*.mp3']
audioPath = easygui.fileopenbox(
    msg="Select Audio",
    title="Audio",
    default='*.mp3',
    filetypes=audio_types)
audio_file = eyed3.load(audioPath)
# temp save album art
album_art_path = None
if audio_file.tag is not None and audio_file.tag.images:
    image = audio_file.tag.images[0]
    album_art_path = os.path.join(os.path.expanduser("~"), "Documents", "album_art.jpg")
    with open(album_art_path, "wb") as img_file:
        img_file.write(image.image_data)
    print(f"Album art extracted to: {album_art_path}")
else:
    # yo no hablo album art
    print("No album art for the mp3 provided found. Please provide another image")
    image_types = ['*.jpg', '*.jpeg', '*.png']
    album_art_path = easygui.fileopenbox(
        msg="Select Image",
        title="Image",
        default='*.jpg',
        filetypes=image_types
    )

def converter(audioPath, imagePath):
    nome = str(os.path.basename(audioPath))
    name = os.path.splitext(nome)[0]

    outputPath = os.path.join(os.path.expanduser("~"), fr"Videos\{name}.mp4")

    audio = mp.AudioFileClip(audioPath, fps=44100)
    video = mp.ImageClip(imagePath)

    # duration match
    video_duration = audio.duration
    final_video = video.set_audio(audio).set_duration(video_duration)
    final_video.write_videofile(outputPath, fps=12)
    print(f"Video saved to: {outputPath}")

converter(audioPath, album_art_path)
