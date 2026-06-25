from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class PhlexArrowHdf(CMakePackage):
    """Phlex Arrow data products persisted in HDF5 for the TDM."""

    homepage = "https://github.com/brettviren/phlex-arrow-hdf"
    git = "https://github.com/brettviren/phlex-arrow-hdf.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    depends_on("arrow")
    depends_on("boost")
    depends_on("hdf5")
    depends_on("spdlog")
    depends_on("tbb")
    depends_on("phlex")
    depends_on("arrow-hdf")
    depends_on("phlex-arrow-common")
