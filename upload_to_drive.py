import json
import requests
headers = {"Authorization": " "}
para = {
    "name": "123.zip",
    "parents":["13Qimc5BJTiX-S8g26zWXUh47-Meu4bF7"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("colab_path.zip", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
