from moviepy.editor import *

clip = (VideoFileClip("video.avi")
        .resize(0.6))
clip.write_gif("DCGAN1.gif")