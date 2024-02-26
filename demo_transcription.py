# Active and Accurate piece
import openai

API_KEY = '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'
model_id = 'whisper-1'

media_file_path = 'checkThisOne.m4a'
media_file = open(media_file_path, 'rb')

response = openai.audio.transcribe(
    api_key=API_KEY,
    model=model_id,
    file=media_file,
    response_format = 'srt'

)


print(response.data['srt'])


# Less active but an accurate piece as well

# import openai

# # Set your OpenAI API key
# openai.api_key = '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'

# # Open the audio file
# with open("checkThisOne.m4a", "rb") as audio_file:
#     # Transcribe the audio
#     transcript = openai.audio.transcriptions.create(
#         model="whisper-1", 
#         file=audio_file, 
#         response_format="text"
#     )

# # Print the transcription
# print(transcript)
