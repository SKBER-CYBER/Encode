import urllib.request
import os
url = "https://raw.githubusercontent.com/SKBER-CYBER/oggy-core/main/Encode.so"
file_name = "Encode.so"
if not os.path.exists(file_name):
    print("📥 Downloading core file...")
    urllib.request.urlretrieve(url, file_name)
    print("✅ Download done")
import Encode
print("🔥 Loaded successfully")
if hasattr(Encode, "main"):
    encode.main()
module
