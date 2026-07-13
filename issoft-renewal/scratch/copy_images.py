import os
import shutil

src_dir = r"C:\Users\kukky\.gemini\antigravity-ide\brain\94018755-1af5-48bb-a839-06d51a31b99b"
dest_dir = r"c:\kukky_Work\Antigravity_PJ\HomePage_Renewal\issoft-renewal\public\images\port"

mapping = {
    "media__1783904435109.png": "3h.png",
    "media__1783904435098.png": "snbi.png",
    "media__1783904435129.png": "daegu.png"
}

os.makedirs(dest_dir, exist_ok=True)

for src_name, dest_name in mapping.items():
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
        print(f"Successfully copied {src_name} -> {dest_name}")
    else:
        print(f"Error: Source not found {src_path}")
