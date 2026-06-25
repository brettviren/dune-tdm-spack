from spack_repo.builtin.build_systems.bundle import BundlePackage

from spack.package import *


class DuneXerosere(BundlePackage):
    """DUNE Xerosere TDM (Transient Data Model) suite.

    A bundle (metapackage) capturing the full set of locally-developed
    Phlex / WireCell / DUNE-DAQ Arrow-HDF packages. Depending on the three
    top-level consumers transitively pulls in the whole suite.
    """

    homepage = "https://github.com/brettviren/dune-xerosere"

    maintainers("brettviren")

    version("0.1.0")

    depends_on("dune-daq-arrow-frame-hdf")
    depends_on("phlex-arrow-hdf")
    depends_on("wire-cell-phlex-arrow")
