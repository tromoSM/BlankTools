#### **[BlankTools](https://github.com/tromoSM/BlankTools/)** / [Random-image-generator](https://github.com/tromoSM/BlankTools/tree/main/Random-image-generator)
****
- creates random images by giving each pixel of the image a random color.
### Difference between `Pseudo-random` and `cryptographically-secure-pseudo-random`
| Method | Advantage |
|-------|-------|
|Pseudo-random | Very fast and efficient| 
|cryptographically-secure-pseudo-random | Designed to be unpredictable |
--------------------------------------------
### Preferences
| Variable name | Variable types | Description | Default | Example| additional info |
|----------|---------|----|---------------------------|------|-|
| fileform | str | file format | png | jpeg | |
| name | str | file name | gurt | photo1 | |
| location | str | file path | `empty` | C:/Users/`username`/Photos/ | use `/` instead of `\` |
| res | Int/Float | screen dimesions*res = resolution of the image | 10 | 0.1 | value must be more than 0. value could be a float |
>[!WARNING]
>Increasing 'res' to a higher value than your pc can handle might freeze your pc.
#### Dependencies
- All the dependecies can be found in [requirements.txt](Requirements.txt)
#### Date
- 2025.10.17 as YYYY.MM.DD
#### Python version
- Python 3.13+ (tested on 3.13 and 3.14)
***
##### © 2025 - tromoSM. All rights reserved.

