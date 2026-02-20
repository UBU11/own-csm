from sarvamai import SarvamAI
from sarvamai.play import save
import os
from dotenv import load_dotenv
import base64

load_dotenv()

api_key = os.getenv("SARVAM_API_KEY")

client = SarvamAI(api_subscription_key=api_key)

audio = client.text_to_speech.convert(
    text="hai its me ubu, nice to meet you",
    target_language_code="ml-IN",
    model="bulbul:v3",
    speaker="rohan"
)
save(audio, "./audio.wav")
