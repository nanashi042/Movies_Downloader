from bs4 import BeautifulSoup
import requests

def get_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return BeautifulSoup(res.text, 'html.parser')

def moviename(movie_name):

    search_url = f"https://moviesnation.beauty/?s={movie_name}"
    soup = get_soup(search_url)

    movie_links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if 'moviesnation.beauty' in href and movie_name.split('+')[0].lower() in href.lower():
            movie_links.append(href)

    if not movie_links:
        print("❌ No movie found.")
        exit()

    main_url = movie_links[0]
    print(f"🎬 Found movie page: {main_url}")

    main_soup = get_soup(main_url)
    bollydrive_links = []
    for a in main_soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text(strip=True).lower()
        if 'bollydrive' in href and '1080' in text:
            bollydrive_links.append(href)

    else:
        print("⚠️ No 1080p BollyDrive links found.")

    return bollydrive_links

moviename("baaghi")