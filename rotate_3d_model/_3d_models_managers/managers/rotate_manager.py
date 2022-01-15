import math

from stl import mesh


class RotateManager:
    def rotate_3d_model(self, file_path, xyz, rotate_degree):
        _3d_model = mesh.Mesh.from_file(filename=file_path)
        _3d_model.rotate(xyz, math.radians(rotate_degree))
        return _3d_model
