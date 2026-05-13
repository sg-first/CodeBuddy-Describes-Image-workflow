import os

def remove_empty_lines(input_file, output_file=None):
    """
    去除 txt 文件中的空行
    
    Args:
        input_file: 输入的 txt 文件路径
        output_file: 输出的 txt 文件路径，如果为 None 则覆盖原文件
    """
    if not os.path.exists(input_file):
        print(f"文件不存在：{input_file}")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    non_empty_lines = [line for line in lines if line.strip()]
    
    output_path = output_file if output_file else input_file
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(non_empty_lines)
    
    print(f"处理完成！共去除 {len(lines) - len(non_empty_lines)} 个空行")
    print(f"结果已保存到：{output_path}")

if __name__ == '__main__':
    input_file = r'result.txt'
    remove_empty_lines(input_file)
