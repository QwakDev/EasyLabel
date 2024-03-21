from source.settings import sets, COLORS
import tkinter as tk
#POP UPS
_GEOMETRY = "750x1200"
#SETTINGS
def SHOW_IMG_MUL_color(window,sets):
    popup= tk.Toplevel(window)
    popup.title('COLORS')
    popup.geometry(_GEOMETRY)

    sets.MUL_col_solid.getWidget(popup)
    sets.MUL_col_solid_random.getWidget(popup)
    sets.MUL_col_solid_mix.getWidget(popup)
    sets.MUL_col_solid_mix_random.getWidget(popup)
    sets.MUL_col_dif_HSV.getWidget(popup)
    sets.MUL_col_dif_steps.getWidget(popup)
    return
def SHOW_IMG_MUL_effects(window,sets):
    popup= tk.Toplevel(window)
    popup.title('EFFECTS')
    popup.geometry(_GEOMETRY)

    sets.MUL_blur.getWidget(popup)
    sets.MUL_shadow.getWidget(popup)
    sets.MUL_blur_random.getWidget(popup)
    sets.MUL_shadow_random.getWidget(popup)
    sets.MUL_noise.getWidget(popup)
    sets.MUL_noise_random.getWidget(popup)
    sets.MUL_reflection.getWidget(popup)
    return
def SHOW_IMG_MUL_rotate(window,sets):
    popup= tk.Toplevel(window)
    popup.title('ROTATE')
    popup.geometry(_GEOMETRY)

    sets.MUL_rot.getWidget(popup)
    sets.MUL_rot_mirror.getWidget(popup)
    sets.MUL_rot_fX.getWidget(popup)
    sets.MUL_rot_fY.getWidget(popup)
    return
def SHOW_IMG_MUL_deform(window,sets):
    popup= tk.Toplevel(window)
    popup.title('DEFORM')
    popup.geometry(_GEOMETRY)
    #DEFORMATION
    sets.MUL_def_Y.getWidget(popup)
    sets.MUL_def_X.getWidget(popup)
    sets.MUL_def_chunks_Y_min.getWidget(popup)
    sets.MUL_def_chunks_Y_max.getWidget(popup)
    sets.MUL_def_chunks_X_min.getWidget(popup)
    sets.MUL_def_chunks_X_max.getWidget(popup)
    return
def SHOW_IMG_MUL_slices(window,sets):
    popup= tk.Toplevel(window)
    popup.title('SLICES')
    popup.geometry(_GEOMETRY)

    sets.MUL_section_slice_x.getWidget(popup)
    sets.MUL_section_slice_y.getWidget(popup)
    return