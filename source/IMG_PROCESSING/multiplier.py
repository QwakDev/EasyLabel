import cv2 as cv
import matplotlib.pyplot as plt
import random
# rotate
# change color
#kick
# add shadow

#change color solid
#change color mix
def MAIN_MAIN(path_temp, solid_color = None, color_dif_HSV = (0,0,0), color_dif_n_steps=0,
     blur = 0, blur_random = False,
     color_mix = None, color_mix_random = False, color_mix_n_steps=0,
     shadow = False, shadow_doted = False, random_shadow = False,
     rotate_X = 0, rotate_Y = 0, rotate_mirror_X = False, rotate_mirror_Y = False, Flip_X = False, Flip_Y= False,
     kick_TOP = 0, kick_BOTTOM = 0, kick_LEFT = 0 , kick_RIGHT=0,
     kick_mirror_TOP = False, kick_mirror_BOTTOM = False, kick_mirror_RIGHT = False, kick_mirror_LEFT = False,
     deform_X = 0, deform_Y = 0, deform_chunks_X_min = 0, deform_chunks_Y_min = 0, deform_chunks_X_max = 0, deform_chunks_Y_max = 0):

     return
def GET_ChangeColorSolid(img, mask, toColor):#BGR
    #CREATING SOLID COLOR PICTURE
    col_pic = np.zeros(mask.shape, dtype='uint8')
    col_pic[:] = toColor
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND AND FOREGROUND
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    fg = cv.bitwise_and(col_pic, col_pic, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_ChangeColorDif(img, mask, dif):#HSV VALUES
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hsv_img = hsv_img + dif
    #CREATING COLOR PICTURE
    col_img = cv.cvtColor(hsv_img.astype(np.uint8), cv.COLOR_HSV2BGR)
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND AND FOREGROUND
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    fg = cv.bitwise_and(col_img, col_img, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_blur(img, mask):
    blur_img = cv.blur(img, (3,3))
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND AND FOREGROUND
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    fg = cv.bitwise_and(blur_img, blur_img, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_blur_random(img, mask):
    blur_img = img
    (h,w,_) = img.shape

    used_h = 0
    while h>used_h:
        y = random.randint(1,h-used_h)
        used_w = 0
        while w>used_w:
            x = random.randint(1,w-used_w)
            #getting blur strength for the section
            blur_strength = random.randint(1,5)
            #croping section
            blur_section = img[used_h:used_h+y, used_w:used_w+x]
            #bluring
            blur_section = cv.blur(blur_section, (blur_strength,blur_strength))
            #pasting section into image
            blur_img[used_h:used_h+y, used_w:used_w+x] = blur_section
            used_w = used_w + x
        used_h = used_h + y
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND AND FOREGROUND
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    fg = cv.bitwise_and(blur_img, blur_img, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out

#plt.imshow(lab_img)