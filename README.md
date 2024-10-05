# goproextract

Video Processing Script
Overview
This script provides a suite of tools to manipulate videos, including resizing, concatenating, compressing, and organizing video files. It also handles video and image file management with functionality to sort, rename, copy, and remove non-MP4 files. Designed to work with video content from devices like GoPro, the script supports automation tasks like resizing videos to 1080p resolution and concatenating them into a single file.

Features
Resize Videos: Resize videos to custom resolutions (default: 1080p).
Concatenate Videos: Combine multiple video files into one seamless video.
Compress Videos: Compress videos to a target bitrate.
Copy and Organize Files: Automatically copy videos into a dated folder structure.
Remove Non-MP4 Files: Remove unwanted files from a folder, leaving only .mp4 videos.
Rename Videos by Creation Time: Rename videos in a folder sequentially based on their creation time.
Download and Prepare Latest Videos: Automate downloading, organizing, and preparing the latest videos for further processing.
Requirements
Python 3.x
Required Python libraries:
moviepy
PIL (Pillow)
numpy
shutil
datetime
re
os
You can install them using:
bash
Copy code
pip install moviepy pillow numpy
Functions
1. get_todays_date_folder_name()
Generates a folder name based on the current date in the format MonthDayYear.

2. custom_resize(clip, new_size)
Resizes a video clip to a custom size using the LANCZOS filter from PIL.

3. convert_video(input_path, resolution)
Converts a video to the specified resolution, ensuring audio is retained. Outputs a new video file with _1080 appended to the filename.

4. resize_videos_in_folder(input_folder, output_folder, new_resolution=(1920, 1080))
Resizes all videos in a given folder to the specified resolution and saves them in a new folder.

5. extract_number(filename)
Extracts numeric parts from filenames using regex, useful for sorting.

6. concatenate_videos(input_folder, output_file)
Concatenates multiple video files in a folder and outputs a single video file.

7. resize_image(input_image_path, output_image_path, size)
Resizes an image to the specified dimensions and saves it.

8. compress_video(input_path, output_path, target_bitrate='1M')
Compresses a video file to the specified bitrate.

9. copy_files(input_folder, output_folder)
Copies video files from the input folder to the output folder, creating a subfolder based on the current date.

10. remove_non_mp4_files(folder)
Removes all non-MP4 files from the specified folder.

11. rename_videos_by_creation_time(folder)
Renames video files in the folder based on their creation time.

12. downloadLastestVids()
A wrapper function to automate the process of downloading, cleaning, renaming, and copying the latest video files from a specific folder.

13. convertto1080Videos()
Resizes all videos in a specified folder to 1080p.

Usage
Resizing Videos to 1080p:
bash
Copy code
python script.py
Uncomment convertto1080Videos() in the main function to run the resizing process for all videos in the specified folder.

Concatenating Videos:
bash
Copy code
python script.py
The script concatenates all videos in a folder when concatenate_videos() is called.

Download Latest Videos:
bash
Copy code
python script.py
Call the downloadLastestVids() function to automate the video downloading and organizing process.

Notes
Make sure to adjust folder paths in the script to match your setup.
The script supports .mp4, .avi, .mov, and .mkv video formats by default, but more formats can be added as needed.
License
This script is free to use and modify under the MIT License
