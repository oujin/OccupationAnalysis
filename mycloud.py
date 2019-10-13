from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread 
import random

words = []
with open('data/skills.txt', 'r', encoding='utf-8') as f:
    # e.g. "'SQL' 100"
    line = f.readline()
    while line:
        items = line.split()
        words += [items[0].replace("'", '')] * int(items[1])
        line = f.readline()
random.shuffle(words)
text = ' '.join(words)
# # 背景掩模
color_mask = imread('src/bigdata.jpg')
wc = WordCloud(
    font_path="msyh.ttc",
    background_color="white",
    max_words=2000,
    mask=color_mask,
    max_font_size=500,
    random_state=10
)
image_colors = ImageColorGenerator(color_mask)
my_wordcloud = wc.generate(text)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.axis('off')
plt.show()
