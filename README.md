💡 Inspiration
Sign-opsis was born from a desire to improve accessibility and communication for the deaf and hard of hearing community. We recognized the challenges in real-time sign language translation—especially in fast-paced environments like virtual meetings, customer service interactions, and social media.

Our goal: Create a seamless bridge between spoken content and sign language.

🛠 What It Does
🎧 Input: Audio from videos, podcasts, or live captions

🤟 Output: A pair of animated hands performing American Sign Language (ASL)

🧱 How We Built It
Speech Recognition (ASR):
We used OpenAI’s Whisper to convert spoken language into text. Whisper handles various accents and background noise well. We added a preprocessing step to clean the text output before translation.

Text-to-ASL Translation:
English grammar doesn’t directly map to ASL. We used spaCy to parse and restructure sentences into ASL-style gloss. Each word or letter is then mapped to corresponding hand coordinate data.

Datasets Used:

ASL Citizen – Alphabet videos and metadata (CSV format)

WLASL – A larger collection of glosses and metadata (JSON format)

Hand Animation:
To animate the hands:

We used OpenCV (cv2) to detect and generate point locations for each joint of the hand.

These points were connected to form a structured hand skeleton.

The points were then passed to MediaPipe’s hand landmark model for frame-by-frame visualization.

This multi-step approach gave us greater control over how hand movements were visualized. However, aligning OpenCV’s output with MediaPipe’s landmark model was challenging, especially in the presence of noisy data or varying hand poses.

Final keypoints were stored in a structured coordinates.json, which can be played back to animate a 2D hand.

🚧 Challenges We Faced
Managing Python and system requirements for spaCy, MediaPipe, and Whisper

Precisely aligning frame timing, pose estimation, and sign meaning

Handling Whisper’s performance drop for audio files > 25MB

Ensuring smooth syncing of audio, sign output, and subtitles across the React + Flask stack

Resolving mismatch issues between OpenCV’s keypoints and MediaPipe’s landmark indexing

🏆 Accomplishments We’re Proud Of
Built a full hand joint extractor using OpenCV and MediaPipe

Maintained consistent (x, y) coordinate tracking across frames

Designed a clean, interactive frontend

Integrated Whisper to transcribe large audio files effectively with preprocessing and error handling

📚 What We Learned
Techniques for extracting and synchronizing 2D hand keypoints from both videos and static images

How to integrate audio processing, NLP, and computer vision into a modular backend

The linguistic differences between English and ASL, which are essential for accurate translation

🚀 What’s Next for Sign-opsis
🌍 Support for multiple sign languages (e.g., BSL, ISL)

😀 Facial expression generation (key to expressive ASL)

💻 Integration with Zoom, YouTube, and Google Meet for real-time translation

📦 Offline support for low-connectivity areas

🌐 Multilingual input support:

Convert audio/video in any language

Generate English transcript

Summarize content

Render 3D avatar performing sign language with synced text/audio subtitles
