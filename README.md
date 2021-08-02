# Batch-map-youtube-dl
## Description
> This project has its body when I was dealing with the production of NTUKENDO club's ipponshu. I tried to collect the source video in each competition, which was already uploaded to YouTube. However, for post-prouction's convenience, it wasn't a good idea putting them in the same folder. So, I figured out this simple python code.

## Prerequisites
- Linux, MacOS or Windows
- youtube-dl
- python3
Note: Downlaod instruction of youtube-dl could be found [here](http://ytdl-org.github.io/youtube-dl/download.html)

## Usage
First, put the playlist containing the url of each video in `src/`. Then run the following code:
```
python3 scripts/batch-map-dl.py
```
For Linux and Mac user, make sure youtube-dl installed.
For Windows user, make sure you put the `youtube-dl.exe` under the same directory.

## Repository structure
| Path | Description |
| -------- | -------- |
| .     | Repo root folder |
| ├ scripts | Folder containing main code |
| ├ src | Folder containing playlist |
