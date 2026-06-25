from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class DuneDaqArrowFrameHdf(CMakePackage):
    """DUNE DAQ HDF5 -> WireCell wc.frame (Arrow/HDF5) pipeline tool, including the
    DUNE-DAQ -> WCT bridge (ToFrame). Part of the TDM (Transient Data Model)."""

    homepage = "https://github.com/brettviren/dune-daq-arrow-frame-hdf"
    git = "https://github.com/brettviren/dune-daq-arrow-frame-hdf.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    depends_on("arrow")
    depends_on("arrow-hdf")
    depends_on("dune-daq-codec")
    depends_on("dune-daq-hdf")
    depends_on("wire-cell-arrow")
    depends_on("wire-cell-toolkit")  # the ToFrame bridge links WireCell directly
