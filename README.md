<img src="https://github.com/MuellerDominik/P5-AIonFPGA/blob/master/doc/report/graphics/top_assembly.png" align="right" alt="Throwing Booth Render" height="220">

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
    ├── cam-interface   # Camera Interface
    └── python          # Python Scripts
```

## Downloads

### Documents

The compiled `.pdf` files can be downloaded from here directly:

| Name           | Download               |
|:-------------- |:---------------------- |
| Project Plan   | [.pdf][Project Plan]   |
| Project Report | [.pdf][Project Report] |

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
| Rear Panel         | [.dxf][Rear Panel]        | [.pdf][Rear Panel Drawing]        |
| Side Panel         | [.dxf][Side Panel]        | [.pdf][Side Panel Drawing]        |
| Fibox              |                           | [.pdf][Fibox Drawing]             |
| Throwing Booth     | [.stp][Throwing Booth]    |                                   |

### Software

| Name             | Download                 |
|:---------------- |:------------------------ |
| Camera Interface | [.exe][Camera Interface] |
| Database         | [.csv][Database]         |

## License

Copyright &copy; 2019 Dominik Müller and Nico Canzani

This project is licensed under the terms of the Apache License 2.0 - see the [LICENSE](LICENSE "LICENSE") file for details

[Project Plan]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.2/p5_aionfpga_project-plan_canzani_mueller.pdf
[Project Report]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/p5_aionfpga_report_canzani_mueller.pdf
[Mounting Adapter]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.3/MountingAdapter.dxf
[Camera Protection]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.3/CameraProtection.dxf
[Rear Panel]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.4/RearPanel.dxf
[Side Panel]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.4/SidePanel.dxf
[Throwing Booth]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/Throwing_Booth_Model.stp
[Mounting Adapter Drawing]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/Mounting_Adapter_Drawing.pdf
[Camera Protection Drawing]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/Camera_Protection_Drawing.pdf
[Rear Panel Drawing]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/Rear_Panel_Drawing.pdf
[Side Panel Drawing]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/Side_Panel_Drawing.pdf
[Fibox Drawing]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/Fibox_Drawing.pdf
[Camera Interface]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/cam-interface.exe
[Database]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/aionfpga_db.csv
