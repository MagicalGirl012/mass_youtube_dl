import youtube_dl
import os
import csv

#Updates the ENTIRE youtube-dl library in question

#Assuming IN the "youtube-scrap" folder
current_dir = os.getcwd()
music_csv_file_path = os.path.join( os.getcwd(), "music.csv" )

#print(music_csv_file_path)

#Process the CSV File
def main():
    with open( music_csv_file_path, "r" ) as music_csv_file:
        csv_reader = csv.reader( music_csv_file, delimiter="," )

        #print(len(csv_reader))

        for index, row in enumerate( csv_reader ):
            if( index == 0 ):
                continue

            elif( len(row) == 3 ):

                os.chdir(current_dir)

                [artist_name, playlist_name, playlist_url] = row

                download_music_path = os.path.join( os.getcwd(), "Music", artist_name, playlist_name, "Media" )
                download_archive_path = os.path.join( os.getcwd(), "Music", artist_name, playlist_name, "dl_archive.txt" )

                process_url(index - 1, artist_name, playlist_name, playlist_url, download_music_path, download_archive_path)

def process_url(index, artist_name, playlist_name, playlist_url, download_music_path, download_archive_path):

    print()

    try:
        os.chdir( download_music_path )
    except Exception as e:
        print("Directory {0} does not exist. \nGenerating Directory\n".format(download_music_path))
        os.makedirs( download_music_path )
        os.chdir( download_music_path )

    print("You are preparing to download:")
    print("Artist: {0}".format( artist_name ))
    print("Playlist: {0}".format( playlist_name ))

    print("The URL is: \n{0}".format( playlist_url ))
    print("\nTo the file location of: \n{0}".format( download_music_path ))
    print("\nWith the download archive of: \n{0}".format( download_archive_path ))

    print("\nIs this information correct?")

    #input("\nEnter to CONFIRM \nControl + C to CANCEL\n")

    index_string = "{:03d}".format(index)

    ydl_opts = {
        'format': 'bestaudio/best',

        'download_archive': download_archive_path,

        'outtmpl': index_string + ' - %(playlist_index)04d - %(title)s.%(ext)s',

        #Start & End Locations
        'playliststart':1,
        'playlistend':1000,

        'ignoreerrors':True,

        #Note: Post Processors Could be the Problem in terms of Run Time. Indefinite ATM. More information needed
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ playlist_url ])

main()
#STOPPER
