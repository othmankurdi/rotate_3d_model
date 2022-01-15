from setttings import params
from _3d_models_managers.rotate_3d_model_from_s3 import Rotate3DModel

if __name__ == '__main__':
    rotate_3d_model = Rotate3DModel(local_file_path=params.LOCAL_FILE_PATH,
                                    local_rotated_file_path=params.LOCAL_ROTATED_FILE_PATH,
                                    bucket_name=params.BUCKET_NAME,
                                    file_name=params.FILE_NAME,
                                    xyz=params.XYZ,
                                    rotate_degree=params.ROTATE_DEGREE)
    rotate_3d_model.rotate_3d_model()
