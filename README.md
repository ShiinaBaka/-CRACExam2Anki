
# CRACExam2Anki

This script converts the exam question bank for the Amateur Radio Operator Certificate, published by the Chinese Radio Amateur Club (CRAC), into Anki card format.

## Features

- Reads and parses questions, options, and images.
- Randomizes the order of options.
- Embeds images in Base64 format into the questions.

## Requirements

- Python 3.x
- `chardet` library

Install the `chardet` library with the following command:
```sh
pip install chardet
```

## Usage

1. Prepare a text file containing questions and image filenames. Refer to the provided question bank file for the example format.
2. Place the text file and images in the same directory.
3. Run the script and input the path to the question bank file and the image folder:
    ```sh
    python 1.py
    ```
4. The script will generate a new file with the suffix `_anki_with_images.txt` in the same directory.
5. Import the generated file into Anki.

## Example

**Input File Example:**

Question with an image:
```
[I] LK0510
[Q] What does the symbol of the circuit component in the attached image represent?
[A] Junction field-effect transistor (JFET)
[B] PNP bipolar junction transistor (BJT)
[C] NPN bipolar junction transistor (BJT)
[D] Insulated-gate field-effect transistor (IGFET)
[P] LK0510.jpg
```

Question without an image:
```
[I] LK0001
[Q] What is the highest legal document specifically for radio management in China, and its legislative body?
[A] Radio Regulations of the People's Republic of China, State Council and Central Military Commission
[B] Radio Management Measures of the People's Republic of China, Ministry of Industry and Information Technology
[C] Telecommunications Regulations of the People's Republic of China, State Council
[D] Amateur Radio Station Management Measures of the People's Republic of China, Ministry of Industry and Information Technology
[P]
```

**Output File Example:**
```
LK0510<br><br>What does the symbol of the circuit component in the attached image represent?<br><br>[A] Junction field-effect transistor (JFET)<br>[B] PNP bipolar junction transistor (BJT)<br>[C] NPN bipolar junction transistor (BJT)<br>[D] Insulated-gate field-effect transistor (IGFET)<br><br><img src="data:image/jpeg;base64,..."><tab>Correct answer: [A] Junction field-effect transistor (JFET)
LK0001<br><br>What is the highest legal document specifically for radio management in China, and its legislative body?<br><br>[A] Radio Regulations of the People's Republic of China, State Council and Central Military Commission<br>[B] Radio Management Measures of the People's Republic of China, Ministry of Industry and Information Technology<br>[C] Telecommunications Regulations of the People's Republic of China, State Council<br>[D] Amateur Radio Station Management Measures of the People's Republic of China, Ministry of Industry and Information Technology<br><tab>Correct answer: [A] Radio Regulations of the People's Republic of China, State Council and Central Military Commission
```

## Notes

- Ensure that the image files are in the specified folder and that the paths are correct.
- If encoding detection fails, you can manually specify the file encoding.

## Additional Information

This script is used to convert the exam question bank for the Amateur Radio Operator Certificate published by the Chinese Radio Amateur Club (CRAC) into Anki cards. The question bank can be downloaded from the [CRAC website](http://www.crac.org.cn/News/Detail?ID=3dbd1bc7f36443958e1872234f42464f).

## Copyright Notice

The question bank is copyrighted by the Chinese Radio Amateur Club (CRAC).

## License

This script is licensed under the MIT License.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---
