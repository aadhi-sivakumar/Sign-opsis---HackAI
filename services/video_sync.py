import ffmpeg
import os

def overlay_sign_video(background_path, overlay_path, output_path="data/final_output.mp4"):
    if not os.path.exists(background_path):
        raise FileNotFoundError(f"Background video not found: {background_path}")
    if not os.path.exists(overlay_path):
        raise FileNotFoundError(f"Overlay video not found: {overlay_path}")

    (
        ffmpeg
        .input(background_path)
        .filter_complex(
            f"[0:v][1:v] overlay=W-w-10:H-h-10"  # Bottom-right PiP
        )
        .output(output_path, codec="libx264", crf=23, preset="medium")
        .run(overwrite_output=True)
    )
    return output_path