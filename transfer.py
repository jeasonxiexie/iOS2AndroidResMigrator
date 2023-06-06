/**
    * 该脚本用于将iOS项目中的图片资源拷贝到Android项目中
    * 该脚本需要放在iOS项目的根目录下
    * 该脚本需要在Python 3.6+环境下运行
    * 使用方法：
    * 1. 将该脚本放置在iOS项目的根目录下
    * 2. 打开终端，cd到iOS项目的根目录下
    * 3. 执行命令 python3 transfer.py
    * 4. 转换后的文件将会保存在output文件夹中
    * 5. 将output文件夹中的文件拷贝到Android项目的res文件夹中
    * 6. 打开Android Studio，点击菜单栏的 Build -> Clean Project
    * 7. 等待Clean完成后，点击菜单栏的 Build -> Rebuild Project
    * 8. 等待Rebuild完成后，即可在Android项目中使用转换后的图片资源
    */
import os
import shutil
import json

# 定义源目录
source_dir = './Assets.xcassets'

# 定义目标目录
dest_dir = './output'

# 定义Android drawable文件夹和对应的iOS图片后缀
drawable_dirs = {
    '1x': 'drawable-mdpi',
    '1.5x': 'drawable-hdpi',
    '2x': 'drawable-xhdpi',
    '3x': 'drawable-xxhdpi',
    '4x': 'drawable-xxxhdpi'
}

# 遍历源目录中的所有文件夹
for root, dirs, files in os.walk(source_dir):
    if '.imageset' in root:
        with open(os.path.join(root, 'Contents.json')) as json_file:
            data = json.load(json_file)
            for image in data['images']:
                if 'filename' in image:
                    filename = image['filename']
                    scale = image['scale']
                    drawable_dir = drawable_dirs[scale]

                    # 对文件名进行处理，将大写字母转换为小写，将空格转换为下划线，还有其他不符合Android命名规范的字符
                    filename_android = filename.replace(' ', '_').replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '').replace('\'', '').replace('&', '').replace('!', '').replace(',', '').replace('?', '').replace(';', '').replace(':', '').replace('，', '').replace('。', '').replace('？', '').replace('；', '').replace('：', '').replace('！', '').replace('、', '').replace('（', '').replace('）', '').replace('‘', '').replace('’', '').replace('“', '').replace('”', '').replace('【', '').replace('】', '').replace('《', '').replace('》', '').replace('——', '').replace('—', '').replace('……', '').replace('·', '').lower()
                    # 处理 '@2x' 和 '@3x'
                    if '@' in filename_android:
                        filename_android = filename_android.split('@')[0] + filename_android.split('@')[1][2:]

                    # 如果文件名以数字开头，则在文件名前添加字母 'a'
                    if filename_android[0].isdigit():
                        filename_android = 'a' + filename_android

                    # 创建目标文件夹
                    os.makedirs(os.path.join(dest_dir, drawable_dir), exist_ok=True)

                    # 拷贝文件
                    shutil.copyfile(os.path.join(root, filename), os.path.join(dest_dir, drawable_dir, filename_android))
                else:
                    print(f"WARNING: No 'filename' in image object in {root}/Contents.json. This image will be ignored.")
                    
print('图片资源拷贝完成')
