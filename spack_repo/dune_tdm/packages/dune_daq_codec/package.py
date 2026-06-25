from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class DuneDaqCodec(CMakePackage):
    """Decode DUNE DAQ readout fragments into dense ADC for the TDM."""

    homepage = "https://github.com/brettviren/dune-daq-codec"
    git = "https://github.com/brettviren/dune-daq-codec.git"

    maintainers("brettviren")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    depends_on("dune-daq-types")
