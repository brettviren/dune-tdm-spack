from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class ArrowHdf(CMakePackage):
    """Apache Arrow <-> HDF5 storage for the DUNE TDM (Transient Data Model)."""

    homepage = "https://github.com/brettviren/arrow-hdf"
    git = "https://github.com/brettviren/arrow-hdf.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    depends_on("arrow")
    depends_on("hdf5")
