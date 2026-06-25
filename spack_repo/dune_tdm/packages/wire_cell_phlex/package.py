from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class WireCellPhlex(CMakePackage):
    """WireCell algorithms exposed as Phlex components for the TDM."""

    homepage = "https://github.com/brettviren/wire-cell-phlex"
    git = "https://github.com/brettviren/wire-cell-phlex.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    depends_on("boost")
    depends_on("tbb")
    depends_on("phlex")
    depends_on("wire-cell-toolkit")
