# Operator-mono-lig 字体

## Prerequisites

- The original _Operator Mono_ font... of course.
- Python (v2.7+)
- Node.js
- Install _fonttools_ from https://github.com/fonttools/fonttools
  - Windows/Linux: `pip install fonttools`
  - Mac: `pip3 install fonttools`

## Installation

Once all the prerequisites have been installed, clone this repo or download latest release from [Releases](https://github.com/kiliman/operator-mono-lig/releases) and unzip.

Next, copy your _Operator Mono_ OpenType files into the `original` folder. **NOTE**: Filenames must not include spaces. It should look like:

- OperatorMonoSSm-Book.otf
- OperatorMonoSSm-BookItalic.otf
- OperatorMono-Light.otf
- OperatorMono-LightItalic.otf
- etc.

Finally, run the following commands to install npm dependencies and build the font files. The new font files will be placed in the `build` folder. You can now install these fonts on your system.

```sh
npm install

# Windows
build

# Linux/Mac
./build.sh
```

# 在ArchLinux上编译
