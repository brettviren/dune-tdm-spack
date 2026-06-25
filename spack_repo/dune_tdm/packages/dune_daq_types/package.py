from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class DuneDaqTypes(CMakePackage):
    """DUNE DAQ data types for the TDM (Transient Data Model)."""

    homepage = "https://github.com/brettviren/dune-daq-types"
    git = "https://github.com/brettviren/dune-daq-types.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")
