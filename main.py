import gallery_dl
from io import StringIO

logs = StringIO()

def on_metadata(metadata):
    print(metadata["_paths_"])

gallery_dl.main(["https://www.tiktok.com/@liverpoolfc", "--no-download", "-o", "tiktok-range=1-3"], logs, on_metadata)

print("end")
print(logs.getvalue())
