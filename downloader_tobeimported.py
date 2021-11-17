import pytube

def download_vdo(url, res):
    itag = choose_resolution(res)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def download_videos(urls, res):
    for url in urls:
        download_video(url, res)

def download_playlist(url, res):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, res)

def choose_resolution(res):
    if res in ["low", "360", "360p"]:
        itag = 18
    elif res in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif res in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif res in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links