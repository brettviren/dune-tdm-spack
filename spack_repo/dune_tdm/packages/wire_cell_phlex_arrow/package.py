from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class WireCellPhlexArrow(CMakePackage):
    """Arrow-backed data products bridging WireCell and Phlex for the TDM."""

    homepage = "https://github.com/brettviren/wire-cell-phlex-arrow"
    git = "https://github.com/brettviren/wire-cell-phlex-arrow.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    depends_on("arrow")
    depends_on("boost")
    depends_on("spdlog")
    depends_on("tbb")
    depends_on("phlex")
    depends_on("wire-cell-toolkit")
    depends_on("phlex-arrow-common")
    depends_on("wire-cell-arrow")
    depends_on("wire-cell-phlex")
