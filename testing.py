# import cv2
# import function.online_ops as a
import json
# ----------------------------------------------------------------------------
# vid=cv2.VideoCapture(0)


# if vid.isOpened()==False:
#     print("Error reading video file")
 
# frame_width=int(vid.get(3))
# frame_height=int(vid.get(3))
# size=(frame_width,frame_height)

# result=cv2.VideoWriter("video.avi",cv2.VideoWriter_fourcc(*"XVID"),10,size)

# while True:
#     ret,frame=vid.read()
#     if ret==True:
#         result.write(frame)
        
#         cv2.imshow("Frame",frame)

#         k=cv2.waitKey(1)
#         if k%256==27:
#             print("Escape hit, closing...")
#             break

#     else:
#         break
# vid.release()
# result.release()
# cv2.destroyAllWindows()
# print("The video was successfully saved!")

# ----------------------------------------------------------------------------------------
# vid=cv2.VideoCapture(0)
# cv2.namedWindow("test")
# i=0
# while vid.isOpened():
#     ret,frame=vid.read()
#     if ret==False:
#         # prevents from infinite loop in case if video ends
#         break
#     cv2.imshow("frame",frame)
#     k=cv2.waitKey(1)
#     if k%256==27:
        #ESC
#         print("Escape hit, closing...")
#         break
#     elif k%256==32:
        #SPACE
#         img_name="photo{}.png".format(i)
#         cv2.imwrite(img_name,frame)
#         print("{} written!".format(img_name))
#         i+=1
# vid.release()
# cv2.destroyAllWindows()
# -------------------------------------------------------------------------------------
{
    "akash": "akashpatel1098@gmail.com",
    "sky": "onlyskymovie2020@gmail.com",
    "patel": "patelakash1098@gmail.com"
}
email={'akash': 'akashpatel1098@gmail.com', 'sky': 'onlyskymovie2020@gmail.com', 'patel': 'patelakash1098@gmail.com',"sau":"saurabh@gamil.com"}

# with open("emails.json","r")  as f:
#     old_dic=dict(json.loads(f.read()))
#     print(old_dic)
# old_dic.
with open("emails.json","w")  as f:
    json.dump(email,f,indent=4)
# Akash chutiya hai