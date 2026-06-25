from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class PhlexArrowCommon(CMakePackage):
    """Common Phlex <-> Apache Arrow conversion utilities for the TDM."""

    homepage = "https://github.com/brettviren/phlex-arrow-common"
    git = "https://github.com/brettviren/phlex-arrow-common.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    depends_on("arrow")
    depends_on("boost")
    depends_on("phlex")
    depends_on("spdlog")
