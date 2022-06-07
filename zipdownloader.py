import zipfile, wget, zipfile, os, sys

filename = '\yourfile.zip'
url = 'yoururl'
dir = 0

def bar_progress(current, total, width=80):
  progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
  sys.stdout.write("\r" + progress_message)
  sys.stdout.flush()

def Download(url, dir):
     wget.download(url, dir, bar=bar_progress)

def TryUnzip(dir, filename):
    with zipfile.ZipFile(dir + filename) as zf:
        zf.extractall(dir)

dir = input("Select a directory:")
Download(url, (dir + filename))
print("\nUnZipping...")
try:
    TryUnzip(dir, filename)
    os.remove(dir + filename)
    print("Done!")
except:
    print("UnZip error!")
input()
exit