[app]
# (str) Title of your application
title = Ashimadi Launcher 3D

# (str) Package name
package.name = ashimadilauncher3d

# (str) Package domain (needed for android/ios packaging)
package.domain = com.ashimadi

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,xml,json,glsl,ttf,wav,mp3,ogg,so,a,txt

# (list) List of directory to include (let empty to include all the files)
source.include_dirs = assets,res,shaders,modules,modi,locales,presets,build

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pillow,pyjnius,android

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required
android.minapi = 21

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
