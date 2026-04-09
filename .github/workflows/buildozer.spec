[app]
title = My App
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

# (optional but useful)
android.api = 31
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1