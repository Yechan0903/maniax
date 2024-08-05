from django.shortcuts import render, redirect
import uuid, json, requests, re, time
from .forms import ImageUploadForm
from django.conf import settings

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            image_file = uploaded_image.image.file
            extracted_texts = extract_text(image_file)
            formatted_texts = parse_text(extracted_texts)
            top3_formatted_texts = formatted_texts[:3]
            top_apps = split_formatted_texts(top3_formatted_texts)
            
            request.user.top_apps = top_apps
            request.user.save()
            
            return redirect('rankings')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form':form})

def extract_text(image_file):
    request_json = {
        'images': [
            {
                'format': 'jpg',
                'name': 'demo'
            }
        ],
            'requestId': str(uuid.uuid4()),
            'version': 'V2',
            'timestamp': int(round(time.time() * 1000))
        }

    payload = {'message': json.dumps(request_json).encode('UTF-8')}
    files = [
            ('file', image_file)
        ]

    headers = {
            'X-OCR-SECRET': settings.OCR_SECRET_KEY
        }

    response = requests.request("POST", settings.OCR_API_URL, headers=headers, data = payload, files = files)
    
    if response.status_code == 200:
        ocr_results = response.json()
        all_texts = []
        for image in ocr_results['images']:
            for field in image['fields']:
                text = field['inferText']
                all_texts.append(text)
    else:
        all_texts = []
    
    print(all_texts)
    return(all_texts)

def parse_text(extracted_texts):
    exclude_set = {'>', 'M', 'TALK'}
    filtered_texts = [text for text in extracted_texts if text not in exclude_set]
    
    text_results = " ".join(filtered_texts)
    pattern = re.compile(r'(\w+ \w+|\w+|카카오톡 TALK|TheDayBefore) (\d+시간 \d+분|\d+분)')
    matches = pattern.findall(text_results) 
    
    formatted_texts = []
    for match in matches:
        app, time = match
        formatted_texts.append(f"{app} {time}")
    print(formatted_texts)
    return formatted_texts

def split_by_time(text):
    time_pattern = re.compile(r'(\d+시간)')
    minute_pattern = re.compile(r'(\d+분)')
    
    if time_pattern.search(text):
        parts = time_pattern.split(text)
        if len(parts) == 3:
            return parts[0], parts[1]+parts[2]
        elif len(parts) == 2:
            return parts[0], parts[1]
    else:
        # '시간' 패턴이 없으면 '분' 패턴을 기준으로 나누기
        parts = minute_pattern.split(text)
        return parts[0], parts[1]
    
    return text, ""

def split_formatted_texts(texts):
    split_texts = []
    for text in texts:
        part1, part2 = split_by_time(text)
        split_texts.append((part1.strip(), part2.strip()))
    return split_texts
        
        
    



