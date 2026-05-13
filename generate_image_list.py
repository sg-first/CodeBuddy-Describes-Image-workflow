import os

def generate_image_list(source_dir, output_file):
    """
    生成指定目录中所有图片的相对路径列表
    
    Args:
        source_dir: 图片目录路径
        output_file: 输出文件路径
    """
    image_extensions = {'.png', '.jpg'}
    
    image_paths = []
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, os.path.dirname(source_dir))
                image_paths.append(rel_path)
    
    image_paths.sort()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(image_paths))
    
    print(f"共找到 {len(image_paths)} 张图片")
    print(f"结果已保存到：{output_file}")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_dir = os.path.join(base_dir, 'UITextures')
    output_file = os.path.join(base_dir, 'images_list_full.txt')
    
    generate_image_list(source_dir, output_file)
