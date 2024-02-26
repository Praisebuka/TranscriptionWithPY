import openai

API_KEY = '<API KEY>'
model_id = 'whisper-1'

media_file_path = 'video_japanese.mp4'
media_file = open(media_file_path, 'rb')

response = openai.Audio.translate(
    api_key=API_KEY,
    model=model_id,
    file=media_file,
    prompt=''
)

print(response.data['srt'])