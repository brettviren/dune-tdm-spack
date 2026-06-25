from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class WireCellArrow(CMakePackage):
    """WireCell <-> Apache Arrow (wc.frame) conversion for the TDM."""

    homepage = "https://github.com/WireCell/wire-cell-arrow"
    git = "https://github.com/WireCell/wire-cell-arrow.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    depends_on("arrow")
    depends_on("wire-cell-toolkit")
