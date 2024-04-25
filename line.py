# import cv2
# import numpy as np

# def red_detect(img):
#     #青色検出
#     RED_MIN = np.array([90, 200, 80])
#     RED_MAX = np.array([150,255,255])
#     hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv_img, RED_MIN, RED_MAX)
#     return mask

# def get_center(binary_img):
#     nlabels, labels, stats, center = cv2.connectedComponentsWithStats(binary_img)
#     if len(stats) > 1:
#         max_index = np.argmax(stats[1:,4]) + 1
#         center_x = int(center[max_index][0])
#         center_y = int(center[max_index][1])
#         return (center_x, center_y)
#     return None
# #画面に点をマッピングをする
# def drawObit(tracks, new_point, frame):
#     if new_point is not None:
#         tracks.append(new_point)
#         for track in tracks:
#             cv2.circle(frame, track, 5, (0, 255, 0), thickness=-1)

# def main():
#     #デバイスの指定
#     cap = cv2.VideoCapture(0)
#     #画面の幅
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1980)
#     #画面の高さ
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#     center_tracks = []
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if ret:
#             mask = red_detect(frame)
#             center = get_center(mask)
#             drawObit(center_tracks, center, frame)
#             cv2.imshow("draw_star", frame)
#             cv2.imshow("mask", mask)
#             if cv2.waitKey(25) & 0xFF == ord("q"):
#                 break
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
import cv2
import numpy as np

def red_detect(img):
    RED_MIN = np.array([90, 200, 80])
    RED_MAX = np.array([150,255,255])
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, RED_MIN, RED_MAX)
    return mask

def get_center(binary_img):
    nlabels, labels, stats, center = cv2.connectedComponentsWithStats(binary_img)
    if len(stats) > 1:
        max_index = np.argmax(stats[1:,4]) + 1
        center_x = int(center[max_index][0])
        center_y = int(center[max_index][1])
        return (center_x, center_y)
    return None

def drawObit(tracks, new_point, frame, max_points=50):
    if new_point is not None:
        tracks.append(new_point)
        if len(tracks) > max_points:
            tracks.pop(0)
        for track in tracks:
            cv2.circle(frame, track, 5, (0, 255, 0), thickness=-1)

def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1980)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    center_tracks = []
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            mask = red_detect(frame)
            center = get_center(mask)
            drawObit(center_tracks, center, frame)
            cv2.imshow("draw_star", frame)
            cv2.imshow("mask", mask)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
