# Image Renamer

Goes through every image file in a given directory and renames them using GPT-4 Vision.

> :warning: May incur large costs and/or rate limits if there are a lot of images. `label_images.py` goes through all subdirectories in a given directory recursively and labels every image with their own GPT-4 completion (including images that may already have a descriptive filename!).

## Useage

- Copy `.env.template` in the root directory to a `.env` file and paste your OpenAI API key.
- Create a virtual environment and run 
  - `pip install -r requirements.txt`
- Run 
  - `python label_images.py <path-to-your-directory>`
