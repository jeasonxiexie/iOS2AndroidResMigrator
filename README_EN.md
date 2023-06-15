[中文](./README.md)

# iOS2AndroidResMigrator

This is a simple library containing two scripts that convert string and image resources in an iOS project into a format suitable for Android projects.

## Script Introduction

1. **transfer.py**: This script is used to copy image resources from the iOS project to the Android project, process the file names to make them conform to Android's naming convention, and store the results in a folder named "output".

2. **convert_strings.py**: This script is used to convert the .strings file in the iOS project into the strings.xml file of Android, and store the results in a folder named "output".

## Usage Steps

### Image Resources Conversion (transfer.py)

1. Place the `transfer.py` script at the root of the iOS project.
2. Open the terminal, switch to the root of the iOS project.
3. Execute the command `python3 transfer.py`.
4. The converted files will be saved in the `output` folder.
5. Copy the files in the `output` folder to the `res` folder of the Android project.
6. Open Android Studio, click on the menu bar `Build -> Clean Project`.
7. Wait for Clean to finish, then click on the menu bar `Build -> Rebuild Project`.
8. After Rebuild is finished, the converted image resources can be used in the Android project.

### String Resources Conversion (convert_strings.py)

1. Place the `convert_strings.py` script at the root of the iOS project.
2. Open the terminal, switch to the root of the iOS project.
3. Execute the command `python3 convert_strings.py`.
4. The converted files will be saved in the `output` folder.
5. Copy the files in the `output` folder to the `res` folder of the Android project.
6. Open Android Studio, click on the menu bar `Build -> Clean Project`.
7. Wait for Clean to finish, then click on the menu bar `Build -> Rebuild Project`.
8. After Rebuild is finished, the converted string resources can be used in the Android project.

## Note

- Please make sure your Python environment is 3.6+.
- The conversion process will ignore comments and blank lines, only processing valid resource entries.
- It will process the source file name, converting uppercase letters to lowercase, and converting spaces and other characters that do not comply with Android's naming rules into underscores.
- If the file name starts with a number, the letter 'a' will be added in front of the file name.
- If the 'filename' field is missing in the source file, it will not be processed, and a related warning will be printed on the console.
- During the .strings file conversion process, special characters will be escaped.

If you encounter problems or need more features, feel free to submit an issue or PR.
