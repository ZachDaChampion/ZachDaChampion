import os
import sys
from PIL import Image, ImageOps

# CLI arguments
# --source: Source folder (default: res-raw)
# --dest: Destination folder (default: res)
# --quality: Quality of compressed images (0-100) (default: 80)
# --resize: Resize images to specified max width and height (<width>x<height>) (default: 720x720)

# Get CLI arguments
args = sys.argv
source = "res-raw"
dest = "res"
quality = 80
resize = "720x720"
for arg in args:
    if arg.startswith("--source="):
        source = arg.replace("--source=", "")
    elif arg.startswith("--dest="):
        dest = arg.replace("--dest=", "")
    elif arg.startswith("--quality="):
        quality = int(arg.replace("--quality=", ""))
    elif arg.startswith("--resize="):
        resize = arg.replace("--resize=", "")

# Clear 'res' folder
for root, dirs, files in os.walk(dest):
    for file in files:
        os.remove

# Navigate file structure in 'res-orig' folder
for root, dirs, files in os.walk(source):
    for file in files:

        # Get file path
        path = os.path.join(root, file)

        # Remove specific arguments from output filename
        new_path = ".".join(
            [part for part in path.replace(source, dest).split(".") if not part.startswith("--")]
        )

        # Create new folder if it doesn't exist
        if not os.path.exists(os.path.dirname(new_path)):
            os.makedirs(os.path.dirname(new_path))

        # Open image
        img = Image.open(path)
        img = ImageOps.exif_transpose(img)

        """
        Resize image
        """

        # Check if file has specific arguments
        file_quality = quality
        file_resize = resize
        for field in file.split("."):
            if field.startswith("--quality="):
                file_quality = int(field.replace("--quality=", ""))
            if field.startswith("--resize="):
                file_resize = field.replace("--resize=", "")

        if file_resize == "" or file_resize == "0x0":
            continue

        current_width, current_height = img.size  # Get current width and height
        max_width, max_height = file_resize.split("x")  # Get max width and height
        max_width = int(max_width)
        max_height = int(max_height)

        # Resize image if it's bigger than max width or height
        if current_width > max_width or current_height > max_height:
            ratio = min(max_width / current_width, max_height / current_height)
            new_width = int(current_width * ratio)
            new_height = int(current_height * ratio)
            img = img.resize((new_width, new_height), Image.LANCZOS)

        # Save image
        img.save(new_path, optimize=True, quality=file_quality)
