import os
from pathlib import Path

root = os.getcwd()
titlelist = os.listdir("src")

# download video to exp/
for title in titlelist:
	f = open(os.path.join("src", title), "r")
	url_list = f.read().splitlines()
	f.close()
	
	# remove title's extension; mkdir(); chdir()
	game_name = Path(title).stem
	path_to_export = os.path.join("exp", game_name)
	os.makedirs(path_to_export)
	os.chdir(path_to_export)

	for url in url_list:
		#cmd = "echo %s >> url_list" %url
		cmd = "youtube-dl %s" %url
		os.system(cmd)
	
	os.chdir(root)
