import cv2
import glob as gb

def Split_frames(Path_videos,Path_images,Number_Frame):
    videos=gb.glob(Path_videos+'/*.mp4')
    i=0
    for video in videos :
        cap = cv2.VideoCapture(video)
        j=0
        while cap.isOpened() :
            success, img = cap.read()
            if success == False :
                break
            if i % Number_Frame == 0 :
                cv2.imwrite(f'{Path_images}/{i}_{video[-12:-4]}.jpg', img)
            cv2.imshow("Tracking", img)
            i = i + 1
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        j = j + 1
        
# Split_frames(Path_videos='Video',Path_images='Player',Number_Frame=30)
Split_frames(Path_videos='Video',Path_images='Ball',Number_Frame=10)