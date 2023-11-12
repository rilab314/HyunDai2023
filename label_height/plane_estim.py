
class PlaneEstim:
    def __init__(self, cfg):
        self.sections = []
        pass

    def fit_section_planes(self, pcd):
        """
        :param pcd: (N, 3)
        :return:
        """
        pcd = self.compute_pixel(pcd)
        section_pcd = self.split_sections(pcd)
        planes = self.estimate_planes(section_pcd)
        planes = self.spatial_average(planes)
        planes = self.temporal_average(planes)

    def compute_pixel(self, pcd):
        """
        :param pcd: (N, 3) [x, y, z]
        :return: (N, 5) [x, y, z, u, v]
        """
        pass

    def split_sections(self, pcd):
        """
        :param pcd: (N, 5) [x, y, z, u, v]
        :return: [[(N0,5), (N1,5), ...],   : first rows of sections
                  [(Ni,5), (Ni+1,5), ...], : second rows of sections
                 ]
        """
        pass

    def estimate_planes(self, section_pcd):
        """
        :param section_pcd: [[(N0,5), (N1,5), ...],   : first rows of sections
                             [(Ni,5), (Ni+1,5), ...], : second rows of sections
                            ]
        :return: (rows, cols, 4) [nx, ny, nz, h], nx*x + ny*y + nz*z + h = 0
        """

        """
        algorithm:
        n = zeros(3)
        for 20
            randomly sample 3 points
            n += cross product(p1-p2, p1-p3)
        n.normalize()
        
        dots = []
        for pi
            pi.normalize()
            di = dot product(pi, n)
            dots.push_back(di)
        
        remove 10% furthest points from n
        compute normal with remaining points
        iterate until 50% points remain
        """
