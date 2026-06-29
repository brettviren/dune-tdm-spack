from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Phlexed(CMakePackage):
    """A Jsonnet-extended variant of the Phlex command-line driver.

    phlexed is a strict superset of the stock ``phlex`` program: it accepts
    every option ``phlex`` does and adds Jsonnet "top-level argument" (TLA)
    support (-A / --tla-str, --tla-str-file, --tla-code, --tla-code-file) plus
    library search-path control (-J / --jpath and the PHLEXED_PATH environment
    variable, resolved first-found-wins).
    """

    homepage = "https://github.com/brettviren/phlexed"
    git = "https://github.com/brettviren/phlexed.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    # Directly used by phlexed's sources / CMakeLists:
    #   * Boost.ProgramOptions parses the command line; Boost.JSON is used for
    #     the configuration object (also pulled in transitively via phlex).
    #   * phlex provides phlex::experimental::run/version (phlex::run_phlex).
    #   * jsonnet provides the C++ wrapper (libjsonnet++) phlexed evaluates with.
    # TBB/spdlog/fmt are consumed only through phlex's exported interface and so
    # are not declared here (they arrive transitively, as in wire-cell-phlex).
    depends_on("boost +json +program_options")
    depends_on("phlex")
    # The `libjsonnet` virtual is provided by go-jsonnet (default, fast) or by
    # the C/C++ `jsonnet` package; phlexed just needs the libjsonnet++ wrapper.
    depends_on("libjsonnet")
