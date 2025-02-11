import re
from urllib.parse import urljoin
import html2text

def img_tag2url(soup, url):
    # 모든 이미지 태그에 대해 외부 이미지 URL을 마크다운 형식으로 변환
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if img_url:
            # 외부 이미지 URL이 절대 URL일 경우, 마크다운 형식으로 변환
            if img_url.startswith("http"):  # 절대 URL인 경우
                # 이미지를 HTML 형식으로 유지 (마크다운을 원하면 아래 코드 사용)
                img_tag.replace_with(f'<img src="{img_url}" />')
            else:  # 상대 경로인 경우, 절대 URL로 변환
                absolute_url = urljoin(url, img_url)
                img_tag.replace_with(f'<img src="{absolute_url}" />')
    return soup
    

def remove_button(soup):
    for button in soup.find_all('button'):
        button.decompose()
    return soup


def cut_content(html_content):
    index = html_content.find('<h1>')
    html_content = html_content[index:]

    index = html_content.find('<h2>출처</h2>')
    html_content = html_content[:index]
    index = html_content.find('<div class="margin-bottom-20">')
    html_content = html_content[:index]

    index = html_content.find('<div class="col-md-12">')
    html_content = html_content[index:]

    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    return html_content


def remove_blank(soup):
    pre_tag = []
    html_content = str(soup)
    num = html_content.count('sample-input')
    for i in range(1, num+1):
        tg = soup.find('pre', {'id': f'sample-input-{i}'})
        if tg:
            pre_tag.append(tg)
        tg = soup.find('pre', {'id': f'sample-output-{i}'})
        if tg:
            pre_tag.append(tg)


    for tg in pre_tag:
        original_text = tg.get_text()
        original_text = str(original_text)
        modified_text = original_text.replace("\r\n","\n")

        tg.string = modified_text

    return soup


def extract_img_url(soup, url):
    # 모든 이미지 태그에 대해 외부 이미지 URL을 마크다운 형식으로 변환
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if img_url:
            # 외부 이미지 URL이 절대 URL일 경우, 마크다운 형식으로 변환
            if img_url.startswith("http"):  # 절대 URL인 경우
                img_tag.replace_with(f'![image]({img_url})')
            else:  # 상대 경로인 경우, 절대 URL로 변환
                absolute_url = urljoin(url, img_url)
                img_tag.replace_with(f'![image]({absolute_url})')
    
    # HTML을 마크다운 형식으로 변환
    h = html2text.HTML2Text()
    h.ignore_links = False  # 링크를 마크다운 형식으로 변환
    image_url = h.handle(str(soup))

    # 자르기
    index = image_url.find('![image]')
    image_url = image_url[index:]

    index = image_url.find('svg')
    image_url = image_url[:index +4]
    image_url = image_url[9:-1]
    return image_url


def sanitize_folder_name(folder_name):
    """
    폴더 이름에서 사용할 수 없는 특수문자를 제거합니다.
    """
    # Windows에서 허용되지 않는 특수문자
    invalid_chars = r'[\\/:*?"<>|]'
    
    # 정규식을 이용해 특수문자 제거
    sanitized_name = re.sub(invalid_chars, '', folder_name)
    
    return sanitized_name
