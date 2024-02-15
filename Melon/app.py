from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://www.melon.com/chart/index.htm"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('table > tbody > tr')
    
    top100 = []

    for tr in trs:
        title = tr.select_one('.rank01 > span > a').text
        artist = tr.select_one('.rank02 > a').text
        image = tr.select_one('img')['src']
        top100.append({
            'title': title,
            'artist': artist,
            'image': image,
        })

    return render_template('index.html', data=top100)

if __name__ == '__main__':  
    app.run(debug=True)