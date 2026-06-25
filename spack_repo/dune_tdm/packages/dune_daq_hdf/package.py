from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class DuneDaqHdf(CMakePackage):
    """DUNE DAQ HDF5 file access for the TDM (Transient Data Model)."""

    homepage = "https://github.com/brettviren/dune-daq-hdf"
    git = "https://github.com/brettviren/dune-daq-hdf.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    depends_on("dune-daq-types")
    depends_on("hdf5")
