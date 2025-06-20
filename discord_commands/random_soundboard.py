import random
import time

SOUNDS = [
    "sound1.mp3",
    "sound2.mp3",
    "sound3.mp3"
]

def play_random_sound(token, guild_id, voice_channel_id):
    # Placeholder implementation
    sound = random.choice(SOUNDS)
    print(f"\033[92mPlaying sound {sound} in guild {guild_id}, voice channel {voice_channel_id} with token [{token[:6]}...] (mock implementation).\033[0m")
    time.sleep(2)  # simulate playing sound

def run_with_token(token):
    guild_id = input(f"\033[95mEnter guild ID for token [{token[:6]}...]: \033[0m")
    voice_channel_id = input("\033[95mEnter voice channel ID to play sound: \033[0m")
    play_random_sound(token, guild_id, voice_channel_id)
    choice = input("\033[95m[ 0 ] Back: \033[0m").strip()
    if choice == '0':
        return

def run_all_tokens():
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f if line.strip()]
    guild_id = input("\033[95mEnter guild ID for all tokens: \033[0m")
    voice_channel_id = input("\033[95mEnter voice channel ID to play sound for all tokens: \033[0m")
    for token in tokens:
        print(f"Playing random sound for token [{token[:6]}...]")
        play_random_sound(token, guild_id, voice_channel_id)

if __name__ == "__main__":
    run_all_tokens()
