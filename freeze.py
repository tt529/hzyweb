import os
import shutil
from app import app, freezer

if __name__ == '__main__':
    freezer.freeze()

    # 定义源文件和目标文件路径
    source_file = os.path.join('build', 'index.html')
    target_file = os.path.join('build', 'index.html')

    # 检查源文件是否存在
    if os.path.exists(source_file):
        # 移动文件到根目录
        shutil.move(source_file, target_file)
        print(f"Moved {source_file} to {target_file}")
    else:
        print(f"{source_file} does not exist")