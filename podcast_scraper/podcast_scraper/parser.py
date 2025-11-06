from importlib.resources import contents

from crawler import response

f = open("podcast.txt","a+")

datas = response.json()

transcript = []
current_speaker = None
current_text = []

for seg in datas["segments"]:
   speaker = seg.get("speaker", "Unknown")
   words_list = [w["text"] for w in seg["words"]]
   text = " ".join(words_list).strip()

   if speaker != current_speaker:
      if current_text:
         transcript.append(" ".join(current_text))
         transcript.append(" ")
      current_speaker = speaker
      current_text = [text]
   else:
      current_text.append(text)

if current_text:
   transcript.append(" ".join(current_text))


for para in transcript:
   f.write(para + "\n")

f.close()