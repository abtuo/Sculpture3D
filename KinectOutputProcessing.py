def depth_array_to_matrix(depth_arr, width=512, height=424):
    depth_matrix = [[depth_arr[i * width + j] for j in range(width)] for i in range(height)]
    return depth_matrix


def color_array_to_rgb_matrix(color_arr, width=1920, height=1080):
    color_matrix = []
    for h in range(height):
        color_matrix += [[]]
        for w in range(width):
            color_matrix[h] += [[color_arr[(h*width + w) * 4],
                                color_arr[(h*width + w) * 4 + 1],
                                color_arr[(h*width + w) * 4 + 2]]]
    return color_matrix


def value_normalization(v, v_min=500, v_max=800):
    if v < v_min:
        return 0
    elif v > v_max:
        return 255
    else:
        return 255 * (v-v_min) / (v_max - v_min)
