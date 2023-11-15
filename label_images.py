"""Assign names to all images in a directory and rename them."""

import base64
import os
import re

import click
from dotenv import load_dotenv
import requests
from tqdm import tqdm

IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".bmp")
PROMPT = (
    "Give a reasonable file name to this image and enclose it in triple quotes (```). "
    "Do not include any file extension."
)


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_image_name(image_path: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    base64_image = encode_image(image_path)
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        "max_tokens": 300,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )
    content = response.json()["choices"][0]["message"]["content"]
    name = re.search(r"```(.*?)```", content, re.DOTALL).group(1).strip()
    return name


def get_image_paths(directory: str) -> list[str]:
    image_paths = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            image_paths.append(os.path.join(directory, filename))
    return image_paths


def name_images(image_paths):
    progress_bar = tqdm(image_paths, total=len(image_paths))
    for path in progress_bar:
        new_name = get_image_name(path)
        new_name_with_extension = f"{new_name}{os.path.splitext(path)[1]}"
        new_file_path = os.path.join(os.path.dirname(path), new_name_with_extension)
        os.rename(path, new_file_path)


@click.command()
@click.argument("directory")
def main(directory):
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    image_paths = get_image_paths(directory)
    name_images(image_paths)


if __name__ == "__main__":
    load_dotenv()
    main()
