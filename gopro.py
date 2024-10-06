import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from moviepy.editor import VideoFileClip
from PIL import Image
import numpy as np
import time
import re 
import shutil
from moviepy.editor import VideoFileClip
import os
from PIL import Image

from datetime import datetime

def get_todays_date_folder_name():
    today = datetime.today()
    folder_name = today.strftime("%B%d%Y")  # Format: MonthDayYear
    return folder_name


def custom_resize(clip, new_size):
    """ Custom resize function using PIL with LANCZOS filter. """
    def resize_frame(frame):
        pil_image = Image.fromarray(frame)
        pil_image_resized = pil_image.resize(new_size, Image.LANCZOS)
        return np.array(pil_image_resized)

    return clip.fl_image(resize_frame)

def convert_video(input_path,resolution):
    # Load the video
    clip = VideoFileClip(input_path)
    
    # Resize the video using custom resize function
    clip_resized = custom_resize(clip, resolution)
     # Ensure the audio is included
    if clip.audio:
        print(f"Including audio from {input_path}")
        clip_resized = clip_resized.set_audio(clip.audio)
    else:
        print(f"No audio track found in {input_path}")

    
    # Generate output path by appending "_1080" to the original filename
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_1080{ext}"
 
    # Write the output video, including audio
    clip_resized.write_videofile(output_path, codec='libx264', audio_codec='aac', audio_bitrate='192k')
    
    # Close the clips
    clip.close()
    clip_resized.close()
    
    return output_path

def resize_videos_in_folder(input_folder, output_folder, new_resolution=(1920, 1080)):
    output_folder= output_folder+"/1080"
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List all files in the input folder
    files = os.listdir(input_folder)
    
    # Filter video files (assuming .mp4 format, you can add more extensions if needed)
    video_files = [file for file in files if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    
    if not video_files:
        print("No video files found in the input folder to resize." + input_folder)
        return

    for video_file in video_files:
        output_path = os.path.join(input_folder, video_file)
        convert_video(output_path, new_resolution)
        print(f"Resized and saved video: {output_path}")


def extract_number(filename):
    # Use regex to extract the numeric part from the filename
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else 0


def concatenate_videos(input_folder, output_file):
    # List all files in the input folder
    files = os.listdir(input_folder)
    
    # Filter video files (assuming .mp4 format, you can add more extensions if needed)
    video_files = [file for file in files if file.endswith(('.MP4', '.mp4','.avi', '.mov', '.mkv'))]
    
    if not video_files:
        print("No video files found in the input folder to concatenate.")
        return
    
    video_files.sort(key=extract_number)

    # Load video clips
    clips = [VideoFileClip(os.path.join(input_folder, file)) for file in video_files]
    
    # Concatenate the video clips
    final_clip = concatenate_videoclips(clips)
    
    # Write the concatenated video to the output file
    final_clip.write_videofile(input_folder+"/"+ output_file, codec='libx264')
    
    # Close the clips
    for clip in clips:
        clip.close()

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size, Image.Resampling.LANCZOS)
    resized_image.save(output_image_path)


def compress_video(input_path, output_path, target_bitrate='1M'):
    # Load the video
    clip = VideoFileClip(input_path)
    
    # Compress and save the video
    clip.write_videofile(output_path, codec='libx264', bitrate=target_bitrate, audio_codec='aac')

    # Close the clip
    clip.close()



def copy_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    output_folder+="/"+ get_todays_date_folder_name()
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print("Created the folder " + output_folder)


    # List all files in the input folder
    files = os.listdir(input_folder)

    if not files:
        print("No files found in the input folder to copy.")
        return
    
    for file in files:
        if (file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))):
            src_path = os.path.join(input_folder, file)
            dest_path = os.path.join(output_folder, file)
            try:
                print(f"Beginning to copied file: {src_path} to {dest_path}")
                shutil.copy2(src_path, dest_path)  # copy2 preserves metadata
                print(f"Finished coping file: {src_path} to {dest_path}")
            except Exception as e:
                print(f"Error copying file {src_path}: {e}")
 

def remove_non_mp4_files(folder):
    # List all files in the folder
    files = os.listdir(folder)
    
    # Remove files that don't end in .mp4
    for file in files:
        if not file.lower().endswith('.mp4'):
            file_path = os.path.join(folder, file)
            try:
                print(f"Removing non-mp4 file: {file_path}")
                os.remove(file_path)
            except Exception as e:
                print(f"Error removing file {file_path}: {e}")



def rename_videos_by_creation_time(folder):
    # List all files in the folder
    files = os.listdir(folder)
    
    # Filter video files to include only .mp4 format
    video_files = [file for file in files if file.lower().endswith('.mp4')]
    
    # Sort files by creation time
    video_files.sort(key=lambda x: os.path.getctime(os.path.join(folder, x)))
    
    # Rename files
    for i, video_file in enumerate(video_files, start=1):
        new_name = f'P{i}.mp4'
        old_path = os.path.join(folder, video_file)
        new_path = os.path.join(folder, new_name)
        try:
            os.rename(old_path, new_path)
            print(f"Renamed {old_path} to {new_path}")
        except Exception as e:
            print(f"Error renaming file {old_path} to {new_path}: {e}")

def downloadLastestVids():
    input_folder="/Volumes/GoPro/DCIM/100GOPRO/"
    output_folder = '/Volumes/The Flash/PhotosWithVideos/2024/InterracialSets2024/' # Replace with your output folder path
    
    remove_non_mp4_files(input_folder)
    rename_videos_by_creation_time(input_folder)
    copy_files(input_folder, output_folder)

def convertto1080Videos():
    # Record start time
    start_time = time.time()

  

   
    input_folder = '/Volumes/The Flash/PhotosWithVideos/2024/InterracialSets2024/July172024' # Replace with your output folder path
    resize_videos_in_folder(input_folder,input_folder)
     # Record end time
    end_time = time.time()

    # Calculate the time taken
    time_taken = end_time - start_time
    time_taken= time_taken/60
    print(f"Time taken by the function: {time_taken} minutes")

if __name__ == "__main__":
    #downloadLastestVids()
    concatenate_videos("/Volumes/The Flash/PhotosWithVideos/2024/InterracialSets2024/September242024","output.mp4")

