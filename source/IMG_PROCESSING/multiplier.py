import cv2 as cv
import matplotlib.pyplot as plt
import random
import numpy as np
from source.settings import COLORS

COLOR_MAPS = [cv.COLORMAP_AUTUMN, cv.COLORMAP_BONE, cv.COLORMAP_JET,cv.COLORMAP_WINTER, cv.COLORMAP_RAINBOW,
cv.COLORMAP_OCEAN, cv.COLORMAP_SUMMER, cv.COLORMAP_SPRING, cv.COLORMAP_COOL, cv.COLORMAP_HSV, cv.COLORMAP_PINK,
cv.COLORMAP_HOT, cv.COLORMAP_PARULA, cv.COLORMAP_MAGMA, cv.COLORMAP_INFERNO, cv.COLORMAP_PLASMA,
cv.COLORMAP_VIRIDIS, cv.COLORMAP_CIVIDIS, cv.COLORMAP_TWILIGHT, cv.COLORMAP_TWILIGHT_SHIFTED,
cv.COLORMAP_TURBO, cv.COLORMAP_DEEPGREEN]

#DEFORM -> COLOR -> BLUR -> SHADOW -> NOISE -> ROTATION
        #OUT_imgs []
        #for im in imgs
            #PROCESS
            #APPEND OUT_imgs
        #POP OUT_imgs into imgs
        #...
        #RETURN imgs
