# dune-tdm-spack

A [Spack](https://spack.io) package repository (Package API **v2.0**, namespace
**`dune_tdm`**) for the DUNE **TDM** (Transient Data Model) suite — the
locally-developed Phlex / WireCell / DUNE-DAQ Arrow-HDF packages.

Layout follows modern Spack conventions:

    spack_repo/dune_tdm/repo.yaml
    spack_repo/dune_tdm/packages/<pkg>/package.py

## Use

Register the repo in a Spack environment's `spack.yaml`:

```yaml
spack:
  repos:
    dune_tdm: /path/to/dune-tdm-spack/spack_repo/dune_tdm
```

## Packages

- **`dune-xerosere`** — a bundle capturing the whole suite; depends on the three
  top-level consumers below, which transitively pull in everything else.
- Top-level: `dune-daq-arrow-frame-hdf`, `phlex-arrow-hdf`, `wire-cell-phlex-arrow`
- Libraries: `arrow-hdf`, `dune-daq-types`, `dune-daq-codec`, `dune-daq-hdf`,
  `phlex-arrow-common`, `wire-cell-arrow`, `wire-cell-phlex`

Each package tracks its upstream `main` branch (these are unreleased
development repositories). External dependencies (`arrow`, `hdf5`, `boost`,
`spdlog`, `tbb`, `phlex`, `wire-cell-toolkit`) come from `builtin` and the
`phlex` / `wirecell` repos.
