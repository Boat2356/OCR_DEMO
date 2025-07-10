import base64
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def encode_image_to_base64(image_path):
  with open(image_path, "rb") as f:
      return base64.b64encode(f.read()).decode("utf-8")

image_path = "./Invoice/Thapthai.png"
image_data = encode_image_to_base64(image_path)

response = client.chat.completions.create(
  model="typhoon-ocr-3b",
  messages=[
      {
          "role": "system",
          "content": "You are an OCR model. Extract all readable text from the image."
      },
      {
          "role": "user",
          "content": [
              {"type": "text", "text": "Please extract text from this image:"},
              {
                  "type": "image_url",
                  "image_url": {
                      "url": f"data:image/png;base64,{image_data}"
                  }
              }
          ]
      }
  ],
  max_tokens=16384,
  extra_body={
              "repetition_penalty": 1.2,
              "temperature": 0.1,
              "top_p": 0.6,
          },
)

print(response.choices[0].message.content)
