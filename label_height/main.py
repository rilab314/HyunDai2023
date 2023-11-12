import config as cfg
from dataset import Dataset
from plane_estim import PlaneEstim
from height_estim import HeightEstim


def main():
    dataset = Dataset(cfg.DATASET)
    num_frames = dataset.num_frame()
    plane_estim = PlaneEstim(cfg.PLANE_ESTIM)
    height_estim = HeightEstim()

    for idx in range(num_frames):
        image, pcd, label = dataset.get_frame(idx)
        planes = plane_estim.fit_section_planes(pcd)
        height = height_estim.estimate(pcd, label, planes)
        # label = interactive_confirm(image, label, height)
        dataset.update_label(label)


if __name__ == '__main__':
    main()
