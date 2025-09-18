import sqlite3

conn=sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute('SELECT * FROM videos')

    for row in cursor.fetchall():
        print(row)

    
def add_video(name,time):
    cursor.execute('INSERT INTO videos(name,time) VALUES (?,?)',(name,time))

    conn.commit()

def update_video(update_id,new_name,new_time):
    cursor.execute('UPDATE videos SET name=?,time=? WHERE id =?',(new_name,update_id,new_time,))

    conn.commit()

def delete_video(delete_id):
    cursor.execute('DELETE FROM videos WHERE id=?',(delete_id,))
    # here comma is required for single parameter
 
    conn.commit()

def main():
    
    while True:
        
        print('\n youtube manager with database | choose an option')
        print('1 : list all youtube videos')
        print('2 : add a youtube video')
        print('3 : update a youtube video details')
        print('4 : delete a youtube video')
        print('5: exit the app')

        choice=int(input('enter your choice : '))
        

        match choice: # it can be also done by if else if 
            
            case 1:
                list_all_videos() 
            case 2:
                name=input('enter video name of video: ')
                time=input('enter duration of video : ')

                add_video(name,time) 
            case 3:
                update_id=int(input('enter the updated id'))
                name=input('enter video name of video: ')
                time=input('enter duration of video : ')

                update_video(update_id,name,time) 
            case 4:
                delete_id=int(input('enter the updated id'))
                delete_video(delete_id) 
            case 5:
                break 
            case _:
                print('invalid choice')

    conn.close()

if __name__=='__main__':
    main()
