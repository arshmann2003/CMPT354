import sqlite3
conn = sqlite3.connect('chinook.db')

myFavArtist = input("Enter your new favorite artist's name: ")

print("Opened database successfully \n")

with conn:

    cur = conn.cursor()

    myQuery = "INSERT INTO artists(name) VALUES(:myArtist)"
    try:
        cur.execute(myQuery,{"myArtist":myFavArtist})

    except sqlite3.IntegrityError:
        print("ERROR: There was a problem adding your artist to the dabase!\n")      
  

if conn:
    conn.commit()
    print("Committed Changes!\n")
    conn.close()
    print("Closed database successfully")
