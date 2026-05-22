import os
import re

def get_image_set(file_path):
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}

def extract_filenames_from_result(result_path):
    if not os.path.exists(result_path):
        return set()
    filenames = set()
    pattern = re.compile(r'【([^】]+)】')
    with open(result_path, 'r', encoding='utf-8') as f:
        for line in f:
            matches = pattern.findall(line)
            for item in matches:
                filename = os.path.basename(item.strip())
                filenames.add(filename)
    return filenames

def main():
    output_file = 'images_remaining.txt'

    all_images = get_image_set('images_list_lite.txt')
    processed_filenames = extract_filenames_from_result('result.txt')

    remaining = []
    for path in sorted(all_images):
        basename = os.path.basename(path)
        if basename not in processed_filenames:
            print(path)
            remaining.append(path)

    with open(output_file, 'w', encoding='utf-8') as f:
        for path in remaining:
            f.write(path + '\n')

    print(f"Total images in list: {len(all_images)}")
    print(f"Already processed: {len(processed_filenames)}")
    print(f"Remaining to process: {len(remaining)}")
    print(f"Result saved to: {output_file}")

if __name__ == '__main__':
    main()
