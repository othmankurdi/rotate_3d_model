from _3d_models_managers.managers.rotate_manager import RotateManager
from _3d_models_managers.managers.show_preview_manager import ShowPreviewManager
from aws_manager.aws_manager import AWSManager


class Rotate3DModel:

    def __init__(self, local_file_path, local_rotated_file_path, bucket_name, file_name, xyz, rotate_degree):
        self.local_file_path = local_file_path
        self.local_rotated_file_path = local_rotated_file_path
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.xyz = xyz
        self.rotate_degree = rotate_degree

    def download_s3_3d_model(self):
        aws_manager = AWSManager()
        aws_manager.download_from_s3(bucket_name=self.bucket_name,
                                     file_name=self.file_name,
                                     save_path=self.local_file_path)

    def _rotate_3d_model(self):
        rotate_manager = RotateManager()
        _3d_model = rotate_manager.rotate_3d_model(file_path=self.local_file_path, xyz=self.xyz, rotate_degree=self.rotate_degree)
        return _3d_model

    def save_3d_model(self, _3d_model):
        _3d_model.save(self.local_rotated_file_path)

    def show_preview(self):
        preview_manager = ShowPreviewManager()
        preview_manager.display(file_path=self.local_rotated_file_path)

    def rotate_3d_model(self):
        self.download_s3_3d_model()
        _3d_model = self._rotate_3d_model()
        self.save_3d_model(_3d_model=_3d_model)
        self.show_preview()
