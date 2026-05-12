import subprocess
import sys
import os


def get_image_paths_from_range(start_line, end_line, list_file="all_images_list.txt"):
    """
    根据行号起终点，从all_images_list.txt中获取对应区间的图片路径
    
    Args:
        start_line: 起始行号（从1开始）
        end_line: 结束行号（包含）
        list_file: 图片列表文件路径
    
    Returns:
        list: 图片路径列表
    """
    image_paths = []
    
    if not os.path.exists(list_file):
        print(f"错误：文件 {list_file} 不存在")
        return []
    
    with open(list_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 行号从1开始，所以转换为0-based索引
    start_index = max(0, start_line - 1)
    end_index = min(len(lines), end_line)
    
    for i in range(start_index, end_index):
        line = lines[i].strip()
        if line:
            image_paths.append(line)
    
    print(f"从第{start_line}行到第{end_line}行，共获取到 {len(image_paths)} 张图片路径")
    return image_paths


def call_codebuddy_for_images(image_paths):
    """
    调用codebuddy -p命令，让AI为图片列表生成描述
    
    Args:
        image_paths: 图片文件路径列表
    
    Returns:
        str: AI生成的描述文本
    """
    if not image_paths:
        print("没有图片需要处理")
        return ""
    
    # 构建prompt
    files_str = "\n".join(image_paths)
    prompt = f"""你是图片描述助手。你的任务是逐个读取以下图片，用AI视觉能力观察每张图片的内容，然后为每张图片生成一段中文描述
**重要规则：**
1. 必须使用 Read 工具逐个读取每张图片文件路径来查看图片内容
2. 绝对不能根据文件名猜测内容——必须实际读取图片
3. 不能写脚本批量处理，必须逐张读取并描述
4. 每张图片描述格式：`【文件名】描述文字`

以下是需要描述的图片列表：
{files_str}"""
    
    print(f"正在调用codebuddy处理 {len(image_paths)} 张图片...")
    
    try:
        # 调用codebuddy -p命令
        result = subprocess.run(
            ["codebuddy", "-p", prompt, "--model", "Kimi-K2.5"],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode != 0:
            print(f"codebuddy执行出错: {result.stderr}")
            return ""
        
        print("codebuddy处理完成")
        return result.stdout
    
    except FileNotFoundError:
        print("错误：找不到codebuddy命令，请确保codebuddy已安装并添加到PATH环境变量")
        return ""
    except Exception as e:
        print(f"调用codebuddy时发生错误: {e}")
        return ""


def append_to_result(text, result_file="result.txt"):
    """
    将文本追加到result.txt文件
    
    Args:
        text: 要追加的文本
        result_file: 结果文件路径
    
    Returns:
        bool: 是否成功
    """
    try:
        with open(result_file, 'a', encoding='utf-8') as f:
            f.write(text)
            if not text.endswith('\n'):
                f.write('\n')
        
        print(f"成功将内容追加到 {result_file}")
        return True
    
    except Exception as e:
        print(f"追加到文件时发生错误: {e}")
        return False


def main():
    """主函数：按1-2-3顺序进行函数调用"""
    
    # 解析命令行参数
    if len(sys.argv) < 3:
        print("用法: python describe_images.py <起始行号> <结束行号>")
        print("示例: python describe_images.py 1 10")
        sys.exit(1)
    
    try:
        start_line = int(sys.argv[1])
        end_line = int(sys.argv[2])
    except ValueError:
        print("错误：行号必须是整数")
        sys.exit(1)
    
    if start_line < 1 or end_line < 1:
        print("错误：行号必须大于等于1")
        sys.exit(1)
    
    print(f"=== 开始处理第{start_line}行到第{end_line}行的图片 ===")
    
    # 步骤1：从all_images_list.txt获取对应区间的图片路径
    image_paths = get_image_paths_from_range(start_line, end_line)
    
    if not image_paths:
        print("未获取到任何图片路径")
        sys.exit(1)
    
    # 步骤2：调用codebuddy生成描述
    descriptions = call_codebuddy_for_images(image_paths)
    
    if not descriptions:
        print("未生成任何描述")
        sys.exit(1)
    
    # 步骤3：将结果追加到result.txt
    success = append_to_result(descriptions)
    
    if success:
        print(f"=== 处理完成，结果已保存到result.txt ===")
    else:
        print("=== 处理失败 ===")
        sys.exit(1)


if __name__ == "__main__":
    main()
