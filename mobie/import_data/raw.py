from .util import downscale


def import_raw_volume(in_path, in_key, out_path,
                      resolution, scale_factors, chunks,
                      tmp_folder, target, max_jobs,
                      block_shape=None):
    """ Import raw data to mobie format.

    Arguments:
        in_path [str] - input data to be added.
        in_key [str] - key of the input data to be added.
        out_path [str] - where to add the data.
        resolution [list[float]] - resolution in micrometer
        scale_factors [list[list[int]]] - scale factors used for down-sampling the data
        chunks [tuple[int]] - chunks of the data to be added
        tmp_folder [str] - folder for temporary files (default: None)
        target [str] - computation target (default: 'local')
        max_jobs [int] - number of jobs (default: number of cores)
        block_shape [tuple[int]] - block shape used for computation.
            By default, same as chunks. (default:None)
    """
    downscale(in_path, in_key, out_path,
              resolution, scale_factors, chunks,
              tmp_folder, target, max_jobs, block_shape,
              library='skimage')
