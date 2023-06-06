/**
    * 该脚本用于将iOS的.strings文件转换为Android的strings.xml文件
    * 使用方法：
    * 1. 将该脚本放置在iOS项目的根目录下
    * 2. 打开终端，cd到iOS项目的根目录下
    * 3. 执行命令 python3 convert_strings.py
    * 4. 转换后的文件将会保存在output文件夹中
    * 5. 将output文件夹中的文件拷贝到Android项目的res文件夹中
    * 6. 打开Android Studio，点击菜单栏的 Build -> Clean Project
    * 7. 等待Clean完成后，点击菜单栏的 Build -> Rebuild Project
    * 8. 等待Rebuild完成后，即可在Android项目中使用转换后的字符串资源
    */

import os
import codecs
import glob
import re

# 定义源目录
source_dir = "./"

# 定义目标目录
dest_dir = "./output"

# 定义需要转换的.strings文件
strings_files = ['Localizable.strings', 'InfoPlist.strings']

# 定义语言和对应的Android资源目录名
langs = {
    'de.lproj': 'values-de',
    'en.lproj': 'values-en',
    'es.lproj': 'values-es',
    'fr.lproj': 'values-fr',
    'it.lproj': 'values-it',
    'ja.lproj': 'values-ja',
    'ko.lproj': 'values-ko',
    'ru.lproj': 'values-ru',
    'zh-Hans.lproj': 'values-zh-rCN',
    'th.lproj': 'values-th',
    'zh-Hant.lproj': 'values-zh-rTW'
}

# 对每个语言和对应的.strings文件进行处理
for lang, res_dir in langs.items():
    # 创建目标文件的目录
    os.makedirs(os.path.join(dest_dir, res_dir), exist_ok=True)

    # 打开目标文件，只写模式，并写入XML头部
    with open(os.path.join(dest_dir, res_dir, 'strings.xml'), 'w') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write('<resources>\n')

    for strings_file in strings_files:
        # 打开源文件
        with codecs.open(os.path.join(source_dir, lang, strings_file), 'r', 'utf-8') as f:
            lines = f.readlines()

        # 打开目标文件，追加模式
        with open(os.path.join(dest_dir, res_dir, 'strings.xml'), 'a') as f:
            # 处理每一行
            for line in lines:
                # 去除注释和空行
                line = line.strip()
                if not line or line.startswith('//') or line.startswith('/*') or line.endswith('*/'):
                    continue

                # 分割键值对
                parts = line.split(' = ', 1)
                if len(parts) != 2:
                    print(f"Skipped line {line}")
                    continue
                key, value = parts
                key = key.strip('"')
                value = value.strip('";')

                # 转换键为小写并替换非法字符
                key = re.sub('[^a-z0-9_]', '_', key.lower())
                # 对value的特殊字符进行转义
                value = value.replace("'", "\\'")
                value = value.replace("&", "&amp;")
                value = value.replace("<", "&lt;")
                value = value.replace(">", "&gt;")
                value = value.replace("\"", "\\\"")
                value = value.replace("\n", "\\n")
                # 写入<string>标签
                f.write('    <string name="%s">%s</string>\n' % (key, value))
    
    # 打开目标文件，追加模式，并写入XML尾部
    with open(os.path.join(dest_dir, res_dir, 'strings.xml'), 'a') as f:
        f.write('</resources>\n')
