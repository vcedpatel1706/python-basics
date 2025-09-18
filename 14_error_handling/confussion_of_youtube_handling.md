**************************Question*******************************
Suppose that currently in 'youtube.txt' there are three videos.
I delete second video by delete_video().when i print all available videos using list_all_videos() then it appears two videos, but numbering of those is 1 and 2, not 1 and 3 ! how it done? how it self rectified that 2nd video is deleted so number of 3rd video is now #2.

****************************Answer*******************************

--> it is the magic of list_all_videos() method.
✅ What's Happening:
        - enumerate() loops over the list of videos.
        - start=1 means it starts numbering from 1.
        - The index is generated fresh every time — based on the  current order in the list.

✅ Why it works perfectly:
        - You are not storing video number inside the file.
        - You're just storing a list of videos.
        - Their positions (indexes) in the list decide the number when you display them.
        - Deleting an item shifts everything behind it automatically.



**************************Question*******************************
where we used list handling and file handlig in this code ?
****************************Answer*******************************
in the code we are jandling the list named videos.
and handling files by json.dump(file) and json.load(file)