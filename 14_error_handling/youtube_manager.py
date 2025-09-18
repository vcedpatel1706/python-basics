import json # we will use only two method of json 'dump' and 'load'

def load_data():
    try:
        with open('youtube.txt','r') as file: # what is need of r ?
            test=json.load(file)
            # print(type(test))  # it is the list of json
            return test
            # what it do ? automatically ectract data from file and load it and convert it to json
    except FileNotFoundError:
        return []
    
# it is the method we made to save the data, such that every time(when we add/update) we don't need to hussle.
def save_data_helper(videos): # means tu file khol and tema lakh
    with open('youtube.txt','w') as file:
        json.dump(videos,file) # what to write and where to write

def list_all_videos(videos):
    # we saw in line -7 that all data stored in youtube.txt is in form of list.so we can use video as iterable and print video directly(we can use actually, don't give problem but....)
    # but in future we are not ble to access the entries of youtube.txt. so we need indexing with file.
    # list has inbuilt indexing but here is json list.
    # that's why we cant use videos as iterable directly.

    # for vid in videos:  
    #     print(vid)

    # here we made file so we can see and by printing also determine that at index 1 /0/2 which entry is but if we want to disply the no. and file to user thrn it is not capable.
    # hence we used enumerated
    # print(len(videos))
    # print(videos[1])

    print('\n')
    print('*'*70)

    for index,vid in enumerate(videos,start=1):
        print(f'{index}. {vid['name']}, Duretion :{vid['time']}')

    print('*'*70)


def add_video(videos):
    name=input('enter video name of video: ')
    time=input('enter duration of video : ')

    videos.append({'name':name , 'time': time})
    save_data_helper(videos)

    print('video added successfully')



def update_video(videos):
    list_all_videos(videos)
    update_index=int(input('enter the index at which you want to update video : '))

    if 1<=update_index<=len(videos):
        name=input('enter the new name of video : ')
        time=input('enter new time of video : ')
        videos[update_index-1]= {'name':name,'time':time}

        save_data_helper(videos)
        print('video updated successfully')


    else:
        print('invalid index selected')
def delete_video(videos):
    list_all_videos(videos)
    delete_index=int(input('enter the index at which you want to delete entry : '))
    if 1<=delete_index<=len(videos):
        del videos[delete_index-1]  # make changes in memory

        save_data_helper(videos)
        print('video deleted successfully')


    else:
        print('invalid index selected')



# it is important to make a start point of all code form there all further applications will load.
# withou this main() method code was ok but to follow industry standards we do so.. 

def main():  
    videos=load_data()
    while True:
        print('\n youtube manager | choose an option')
        print('1 : list all youtube videos')
        print('2 : add a youtube video')
        print('3 : update a youtube video details')
        print('4 : delete a youtube video')
        print('5: exit the app')

        choice=int(input('enter your choice : '))
        # print(videos)

        match choice:
            
            case 1:
                list_all_videos(videos) 
            case 2:
                add_video(videos) 
            case 3:
                update_video(videos) 
            case 4:
                delete_video(videos) 
            case 5:
                break 
            case _:
                print('invalid choice')

if __name__=='__main__':  # it's called dunder(__) double underscor
    main()