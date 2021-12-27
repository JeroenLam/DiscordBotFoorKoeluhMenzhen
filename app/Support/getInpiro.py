import urllib.request, os

# Function to download url data
def download(URL):
    # Imitating firefox
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
    # Scraping html page for new link
    request = urllib.request.Request(URL, headers = headers)
    return urllib.request.urlopen(request)
    
# Download image to ./inspiro.jpg
def getInspiro():
    # Storing path to Temp folder
    tempDir = os.path.join(os.path.dirname(__file__), '../Temp/')

    html = download('https://inspirobot.me/api?generate=true').read()
    link = str(html).strip('b').strip("'")  # Stripping link
    data = download(link)   # Downloading image
    with open(tempDir + 'inspiro.jpg','wb') as output:
        output.write(data.read()) # Write image
        
def getInspiroXmas():
    # Storing path to Temp folder
    tempDir = os.path.join(os.path.dirname(__file__), '../Temp/')

    html = download('https://inspirobot.me/api?generate=true&season=xmas').read()
    link = str(html).strip('b').strip("'")  # Stripping link
    data = download(link)   # Downloading image
    with open(tempDir + 'inspiroXmas.jpg','wb') as output:
        output.write(data.read()) # Write image
        
        
# Download mps to ./inspiro.mp3
def getInspiroMP3():
    # Storing path to Temp folder
    tempDir = os.path.join(os.path.dirname(__file__), '../Temp/')

    # Downlaod and procces the page to optain the link
    html = download('https://inspirobot.me/api?generateFlow=1&sessionID=7ee2dc54-f836-485e-a4be-abc8f49ed0e6').read()
    link = str(html).strip('b').strip("'")  # Stripping link
    # convert the website body to a dictionary, this sometimes trows, hence exception for retying
    try:
        link = eval(link) 
    except :
        getInspiroMP3()
        return
    # Download and write data to file    
    data = download(link['mp3'])   # Downloading mp3
    with open(tempDir + 'inspiro.mp3','wb') as output:
        output.write(data.read()) # Write mp3
