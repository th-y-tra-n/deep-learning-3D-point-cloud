###########################################################
# IMPORT LIBRARIES
###########################################################
import open3d as o3d
import copy

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

# Scaling

# Shearing

# Reflection


###########################################################
# NON-RIGID TRANSFORMATIONS MODULE
###########################################################


###########################################################
# MAIN FUNCTION
###########################################################
if __name__ == "__main__":
    translate()