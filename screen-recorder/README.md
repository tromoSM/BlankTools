#### **[BlankTools](https://github.com/tromoSM/BlankTools/)** / [screen-recorder](https://github.com/tromoSM/BlankTools/tree/main/screen-recorder)
****
- Simple lightweight screen recorder.

### Preferences
| Variable name | Variable types | Description | Default | Example| additional info |
|----------|---------|----|---------------------------|------|-|
| filename | str | file name | Recording | Screen recording | |
| codec | str | codec | mp4v | 'V','P','8','0' | this codec should be compatible with the file format |
| fileformat | str | file format | mp4 | webM | this file format should be compatible with the codec |
| fps | int/float | frames per second | 30.0 | 15.0 | |
| Notify | bool | notify when saved | True | False | |

>[!NOTE]
> Set `fps` to a lower number your pc can handle if your pc is a lower-end pc. see why

>[!TIP]
> Set `codec` to `'V','P','8','0'` and `fileformat` to `webM` be compatible with web browsers. 
#### Dependencies
- All the dependecies can be found in [requirements.txt](Requirements.txt)
#### Date
- 2025.10.31 as YYYY.MM.DD
#### Python version
- Python 3 (tested on 3.13)
***
##### © 2025 - tromoSM. All rights reserved.

