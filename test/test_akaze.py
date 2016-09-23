from cv2img import CV2Img, Rect
from config import IMG_PATH

import numpy as np
import cv2

def filter_matches(kp1, kp2, matches, ratio = 0.75):
    mkp1, mkp2= [], []
    new_matches = []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            new_matches.append(m)

            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )

    p1 = np.float32([kp.pt for kp in mkp1])
    p2 = np.float32([kp.pt for kp in mkp2])
    kp_pairs = zip(mkp1, mkp2)
    return p1, p2, kp_pairs, new_matches

img1 = CV2Img()
img1.load_file(IMG_PATH("facebook_screen.png"))

img2 = CV2Img()
img2.load_file(IMG_PATH("facebook_password.png"))

detector = cv2.AKAZE_create()
norm = cv2.NORM_HAMMING
matcher = cv2.BFMatcher(norm)
#detector = cv2.xfeatures2d.SIFT_create(400)
#matcher = cv2.BFMatcher()

kp1, des1 = detector.detectAndCompute(img1.source, None)
kp2, des2 = detector.detectAndCompute(img2.source, None)
print('img1 - %d features, img2 - %d features' % (len(kp1), len(kp2)))

raw_matches = matcher.knnMatch(des1, trainDescriptors=des2, k=2)
p1, p2, kp_paris, new_matches = filter_matches(kp1, kp2, raw_matches)

if len(p1) >= 4:
    H, status = cv2.findHomography(p1, p2, cv2.RANSAC, 5.0)
    print("{}/{} inliers/matched".format(np.sum(status), len(status)))
else:
    H, status = None, None
    print("{} matches found, not enough for homography estimation".format(len(p1)))

h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]
obj_corners = np.float32([[0, 0], [w1, 0], [w1, h1], [0, h1]])
obj_corners = obj_corners.reshape(1, -1, 2)

scene_corners = cv2.perspectiveTransform(obj_corners, H)
scene_corners = scene_corners.reshape(-1, 2)

print(scene_corners)
result = Rect(int(round(scene_corners[3][0])),
              int(round(scene_corners[3][1])),
              int(round(scene_corners[1][0])),
              int(round(scene_corners[1][1])))

img1.draw_result_range(result)
img1.show()

"""
img3 = cv2.drawMatchesKnn(img1.source, kp1, img2.source, kp2, new_matches, None, flags=2)
result = CV2Img(img3)
result.show()
"""
