# Image Renamer

Goes through every image file in a given directory and renames them using GPT-4 Vision.

> :warning: May incur large costs and/or rate limits if there are a lot of images. `label_images.py` labels each image with its own prompt and goes through all the subdirectories in a given directory recursively.

## Useage

- Copy `.env.template` in the root directory to a `.env` file and paste your OpenAI API key.
- Create a virtual environment and run 
  - `pip install -r requirements.txt`
- Run 
  - `python label_images.py <path-to-your-directory>`
