
import pytube
import youtube_downloader
import file_converter

print('''
What do you want?
(a) Download YouTube Videos Manually
(b) Download a complete playlist
''')

choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        youtube_downloader.download_playlist(link, quality)
        print("Download finished!")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)

else:
    print("Invalid input! Terminating...")