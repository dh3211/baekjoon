from functions import img_tag2url, remove_button, cut_content, extract_img_url,remove_blank, sanitize_folder_name
from bs4 import BeautifulSoup
import os
import shutil
import requests


def main():
    ##  connect problem URL
    problem_id = 15486


    url = f"https://www.acmicpc.net/problem/{problem_id}"
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/132.0.0.0\
                Safari/537.36'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        problem_title = soup.find('span', {'id': 'problem_title'}).decode_contents()
        soup = img_tag2url(soup, url)
        soup = remove_button(soup)
        html_content = str(soup)
        html_content = cut_content(html_content)
        html_content = remove_blank(soup, html_content)

    else:
        print(f"Failed to request the problem page. Status code: {response.status_code}")
        return


    ##  connect problem difficulty image URL
    url = f"https://solved.ac/search?query={problem_id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup_image = BeautifulSoup(response.text, 'html.parser')
        image_url = extract_img_url(soup_image, url)

        html_content = \
            f'''<h1>''' +\
            f'''<img src="{image_url[9:-1]}" style="height: 1em; vertical-align: middle;" />''' +\
            f'''  {problem_id}번 - {problem_title}</h1>''' +\
            f'''\n<br><br>\n''' + html_content
    
    else:
        print(f"Failed to request the difficulty image page. Status code: {response.status_code}")
        return


    ##  create problem folder
    folder_name = '0'*(5- len(str(problem_id))) +f'{problem_id}' +f' - {problem_title}'
    folder_name = sanitize_folder_name(folder_name)
    folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"'{folder_path}' 폴더가 생성되었습니다.")
    else:
        print(f"'{folder_path}' 폴더가 이미 존재합니다.")


    ##   create md file
    md_path = os.path.join(folder_path, f'{problem_id}.md')

    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(html_content)
    print("create md file!")


    ## create python form
    form_python = os.path.join(os.path.dirname(__file__), 'form_python.txt')
    py_path = os.path.join(folder_path, f'{problem_id}.py')
    if not os.path.exists(py_path):
        shutil.copy(form_python, py_path)
        print(f"create python file!")


    ##  create IO folder
    IOfolder_path = os.path.join(folder_path,"IO")
    if not os.path.exists(IOfolder_path):
        os.makedirs(IOfolder_path)


    ##  create IO text file
    num = html_content.count('sample-input')
    for i in range(1, num+1):
        pre_tag = soup.find('pre', class_='sampledata', id=f'sample-input-{i}')
        content = pre_tag.decode_contents()
        with open(os.path.join(IOfolder_path, f'{problem_id}_{i}_i.txt'), 'w', encoding='utf-8') as file:
            file.write(content)

        pre_tag = soup.find('pre', class_='sampledata', id=f'sample-output-{i}')
        content = pre_tag.decode_contents()
        with open(os.path.join(IOfolder_path, f'{problem_id}_{i}_o.txt'), 'w', encoding='utf-8') as file:
            file.write(content)

    print(f'{folder_name}' +" ...Done!")


if __name__ == "__main__":
    main()