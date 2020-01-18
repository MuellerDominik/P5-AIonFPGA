# P5-AIonFPGA

> AI High-Performance Solution on FPGA

## Repository Structure

This repository is structured as follows:

```
.
├── cad                 # CAD files of the Throwing Booth
├── doc                 # Documentation
│   ├── project-plan    # Project Plan
│   └── report          # Project Report
└── sw                  # Software
    ├── cam_interface   # Camera Interface
    └── python          # Python Scripts
```

## Downloads

### Documents

The compiled `.pdf` files can be downloaded from here directly:

| Name           | Download             |
|:-------------- |:-------------------- |
| Project Plan   | [.pdf][Project Plan] |
| Project Report | [/][Project Report]  |

#### Compilation

The `.pdf` files can be built by running `make` in the respective directory:

```bash
$ make build clean
```

### Mechanical

| Name               | CAD                       | Drawing                           |
|:------------------ |:------------------------- |:--------------------------------- |
| Mounting Adapter   | [.dxf][Mounting Adapter]  | [.pdf][Mounting Adapter Drawing]  |
| Camera Protection  | [.dxf][Camera Protection] | [.pdf][Camera Protection Drawing] |

## License

Copyright &copy; 2019 Dominik Müller and Nico Canzani

This project is licensed under the terms of the Apache License 2.0 - see the [LICENSE](LICENSE "LICENSE") file for details

[Project Plan]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.2/p5_aionfpga_project-plan_canzani_mueller.pdf
[Project Report]: #
[Mounting Adapter]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.3/MountingAdapter.dxf
[Camera Protection]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.3/CameraProtection.dxf
[Mounting Adapter Drawing]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.3/MountingAdapter.pdf
[Camera Protection Drawing]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.3/CameraProtection.pdf
