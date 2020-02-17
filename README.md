<img src="https://github.com/MuellerDominik/P5-AIonFPGA/blob/master/doc/report/graphics/top_assembly.png" align="right" alt="Throwing Booth Render" height="450">

# P5-AIonFPGA

> AI High-Performance Solution on FPGA

## Repository Structure

This repository is structured as follows:

```
.
├── cad                 # CAD files of the Throwing Booth
├── doc                 # Documentation
│   ├── fact-sheet      # Fact Sheet
│   ├── presentation    # Presentation
│   ├── project-plan    # Project Plan
│   └── report          # Project Report
└── sw                  # Software
    ├── cam-interface   # Camera Interface
    └── python          # Python Scripts
```

## Downloads

### Documents

The compiled `.pdf` files can be downloaded from here directly:

| Name               | Download               | SHA-256 checksum                                                   |
|:------------------ |:---------------------- |:------------------------------------------------------------------ |
| Project Plan       | [.pdf][Project Plan]   | `75256fd6d28adf24114fa799d3c93957663c4cb0b65e296efe11dfb00c0f3305` |
| **Project Report** | [.pdf][Project Report] | `1cc0ad37966c758b7be9acfc377187fbf6ed6d5011ed15d732652167e6351fd1` |
| Presentation       | [.pptx][Presentation]  | `98d2db6d353c2f17faa2e8a698cb1655aaf4e8a67ca07d807dd26fe1fddd615f` |
| Fact Sheet         | [.pdf][Fact Sheet]     | `c5267fa345f4ed9caf45743bf182baf9919883fc5a41b03d3843d0520dc32060` |

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

| Name             | Download                 | SHA-256 checksum                                                   |
|:---------------- |:------------------------ |:------------------------------------------------------------------ |
| Camera Interface | [.exe][Camera Interface] | `6fe96e48369980c44b1ec7f457cd6a8e701554c5ae7c9b6a90c904dd19e3de93` |
| Database         | [.csv][Database]         | `12a48e5d6550a2349968a423ea74518bb0d7ee153c19a7675a96eec8ee55d664` |

## License

Copyright &copy; 2019 Dominik Müller and Nico Canzani

This project is licensed under the terms of the Apache License 2.0 - see the [LICENSE](LICENSE "LICENSE") file for details

[Project Plan]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v0.0.2/p5_aionfpga_project-plan_canzani_mueller.pdf
[Project Report]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.0/p5_aionfpga_report_canzani_mueller.pdf
[Presentation]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.1/p5_aionfpga_presentation_canzani_mueller.pptx
[Fact Sheet]: https://github.com/MuellerDominik/P5-AIonFPGA/releases/download/v1.0.1/p5_aionfpga_fact-sheet_canzani_mueller.pdf

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
