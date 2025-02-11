import requests
from tqdm import tqdm

url = "https://www.sample-videos.com/text/Sample-text-file-10kb.txt"

with requests.get(url, stream=True) as response:
    response.raise_for_status()
    total_size = int(response.headers.get("content-length", 0))
    with open("largestream.zip", "wb") as f:
        with tqdm(total=total_size, unit="B", unit_scale=True, desc="Downloading") as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                pbar.update(len(chunk))


print("File Downloaded Successfully")