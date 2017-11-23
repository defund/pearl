import appdirs
import os

dirs = appdirs.AppDirs('hangups', 'hangups')
path = os.path.join(dirs.user_cache_dir, 'refresh_token.txt')
os.remove(path)