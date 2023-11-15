# Image Labeler

Script that goes through every image file in a given directory and renames them using GPT-4 Vision.

## Useage

- Copy `.env.template` in the root directory to a `.env` file and paste your OpenAI API key.
- Create a virtual environment and run 
  - `pip install -r requirements.txt`
- Run 
  - `python label_images.py <path-to-your-directory>`