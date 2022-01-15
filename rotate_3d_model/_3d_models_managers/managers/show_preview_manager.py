from matplotlib import pyplot
from mpl_toolkits import mplot3d
from stl import mesh


class ShowPreviewManager:

    def display(self, file_path):
        figure = pyplot.figure()
        axes = mplot3d.Axes3D(figure)
        _3d_model = mesh.Mesh.from_file(file_path)
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(_3d_model.vectors))
        scale = _3d_model.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)
        pyplot.show(block=True)
