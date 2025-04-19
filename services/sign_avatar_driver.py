import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

CLIP_DIR = "sign_assets/gloss_clips"

def generate_sign_video(gloss_string, output_path="data/generated_sign.mp4"):
    gloss_words = gloss_string.strip().split()

    clips = []
    for word in gloss_words:
        clip_path = os.path.join(CLIP_DIR, f"{word.upper()}.mp4")
        if os.path.exists(clip_path):
            clips.append(VideoFileClip(clip_path))
        else:
            print(f"⚠️ Missing clip for: {word}")

    if not clips:
        raise ValueError("No matching clips found.")

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path, codec="libx264")

    return output_path