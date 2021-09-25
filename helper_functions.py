def get_centred_x_coords(rect, surf): # Centers an object on a surface in the x-axis
    x =  surf.get_width() / 2 - rect.width / 2
    rect.x = x
    return rect

def get_centred_y_coords(rect, surf): # Centers an object on a surface in the y-axis
    y =  surf.get_height() / 2 - rect.height / 2
    rect.y = y
    return rect

def get_centred_coords(rect, surf): # Centers an object on a surface
    rect = get_centred_x_coords(rect, surf)
    rect = get_centred_y_coords(rect, surf)
    return rect