import cv2
import function.online_ops as a

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


