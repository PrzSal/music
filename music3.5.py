#!/usr/bin/env python3
import sys
import csv
import random
def print_menu():
    menus = ('''Choose the action:
     1) Add new album
     2) Find albums by artist
     3) Find albums by year
     4) Find musician by album
     5) Find albums by letter(s)
     6) Find albums by genre
     7) Calculate the age of all albums
     8) Choose a random album by genre
     9) Show the amount of albums by an artist *
    10) Find the longest-time album *
     0) Exit''')
    print(menus)


def reader_music():
    '''In this function open csv file and create 2 tuples in tuples and return music'''
    csvfile = open("music.csv", "r")   # open cvs and setup csv.reader settings
    csvfile.seek
    upper_stream = (line.upper() for line in csvfile) # Create upper letter
    reader = csv.reader(upper_stream, delimiter="|")
    music_complet = []
    for music_part in reader:
        music = ((music_part[0], music_part[1]), (music_part[2], music_part[3], music_part[4]))
        music_complet.append(music)
    return music_complet


def add_new_album(music_complet):
    '''First function = menu:1. In loop create new lines in csv file
    and check do know write artist and album in csv file.'''
    stop = 0    # start loop
    while stop == 0:
        new_artist = input("Please give me Artist: ").upper() #add new artist
        new_albums = input("Please give me Album: ").upper()
        artist = []
        album = []
        for music_part in music_complet:    # create new list with artist and albums
            artist += [music_part[0][0]]
            album += [music_part[0][1]]
        if any(new_artist in s for s in artist) and any(new_albums in s for s in album):
            print('I know this artis and album, please insert oder!')   # check new artist and album in music csv
        else:   # after check continue write new lines in csv file
            year = input("Please give me Year: ")
            genre = input("Please give me genhre: ").upper()
            long_album = input("How long this album: ").upper()
            complete = new_artist+" | "+new_albums+" | "+year+" | "+genre+" | "+long_album+"\n"
            musicwrite = open("music.csv", "a") # create file to write in the end line
            musicwrite.writelines(complete) #save
            musicwrite.close()
            print('Changes saved!')
            stop += 1


def search_by_artist(music_complet):
    stop = 0
    while stop == 0:
        search = input("Please give me Artist: ").upper()
        for artist in music_complet:
            if search in artist[0][0] and len(search) > 0:      # check search in artist
                print("------------------------------------------------------")
                print(" Albums: ", artist[0][1], " Artist: ", artist[0][0])
                print("------------------------------------------------------")
                stop += 1   # stop loop
        else:
            if stop == 0:   # wrong word or none write loop on
                print("I don't know this Artist!")
            else:
                print('')


def search_by_year(music_complet):
    stop = 0
    while stop == 0:
        search = input("Please give me the date of release of the album: ")
        for year in music_complet:
            if search in year[1][0] and len(search) == 4 and search.isdigit():
                print("------------------------------------------------------")
                print(" Albums: ", year[0][1], " Artist: ", year[0][0])
                print("------------------------------------------------------")
                stop += 1
        else:
            if stop == 0:
                print("I don't know this year!")
            else:
                print('')


def search_artist_by_albums(music_complet):
    stop = 0
    while stop == 0:
        search = input("Please give me the name of album: ").upper()
        for album in music_complet:
            if search in album[0][1] and len(search) > 0:
                print("---------------------------------------------")
                print(" Artist: ", album[0][0])
                print("---------------------------------------------")
                stop += 1
        else:
            if stop == 0:
                print("I don't know this album!")
            else:
                print('')


def search_albums_by_letter(music_complet):
    stop = 0
    while stop == 0:
        search = input("Please give me the letter in the album: ").upper()
        for album_letter in music_complet:
            if search in album_letter[0][1][:-1] and len(search) < len(album_letter[0][1][:-1]):
                print("------------------------------------------------------")
                print(" Album: ", album_letter[0][1], "Artist: ", album_letter[0][0])
                print("------------------------------------------------------")
                stop += 1
        else:
            if stop == 0:
                print("I don't know this letter!")
            else:
                print('')


def find_albums_by_genhre(music_complet):
    stop = 0
    while stop == 0:
        search = input("Please give me the genhre the album: ").upper()
        for genre in music_complet:
            if search in genre[1][1] and len(search) >= 3:
                print("------------------------------------------------------")
                print(" Album: ", genre[0][1], "Artist: ", genre[0][0])
                print("------------------------------------------------------")
                stop += 1
        else:
            if stop == 0:
                print("I don't know this letter!")
            else:
                print('')


def how_years_old_all_albums(music_complet):
    all_age = []
    for year in music_complet:      # create list to keep year all position
        all_age += [2017 - int(year[1][0])]
    print("------------------------------------------------------------------------------------------------")
    print('All age albums =', sum(all_age), 'years')
    print("------------------------------------------------------------------------------------------------")


def random_choice_genre():
    plik = open("music.csv") # Open file
    content = plik.readlines() #read lines
    plik.close()
    genre = input("Please input genre: ").upper()
    for i in content:   #loop
        random_genre = random.choice(content).upper()
        random_genre = random_genre.split(" | ")  #remove split |
        genre_random_choice = random_genre[3]
        album = random_genre[1]
        artist = random_genre[0]
        if genre_random_choice == genre:    #argument
            print("---------------------------------------------")
            print(" Album: " + album, " Artist: " + artist)
            print("---------------------------------------------")
            break
    else:
        print('Wrong genre!')


def main():
    menu = True
    print('Welcome in the CoolMusic!')
    while True:
        print_menu()
        menu = input("please insert number: ")
        if menu == '1':
            music_complet = reader_music()
            add_new_album(music_complet)
        elif menu == '2':
            music_complet = reader_music()
            search_by_artist(music_complet)
        elif menu == '3':
            music_complet = reader_music()
            search_by_year(music_complet)
        elif menu == '4':
            music_complet = reader_music()
            search_artist_by_albums(music_complet)
        elif menu == '5':
            music_complet = reader_music()
            search_albums_by_letter(music_complet)
        elif menu == '6':
            music_complet = reader_music()
            find_albums_by_genhre(music_complet)
        elif menu == '7':
            music_complet = reader_music()
            how_years_old_all_albums(music_complet)
        elif menu == '8':
            random_choice_genre()
        elif menu == '9':
            print("test9")
        elif menu == '10':
            print("test10")
        elif menu == '0':
            sys.exit()
        else:
            print("Wrong choice!")

main()
