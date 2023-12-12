import requests
from PIL import Image
from io import BytesIO
import os

def download_sprite_images(json_url, sprite_sheet_url, output_folder):
    # JSON 데이터를 가져옵니다
    response = requests.get(json_url)
    data = response.json()

    # Sprite 시트 이미지를 다운로드합니다
    sprite_sheet_response = requests.get(sprite_sheet_url)
    sprite_sheet = Image.open(BytesIO(sprite_sheet_response.content))

    # 출력 폴더가 없으면 생성합니다
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for champion_name, champion_data in data['data'].items():
        image_data = champion_data['image']
        x = image_data['x']
        y = image_data['y']
        w = image_data['w']
        h = image_data['h']

        # Sprite 시트에서 개별 이미지를 추출합니다
        sprite = sprite_sheet.crop((x, y, x + w, y + h))
        sprite.save(os.path.join(output_folder, f'{champion_name}.png'))

# JSON URL과 Sprite 시트 URL
json_url = 'https://ddragon.leagueoflegends.com/cdn/13.23.1/data/ko_KR/tft-champion.json'
sprite_sheet_url = 'https://ddragon.leagueoflegends.com/cdn/13.23.1/img/sprite/tft-champion0.png'  # 예시 URL, 실제 URL로 대체 필요

# 이미지를 저장할 폴더
output_folder = 'tft_champions'

download_sprite_images(json_url, sprite_sheet_url, output_folder)
