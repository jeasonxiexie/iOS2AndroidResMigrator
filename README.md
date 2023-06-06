# iOS2AndroidResMigrator

这是一个简易的库，包含两个脚本，用于将iOS项目中的字符串资源以及图片资源转换为适用于Android项目的形式。

## 脚本介绍

1. **transfer.py**: 该脚本用于将iOS项目中的图片资源拷贝到Android项目中，处理文件名使其符合Android的命名规范，并将结果存放到名为 "output" 的文件夹中。

2. **convert_strings.py**: 该脚本用于将iOS项目中的.strings文件转换为Android的strings.xml文件，并将结果存放到名为 "output" 的文件夹中。

## 使用步骤

### 图片资源转换（transfer.py）

1. 将`transfer.py`脚本放置在iOS项目的根目录下。
2. 打开终端，切换到iOS项目的根目录下。
3. 执行命令 `python3 transfer.py`。
4. 转换后的文件将会保存在`output`文件夹中。
5. 将`output`文件夹中的文件拷贝到Android项目的`res`文件夹中。
6. 打开Android Studio，点击菜单栏的 `Build -> Clean Project`。
7. 等待Clean完成后，点击菜单栏的 `Build -> Rebuild Project`。
8. 等待Rebuild完成后，即可在Android项目中使用转换后的图片资源。

### 字符串资源转换（convert_strings.py）

1. 将`convert_strings.py`脚本放置在iOS项目的根目录下。
2. 打开终端，切换到iOS项目的根目录下。
3. 执行命令 `python3 convert_strings.py`。
4. 转换后的文件将会保存在`output`文件夹中。
5. 将`output`文件夹中的文件拷贝到Android项目的`res`文件夹中。
6. 打开Android Studio，点击菜单栏的 `Build -> Clean Project`。
7. 等待Clean完成后，点击菜单栏的 `Build -> Rebuild Project`。
8. 等待Rebuild完成后，即可在Android项目中使用转换后的字符串资源。

## 注意事项

- 请确保Python环境为3.6+。
- 转换过程中，会忽略注释和空行，只处理有效的资源条目。
- 会对源文件名进行处理，将大写字母转换为小写，将空格和其他不符合Android命名规范的字符转换为下划线。
- 如果文件名以数字开头，则在文件名前添加字母 'a'。
- 若源文件中有文件缺失 'filename' 字段，将不会被处理，且会在控制台打印出相关警告。
- .strings 文件转换过程中，会对特殊字符进行转义。

如果遇到问题或需要更多功能，欢迎提交issue或者PR。
