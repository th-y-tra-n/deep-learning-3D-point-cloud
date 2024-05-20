###########################################################
# IMPORT LIBRARIES
###########################################################
import open3d as o3d
import copy
import numpy as np
import open3d.visualization.gui as gui

###########################################################
# RIGID TRANSFORMATIONS MODULE
###########################################################
# Translation
def translate():
    armadillo_data = o3d.data.ArmadilloMesh()
    pcd = o3d.io.read_triangle_mesh(armadillo_data.path).sample_points_poisson_disk(5000)
    pcd_tx = copy.deepcopy(pcd).translate((150, 0, 0))
    pcd_ty = copy.deepcopy(pcd).translate((0, 200, 0))
    print('Displaying original point cloud and translated geometries')
    o3d.visualization.draw([{
        "name": "Original geometry",
        "geometry": pcd
    },
        {
        "name": "Translated geometry (x-axis)",
        "geometry": pcd_tx
    },
        {
        "name": "Translated geometry (y-axis)",
        "geometry": pcd_ty
        }
    ], show_ui=True)


# Rotation
def rotate():
    armadillo_data = o3d.data.ArmadilloMesh()
    pcd = o3d.io.read_triangle_mesh(armadillo_data.path).sample_points_poisson_disk(5000)
    pcd_rx = copy.deepcopy(pcd).rotate(R=o3d.geometry.get_rotation_matrix_from_xyz((np.pi / 2, 0, 0)), center=(0, 0, 0))
    pcd_ry = copy.deepcopy(pcd).rotate(R=o3d.geometry.get_rotation_matrix_from_xyz((0, np.pi / 2, 0)), center=(0, 0, 0))
    pcd_rz = copy.deepcopy(pcd).rotate(R=o3d.geometry.get_rotation_matrix_from_xyz((0, 0, np.pi / 2)), center=(0, 0, 0))
    print('Displaying original point cloud and rotated geometries')
    o3d.visualization.draw([{
        "name": "Original geometry",
        "geometry": pcd
    },
        {
        "name": "Rotated geometry (x-axis)",
        "geometry": pcd_rx
    },
        {
        "name": "Rotated geometry (y-axis)",
        "geometry": pcd_ry
    },
        {
        "name": "Rotated geometry (z-axis)",
        "geometry": pcd_rz
        }
    ], show_ui=True)

# Scaling
def scale():
    armadillo_data = o3d.data.ArmadilloMesh()
    pcd = o3d.io.read_triangle_mesh(armadillo_data.path).sample_points_poisson_disk(5000)
    pcd_sx = copy.deepcopy(pcd).scale((0.5, 1, 1), center=(0, 0, 0))
    pcd_sy = copy.deepcopy(pcd).scale((1, 2, 1), center=(0, 0, 0))
    pcd_sz = copy.deepcopy(pcd).scale((1, 1, 3), center=(0, 0, 0))
    print('Displaying original point cloud and scaled geometries')
    o3d.visualization.draw([{
        "name": "Original geometry",
        "geometry": pcd
    },
        {
        "name": "Scaled geometry (x-axis)",
        "geometry": pcd_sx
    },
        {
        "name": "Scaled geometry (y-axis)",
        "geometry": pcd_sy
    },
        {
        "name": "Scaled geometry (z-axis)",
        "geometry": pcd_sz
        }
    ], show_ui=True)

# Shearing
def shear():
    armadillo_data = o3d.data.ArmadilloMesh()
    pcd = o3d.io.read_triangle_mesh(armadillo_data.path).sample_points_poisson_disk(5000)
    pcd_shx = copy.deepcopy(pcd).shear((1, 0, 0, 0, 1, 0, 0, 0, 1), center=(0, 0, 0))
    pcd_shy = copy.deepcopy(pcd).shear((1, 0, 0, 0, 1, 0, 0, 0, 1), center=(0, 0, 0))
    pcd_shz = copy.deepcopy(pcd).shear((1, 0, 0, 0, 1, 0, 0, 0, 1), center=(0, 0, 0))
    print('Displaying original point cloud and sheared geometries')
    o3d.visualization.draw([{
        "name": "Original geometry",
        "geometry": pcd
    },
        {
        "name": "Sheared geometry (x-axis)",
        "geometry": pcd_shx
    },
        {
        "name": "Sheared geometry (y-axis)",
        "geometry": pcd_shy
    },
        {
        "name": "Sheared geometry (z-axis)",
        "geometry": pcd_shz
        }
    ], show_ui=True)

# Reflection
def reflect():
    armadillo_data = o3d.data.ArmadilloMesh()
    pcd = o3d.io.read_triangle_mesh(armadillo_data.path).sample_points_poisson_disk(5000)
    pcd_rx = copy.deepcopy(pcd).rotate(R=o3d.geometry.get_rotation_matrix_from_xyz((np.pi, 0, 0)), center=(0, 0, 0))
    pcd_ry = copy.deepcopy(pcd).rotate(R=o3d.geometry.get_rotation_matrix_from_xyz((0, np.pi, 0)), center=(0, 0, 0))
    pcd_rz = copy.deepcopy(pcd).rotate(R=o3d.geometry.get_rotation_matrix_from_xyz((0, 0, np.pi)), center=(0, 0, 0))
    print('Displaying original point cloud and reflected geometries')
    o3d.visualization.draw([{
        "name": "Original geometry",
        "geometry": pcd
    },
        {
        "name": "Reflected geometry (x-axis)",
        "geometry": pcd_rx
    },
        {
        "name": "Reflected geometry (y-axis)",
        "geometry": pcd_ry
    },
        {
        "name": "Reflected geometry (z-axis)",
        "geometry": pcd_rz
        }
    ], show_ui=True)

###########################################################
# NON-RIGID TRANSFORMATIONS MODULE
###########################################################


###########################################################
# MAIN FUNCTION
###########################################################
if __name__ == "__main__":
    gui.Application.instance.initialize()
    #translate()
    #rotate()
    #scale()
    #shear()
    #reflect()
    gui.Application.instance.post_to_main_thread(rotate())