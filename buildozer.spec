[app]
title = Ashimadi Launcher 3D
package.name = ashimadilauncher3d
package.domain = com.ashimadi
source.dir = .
source.include_exts = py,png,jpg,jpeg,xml,json,glsl,ttf,wav,mp3,ogg,so,a,txt
source.include_dirs = assets,res,shaders,modules,modi,locales,presets,build
version = 1.0.0
requirements = python3,kivy,pillow,pyjnius,android
orientation = sensor
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
