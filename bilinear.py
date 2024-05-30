def bilinear_interpolation(input_image, new_width, new_height):
    old_height, old_width = len(input_image), len(input_image[0])

    output_image = [[0 for _ in range(new_width)] for _ in range(new_height)]
    #create le array fadia
    x_scale = (old_width - 1) / (new_width - 1)
    y_scale = (old_height - 1) / (new_height - 1)
    #el scale bta3i
    for new_y in range(new_height):
        for new_x in range(new_width):
            #b3ml nestep loop 3la newh,neww
            x = new_x * x_scale
            y = new_y * y_scale
            x1 = int(x)
            y1 = int(y)
            x2 = min(x1 + 1, old_width - 1)
            y2 = min(y1 + 1, old_height - 1)
            dx = x - x1
            dy = y - y1
            pixel_value = (
                input_image[y1][x1] * (1 - dx) * (1 - dy) +
                input_image[y1][x2] * dx * (1 - dy) +
                input_image[y2][x1] * (1 - dx) * dy +
                input_image[y2][x2] * dx * dy
            )
            output_image[new_y][new_x] = int(pixel_value)
    return output_image
