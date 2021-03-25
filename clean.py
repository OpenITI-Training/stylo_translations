import os
import re
from openiti.helper.ara import deNoise, normalize_ara_heavy


def clean(s):
    # remove header
    s = re.split("#META#Header#End#?[\r\n]+", s)[-1]

    # remove page numbers:
    s = re.sub("PageV[^P]+P\w+", "", s)

    # remove title tags:
    s = re.sub("### \|+ ", "", s)

    # remove paragraph and line markers:
    s = re.sub("# |~~", "", s)

    # remove short vowels etc.:
    s = deNoise(s)

    # normalize alifs, alif maqsura, hamzas and ta marbuta:
    s = normalize_ara_heavy(s)

    return s

folder = "transl_first"
outfolder = folder + "_cleaned"
if not os.path.exists(outfolder):
    os.makedirs(outfolder)
for fn in os.listdir(folder):
    print(fn)
    fp = os.path.join(folder, fn)
    with open(fp, mode="r", encoding="utf-8") as file:
        text = file.read()
    text = clean(text)
    fn = re.sub("\.mARkdown", "", fn)
    with open(os.path.join(outfolder, fn), mode="w", encoding="utf-8") as file:
        file.write(text)
    
