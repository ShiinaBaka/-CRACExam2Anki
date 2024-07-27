import re
import os
import random
import chardet
import base64

def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"警告：找不到图片文件 {image_path}")
        return None

def shuffle_options(options):
    option_list = re.findall(r'\[([A-D])\](.*?)(?=\[[A-D]\]|\Z)', options, re.DOTALL)
    random.shuffle(option_list)
    shuffled_options = ''
    correct_answer = ''
    for i, (letter, content) in enumerate(option_list):
        new_letter = chr(65 + i)
        shuffled_options += f'{new_letter}. {content.strip()}<br>'
        if letter == 'A':
            correct_answer = f'{new_letter}. {content.strip()}'
    return shuffled_options.strip(), correct_answer

def convert_to_anki(input_text, image_folder):
    questions = re.split(r'\[I\]', input_text)
    
    anki_cards = []
    
    for question in questions:
        if question.strip():
            match = re.search(r'(LK\d+)\n\[Q\](.*?)(\[A\].*?)(\[P\](.*?))?$', question, re.DOTALL)
            if match:
                number, q, options, _, image_file = match.groups()
                
                q = q.strip()
                shuffled_options, correct_answer = shuffle_options(options.strip())
                
                front = f"{number}<br><br>{q}<br><br>{shuffled_options}"
                back = f"正确答案: {correct_answer}"
                
                # 检查是否有图片
                if image_file:
                    image_file = image_file.strip()
                    image_path = os.path.join(image_folder, image_file)
                    image_data = encode_image(image_path)
                    if image_data:
                        front += f'<br><img src="data:image/jpeg;base64,{image_data}">'
                
                anki_cards.append(f"{front}\t{back}")
    
    random.shuffle(anki_cards)
    return "\n".join(anki_cards)

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    return chardet.detect(raw_data)['encoding']

# 询问用户输入文件路径
input_file = input("请输入题库文件的路径：").strip('"').strip("'")
image_folder = input("请输入图片文件夹的路径：").strip('"').strip("'")

# 规范化路径
input_file = os.path.normpath(input_file)
image_folder = os.path.normpath(image_folder)

# 检查文件是否存在
if not os.path.exists(input_file):
    print(f"错误：题库文件不存在。请检查文件路径是否正确。路径：{input_file}")
elif not os.path.exists(image_folder):
    print(f"错误：图片文件夹不存在。请检查文件夹路径是否正确。路径：{image_folder}")
else:
    # 检测文件编码
    file_encoding = detect_encoding(input_file)
    print(f"检测到文件编码为: {file_encoding}")

    # 读取输入文件
    try:
        with open(input_file, 'r', encoding=file_encoding) as file:
            input_text = file.read()

        # 转换内容
        anki_content = convert_to_anki(input_text, image_folder)

        # 生成输出文件名
        output_file = os.path.splitext(input_file)[0] + "_anki_with_images.txt"

        # 将结果写入新文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(anki_content)

        print(f"转换完成。结果已保存到 {output_file}")
        print("您可以直接将此文件导入到Anki中。")
    except UnicodeDecodeError:
        print("无法自动检测文件编码。请尝试手动指定编码，常见的编码有 'utf-8', 'gbk', 'gb2312', 'ascii'等。")
        manual_encoding = input("请输入文件编码：")
        
        try:
            with open(input_file, 'r', encoding=manual_encoding) as file:
                input_text = file.read()
            
            # 转换内容
            anki_content = convert_to_anki(input_text, image_folder)

            # 生成输出文件名
            output_file = os.path.splitext(input_file)[0] + "_anki_with_images.txt"

            # 将结果写入新文件
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(anki_content)

            print(f"转换完成。结果已保存到 {output_file}")
            print("您可以直接将此文件导入到Anki中。")
        except UnicodeDecodeError:
            print("无法读取文件。请确保指定了正确的编码。")

# 在脚本结束时，打印出图片文件夹中的所有文件
print("\n图片文件夹中的文件：")
for file in os.listdir(image_folder):
    print(file)