# [xhls] Vision - mpeg_forward

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Usage](#usage)
* [References](#References)
* [Contributing](#contributing)



<!-- ABOUT THE PROJECT -->
## About The Project
The DCT concentrates most of the pixels energy distribution into a few frequency coefficients. DCT is a valuable tool for pictures compression, when associated with Quantization and VLC. The transform itself does not compress images and it is accurately reversible. DCT is a separable transform: 2-D F-DCT and I-DCT can be done as consecutive 1-D transforms.

**Directory structure**
```
README.md
code/
    dct.h
    dct_coeff_table.h
    fdctref.cpp
    my_dct.cpp
    wang_fdct.cpp
code_opt/
    dct.h
    dct_coeff_table.h
    fdctref.cpp
    my_dct.cpp
    wang_fdct.cpp
testdata/
    test_wang_fdct.cpp
    pynq_python/
        dct.py
script/
    run_hls_dct_script.tcl
impl/
    top_fdct_csynth.rpt
    wang_dct_1d_1_csynth.rpt
    wang_dct_1d_csynth.rpt
```

<!-- USAGE EXAMPLES -->
## Usage

1. fpga board setup

We use **Xilinx ZedBoard Evaluation and Development Kit** to evaulate this project

2. using HLS vivado to simulation and synthesis

3. export RTL

4. generate .bit from vivado

3. python test
```shell 
 python dct.py
```
## References
* https://github.com/Xilinx/HLx_Examples

<!-- CONTRIBUTING -->
## Contributing
* code modification and pipeline