def GET_ALL(img, mask,sets=None, solid_color = None, solid_color_random = False,
    color_dif_HSV = [0,0,0], color_dif_n_steps=0, blur = False, blur_random = False,
    color_mix = None, color_mix_random = False, color_mix_n_steps=0,
    shadow = False, shadow_random = False,
    noise = False, noise_random = False, reflection = False,
    rotate = 0, rotate_mirror = False, Flip_X = False, Flip_Y= False,
    deform_X = 0, deform_Y = 0, deform_chunks_X_min = 0, deform_chunks_Y_min = 0, deform_chunks_X_max = 0, deform_chunks_Y_max = 0):

    if sets != None:
        #TODO color_MIX_n_steps
        #COLORS
        solid_color = sets.MUL_col_solid.value
        solid_color_random = sets.MUL_col_solid_random.value
        color_mix = sets.MUL_col_solid_mix.value
        color_mix_random = sets.MUL_col_solid_mix_random.value
        color_dif_HSV = sets.MUL_col_dif_HSV.value
        color_dif_n_steps = sets.MUL_col_dif_steps.value
        #EFFECTS
        blur = sets.MUL_blur.value
        blur_random = sets.MUL_blur_random.value
        shadow = sets.MUL_shadow.value
        shadow_random = sets.MUL_shadow_random.value
        noise = sets.MUL_noise.value
        noise_random = sets.MUL_noise_random.value 
        reflection = sets.MUL_reflection.value
        #ROTATIONS
        rotate =sets.MUL_rot.value
        rotate_mirror = sets.MUL_rot_mirror.value
        Flip_X = sets.MUL_rot_fX.value 
        Flip_Y = sets.MUL_rot_fY.value
        #DEFORM
        deform_X = sets.MUL_def_X.value 
        deform_Y = sets.MUL_def_Y.value 
        deform_chunks_X_min = sets.MUL_def_chunks_X_min.value 
        deform_chunks_Y_min = sets.MUL_def_chunks_Y_min.value 
        deform_chunks_X_max = sets.MUL_def_chunks_X_max.value 
        deform_chunks_Y_max = sets.MUL_def_chunks_Y_max.value



    #TODO FILL :
    #COLOR_dif_hsv
    #COLOR MIX
    #NOISE_RANDOM
    #SHADOW_RANDOM
    IMGS = []
    IMGS.append(img)
    #DEFORMATION
    OUT_imgs = []
    if deform_X > 0:
        OUT_imgs.append(GET_deform(img,maxT=deform_X,chunks_min=deform_chunks_X_min,chunks_max=deform_chunks_X_max))
    if deform_Y > 0:
        OUT_imgs.append(GET_deform(img,maxT=deform_Y,axis=False,chunks_min=deform_chunks_Y_min,chunks_max=deform_chunks_Y_max))
    IMGS.extend(OUT_imgs)
    #COLOR SOLID
    OUT_imgs=[]
    if solid_color != None:
        for i in IMGS:
            OUT_imgs.extend(GET_change_color_solid(img,mask,solid_color))
    IMGS.extend(OUT_imgs)
    #COLOR SOLID RANDOM
    if solid_color_random:
        IMGS.append(GET_change_color_random(img,mask))
    
    #BLUR
    OUT_imgs=[]
    if blur:
        for i in IMGS:
            OUT_imgs.append(GET_blur(i, mask))
    #BLUR RANDOM
    if blur_random:
        for i in IMGS:
            OUT_imgs.append(GET_blur_random(i, mask))
    IMGS.extend(OUT_imgs)
    #REFLECTION
    OUT_imgs = []
    if reflection:
        for i in IMGS:
            OUT_imgs.append(GET_reflection(i,mask,90,10))
    IMGS.extend(OUT_imgs)
    #SHADOW
    OUT_imgs = []
    if shadow:
        for i in IMGS:
            OUT_imgs.append(GET_shadow(i,mask,90,10))
    IMGS.extend(OUT_imgs)
    #SHADOW RANDOM TODO
    #NOISE TODO: COLORED IMAGES SEEM TO GET NO NOISE 
    OUT_imgs = []
    if noise:
        for i in IMGS:
            OUT_imgs.append(GET_noise(i,mask,True))
            OUT_imgs.append(GET_noise(i,mask,False))
    IMGS.extend(OUT_imgs)
    #ROTATE
    OUT_imgs = []
    if rotate > 0:
        for i in IMGS:
            OUT_imgs.extend(GET_rotate(i, mask, rotate,rotate_mirror))
    IMGS.extend(OUT_imgs)
    #FLIP
    OUT_imgs = []
    if Flip_X:
        for i in IMGS:
            OUT_imgs.append(GET_flip_X(i,mask))
    if Flip_Y:
        for i in IMGS:
            OUT_imgs.append(GET_flip_Y(i,mask))
    if Flip_Y and Flip_X:
        for i in IMGS:
            OUT_imgs.append(GET_flip_Y(GET_flip_X(i,mask),mask))
    IMGS.extend(OUT_imgs)
    OUT_imgs=[]
    return IMGS
def GET_deform(img,minT=0, maxT=2,axis = True,chunks_min = 3,chunks_max = 7):
    h,w,_ = img.shape
    out = img.copy()
    img_chunks = []
    #getting CHUNKS
    cMax = 0
    if axis:
        cMax = h
    else: 
        cMax = w
    chunked = 0
    while chunked<cMax:
            c = random.randint(chunks_min,chunks_max)
            chunk = None
            #GETTING INDIVIDUAL CHUNK
            if axis:
                chunk = img[chunked:(chunked + c), :]

            else:
                chunk = img[:, chunked:(chunked + c)]
            img_chunks.append(chunk)
            chunked = chunked + c
    img_chunks.pop()
    #TRANSFORMING img by chunk
    used= 0
    for c in img_chunks:        
        #GETTING transition value
        plus_min = 1
        pmR = random.randint(0,1)
        if pmR == 1:
            plus_min = (-1)
        tv = plus_min * random.randint(minT,maxT)
        #GETTING transition matrix
        tx = 0
        ty = 0
        if axis:
            tx = tv
        else:
            ty = tv
        transitionM = np.array([
        [1, 0, tx], #positive RIGHT, negative LEFT
        [0, 1, ty] #positive DOWN, negative UP
        ], dtype='float32')
        #APPLYING transition to the chunk
        h_c, w_c, _ = c.shape
        t_chunk = cv.warpAffine(c,transitionM, (w_c, h_c))
        #STICHING CHUNK on to the output
        change = 0
        if axis:
            change = h_c
            out[used:(used + change), :] = t_chunk
        else:
            change = w_c
            out[:, used:(used + change)] = t_chunk
        used = used + change
    return  out
