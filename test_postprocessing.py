import numpy as np
import vigra
from elf.segmentation.workflows import simple_multicut_workflow


def dummy_inputs(shape=(64, 64, 64)):
    boundaries = np.random.rand(*shape).astype('float32')
    foreground = np.random.rand(*shape).astype('float32')
    return boundaries, foreground


def test_postprocessing():
    boundaries, foreground = dummy_inputs()

    seg = simple_multicut_workflow(boundaries,
                                   use_2dws=False,
                                   multicut_solver='kernighan-lin')
    assert seg.shape == boundaries.shape

    mean_fg_prob = vigra.analysis.extractRegionFeatures(foreground, seg.astype('uint32'), features=['mean'])['mean']
    bg_ids = np.where(mean_fg_prob < 0.5)[0]

    seg[np.isin(seg, bg_ids)] == 0
    assert seg.shape == boundaries.shape


if __name__ == '__main__':
    test_postprocessing()
