
class __Params__:
    target_region_pixel_tlbr = [800, 500, 1200, 1421]
    section_layout = [2, 3]
    section_shape = [(target_region_pixel_tlbr[2] - target_region_pixel_tlbr[0])/section_layout[0],
                     (target_region_pixel_tlbr[3] - target_region_pixel_tlbr[1])/section_layout[1],]


DATASET = {'path': 'F:/work/dataset/hyundai/sample_pcd'}

# TODO: TLBR -> LTRB (x1y1x2y2)
PLANE_ESTIM = {
    'camera_param': {'fx': 100, 'fy': 100, 'cx': 960, 'cy': 600}
    'target_region_pixel_tlbr': __Params__.target_region_pixel_tlbr,
    'section_layout': __Params__.section_layout,    # target region is divided by layout
    'section_shape': __Params__.section_shape,      # section size in pixels
    'default_plane_normal': [0, 0, 1],
    'default_plane_height': 1.0,
}

HEIGHT_ESTIM = {
    'camera_param': {'fx': 100, 'fy': 100, 'cx': 960, 'cy': 600}
}