def GET_random_poly_pts(minX,maxX,minY,maxY):
    pts = []
    
    points = random.randint(3,9)
    for n in range(0, points):
        x = random.randint(minY,maxY)
        y = random.randint(minX,maxX)
        pts.append([x,y])
        
    pts = np.array(pts, dtype='uint8')
    return pts
def GET_random_mask(img, divisions, mask=''):
                                    #divisions is the number of divisions of the image
                                    #number of sections = 2^divisions
    out = np.zeros(img.shape, dtype='uint8')
    (h,w,_) = img.shape
    h1 = h
    w1 = w
    #SECTION SIZES
    for n in range(1,divisions):
        h1 = (h1/2)
        w1 = (w1/2)
    x = 0
    y = 0
    #GETING SHAPE TO EVERY SECTION
    while y != h:
        x = 0
        while x != w:
            points = GET_random_poly_pts(int(y), int(y+h1),int(x),int(x+w1))
            cv.fillPoly(out, pts=np.int32([points]), color = (255,255,255))
            x = x + w1
        y = y + h1
    if mask != '':
        #GETTING MASK BITWISE
        thresh = 254
        grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        im_bw_inv = cv.bitwise_not(im_bw)
        #GETTING BACKGROUND 
        bg = cv.bitwise_and(mask, mask, mask = im_bw_inv)
        fg = cv.bitwise_and(out, out, mask = im_bw)

        out = cv.add(bg,fg)
        return out
    else:
        return out
def GET_shadow(img, mask, opacity_top, opacity_bottom):
    (h,w,_) = img.shape
    out_img = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
    #GET GRADIENT
    g_bot = (255*opacity_top)/100
    g_top = (255*opacity_bottom)/100
    g_y = np.linspace(g_bot,g_top,h,dtype='uint8')
    g_x = np.linspace(1,1,w,dtype='uint8')
    grad = np.outer(g_y,g_x)
    #ADD GRADIENT
    out_img[:,:,3] = grad
    #REDUCE BGRA to BGR
    out = np.zeros(img.shape, dtype='uint8')

    gray_grad = cv.cvtColor(grad,cv.COLOR_GRAY2BGR)
    for hh in range(0,h - 1):
        for ww in range(0, w-1):
            a = out_img[hh][ww][3]/255
            B = out_img[hh][ww][0]/255
            G = out_img[hh][ww][1]/255
            R = out_img[hh][ww][2]/255
            bgB = gray_grad[hh][ww][0]/255
            bgG = gray_grad[hh][ww][1]/255
            bgR = gray_grad[hh][ww][2]/255
            out[hh][ww][0] = (((1-a) * bgB) + (a*B)) * 255#B 
            out[hh][ww][1] = (((1-a) * bgG) + (a*G)) * 255 #G
            out[hh][ww][2] = (((1-a) * bgR) + (a*R)) * 255 #R
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    #CREATING SOLID COLOR PICTURE
    #GETTING BACKGROUND
    fg = cv.bitwise_and(out, out, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    
    return out
def GET_reflection(img, mask, opacity_top, opacity_bottom):
    (h,w,_) = img.shape
    out_img = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
    #GET GRADIENT
    g_bot = (255*opacity_top)/100
    g_top = (255*opacity_bottom)/100
    g_y = np.linspace(g_bot,g_top,h,dtype='uint8')
    g_x = np.linspace(1,1,w,dtype='uint8')
    grad = np.outer(g_y,g_x)
    #ADD GRADIENT
    out_img[:,:,3] = grad
    #REDUCE BGRA to BGR
    out = np.zeros(img.shape, dtype='uint8')

    gray_grad = cv.cvtColor(grad,cv.COLOR_GRAY2BGR)
    for hh in range(0,h - 1):
        for ww in range(0, w-1):
            a = out_img[hh][ww][3]/255
            B = out_img[hh][ww][0]/255
            G = out_img[hh][ww][1]/255
            R = out_img[hh][ww][2]/255
            bgB = gray_grad[hh][ww][0]/255
            bgG = gray_grad[hh][ww][1]/255
            bgR = gray_grad[hh][ww][2]/255
            out[hh][ww][0] = (((1-a) * B) + (a*bgB)) * 255#B 
            out[hh][ww][1] = (((1-a) * G) + (a*bgG)) * 255 #G
            out[hh][ww][2] = (((1-a) * R) + (a*bgR)) * 255 #R
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    #CREATING SOLID COLOR PICTURE
    #GETTING BACKGROUND
    fg = cv.bitwise_and(out, out, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    
    return out
def GET_rotate(img, mask, angle, mirror):
    out = []
    (h, w, _ ) =img.shape
    #CENTER POINTS
    cX, cY = w/2, h/2
    if mirror == True:
        for a in range(360 - angle, 359):
            #ROTATION MATRIX
            rotationM = cv.getRotationMatrix2D((cX, cY), a, 1.0)
            #sin & cos ABSOLUTE VALUES
            cosRotationM = np.abs(rotationM[0][0])
            sinRotationM = np.abs(rotationM[0][1])
            #NEW DIMENSIONS
            nW = int((h*sinRotationM) + (w*cosRotationM))
            nH = int((h*cosRotationM) + (w*sinRotationM))
            #UPDATE ROTATION MATRIX
            rotationM[0][2] += (nW/2) - cX
            rotationM[1][2] += (nH/2) - cY
            #rotate image
            rot_img = cv.warpAffine(img, rotationM, (nW,nH))
            out.append(rot_img)
    for a in range(1, angle):
        #ROTATION MATRIX
        rotationM = cv.getRotationMatrix2D((cX, cY), a, 1.0)
        #sin & cos ABSOLUTE VALUES
        cosRotationM = np.abs(rotationM[0][0])
        sinRotationM = np.abs(rotationM[0][1])
        #NEW DIMENSIONS
        nW = int((h*sinRotationM) + (w*cosRotationM))
        nH = int((h*cosRotationM) + (w*sinRotationM))
        #UPDATE ROTATION MATRIX
        rotationM[0][2] += (nW/2) - cX
        rotationM[1][2] += (nH/2) - cY
        #rotate image
        rot_img = cv.warpAffine(img, rotationM, (nW,nH))
        out.append(rot_img)


    return out
def GET_flip_X(img, mask):
    return cv.flip(img,0)
def GET_flip_Y(img, mask):
    return cv.flip(img,1)
def GET_change_color_solid(img, mask, colors):#BGR
    out = []
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    #CREATING SOLID COLOR PICTURE
    col_pic = np.zeros(mask.shape, dtype='uint8')
    for col in colors:
        (_, b,g,r) = col
        col_pic[:] = [b,g,r] 
        #GETTING BACKGROUND
        fg = cv.bitwise_and(col_pic, col_pic, mask = im_bw)
        #BLENDING PICTURES
        toSave = cv.add(bg,fg)
        out.append(toSave)
    return out
def GET_change_color_random(img, mask):
    out = img.copy()
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(out, out, mask = im_bw_inv)
    #CREATING COLOR PICTURE
    col_pic = np.zeros(mask.shape, dtype='uint8')
    (h,w,_) = out.shape
    used_h = 0
    while h>used_h:
        y = random.randint(1,h-used_h)
        used_w = 0
        while w>used_w:
            x = random.randint(1,w-used_w)
            #getting color
            color = random.randint(1,len(COLORS))
            #croping section
            paint_section = out[used_h:used_h+y, used_w:used_w+x]
            #coloring section
            (_, b,g,r) = COLORS[color]
            paint_section[:] = [b,g,r]
            #pasting section into image
            col_pic[used_h:used_h+y, used_w:used_w+x] = paint_section
            used_w = used_w + x
        used_h = used_h + y
    #GETTING BACKGROUND
    fg = cv.bitwise_and(col_pic, col_pic, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_change_color_dif(img, mask, dif):#HSV VALUES
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
    out = img.copy()
    blur_img = cv.blur(out, (3,3))
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND AND FOREGROUND
    bg = cv.bitwise_and(out, out, mask = im_bw_inv)
    fg = cv.bitwise_and(blur_img, blur_img, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_blur_random(img, mask):
    blur_img = img.copy()
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
            blur_section = blur_img[used_h:used_h+y, used_w:used_w+x]
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
def GET_color_mix(img, mask, colorMaps):
    out = []
    img_gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    for col in colorMaps: 
        img_col = cv.applyColorMap(grey, col)
        #GETTING FOREGROUND
        fg = cv.bitwise_and(img_col, img_col, mask = im_bw)
        #BLENDING PICTURES
        toSave = cv.add(bg,fg)
        out.append(toSave)
   
    return out #list of images
def GET_color_mix_random(img, mask):
    img_gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    #CREATING COLOR PICTURE
    col_pic = np.zeros(mask.shape, dtype='uint8')
    (h,w,_) = img.shape
    used_h = 0
    while h>used_h:
        y = random.randint(1,h-used_h)
        used_w = 0
        while w>used_w:
            x = random.randint(1,w-used_w)
            #getting blur strength for the section
            color = random.randint(0,len(COLOR_MAPS)-1)
            #croping section
            paint_section = img_gray[used_h:used_h+y, used_w:used_w+x]
            #coloring section
            paint_section = cv.applyColorMap(paint_section, COLOR_MAPS[color])
            #pasting section into image
            col_pic[used_h:used_h+y, used_w:used_w+x] = paint_section
            used_w = used_w + x
        used_h = used_h + y
    #GETTING BACKGROUND
    fg = cv.bitwise_and(col_pic, col_pic, mask = im_bw)
    #BLENDING PICTURES
    out = cv.add(bg,fg)
    return out
def GET_noise(img, mask, whites = False):
    mean = 2
    var = 5
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, (img.shape[0],img.shape[1])) 
    noise = np.zeros(img.shape, np.float32)
    if whites:
        noise[:, :, 0] = img[:, :, 0] + gaussian
        noise[:, :, 1] = img[:, :, 1] + gaussian
        noise[:, :, 2] = img[:, :, 2] + gaussian
    else:
        noise[:, :, 0] = img[:, :, 0] - gaussian
        noise[:, :, 1] = img[:, :, 1] - gaussian
        noise[:, :, 2] = img[:, :, 2] - gaussian
    noise = noise.astype(np.uint8)
    #GETTING MASK BITWISE
    thresh = 254
    grey =cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    (_, im_bw) = cv.threshold(grey, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    im_bw_inv = cv.bitwise_not(im_bw)
    #GETTING BACKGROUND 
    bg = cv.bitwise_and(img, img, mask = im_bw_inv)
    fg = cv.bitwise_and(noise, noise, mask = im_bw)

    out = cv.add(bg,fg.astype('uint8'))
    return out
def GET_quant(img,clusters, k=2):
    Z = img.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)
                #( type, max_iter = 10 , epsilon = 1.0 )
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,label,center=cv.kmeans(Z,k,None,criteria,clusters,cv.KMEANS_RANDOM_CENTERS)
    #CONVERTING TO uint8 img
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return res2
