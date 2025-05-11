#---------------------------------------------------------
# Name: Winston Yamanaka
# File Creation Date: 2025-05-08
# Last Edit Date: 2025-05-08
# Description: Py-Strings
#              playing with text and string tools :P
#---------------------------------------------------------

# 1. putting a paragraph into a variable (looked up an essay about transformers)
text = "Evaluation of the movie: “Transformers” When I was a child, I just to watch TV for about one or two hours, and I remember that my brothers were always there, watching the animated series “Transformers”. At that time, I didn’t like really much those series. But I had to watch it because of my brothers. Then we grew up, and never watch those kinds of series again, until 2007, when a movie about those caricatures came out to the theater. My brothers and I went to watch the movie, and I just liked it, because there were good actors, the time and plot combined were good, and I loved the genres that it contains. I decided to evaluate this movie, because my brothers, my nephew and I have watched it many times. The movie “Transformers” was released on July 3rd, 2007, the director was Michael Bay, the studios were DreamWorks and Paramount Pictures, and the primary actors and actresses were: Shia LaBeouf, Megan Fox, Anthony Anderson, Josh Duhamel, and Tyrese Gibson. The genre is: Action/Adventure, Science Fiction/Fantasy adaptation, and war. The plot of the movie is: The earth is caught on the middle of an intergalactic war between two races of robots, the heroics Autobots and the evil Decepticons, which are able to change into a variety of objects, including cars, trucks, planes and other technological creations (yahoo, 2007). As I said, I went to the theater to watch this movie, and I thought that it was going to have actors that were well known. But then the movie begun and I realized that I didn’t know many of them, like Shia LaBeouf, and Megan Fox, so I expected that the movie would not be good. As the movie went on, and I discovered that the actors and actresses were good, they worked great together, and people liked them. They were professionals, and acted really great. After that, one of my brothers told me that they had already acted on other movies. So I went to the internet and I found out that the actors of this movie, and some other young"

# 2. count how many e's
e_count = text.count("e")
print("Letter 'e' count:", e_count)

# 3. count how many b's
b_count = text.count("b")
print("Letter 'b' count:", b_count)

# 4. print 20 characters after the first e
first_e = text.find("e")  # get the position of the first e
after_e = text[first_e+1:first_e+21]  # 20 characters after that
print("20 chars after first e:", after_e)

# 4 (again). count words (split by space)
words = text.split()
print("Number of words:", len(words))

# 5. count how many sentences (roughly use . ! ? as endings)
import re
sentences = re.split(r'[.!?]', text)
# remove empty strings and trim
sentences = [s.strip() for s in sentences if s.strip() != '']
print("Number of sentences:", len(sentences))

# 6. find shortest sentence
shortest = min(sentences, key=len)
print("Shortest sentence:", shortest)

# 7. count UNIQUE words (ignore punctuation and case)
words_cleaned = [re.sub(r'[^\w]', '', w).lower() for w in words]
unique_words = set(words_cleaned)
print("Number of unique words:", len(unique_words))

# 7 (again). capitalize every h
text_h_caps = text.replace("h", "H")
print("Text with all h's capitalized (first 300 chars only):")
print(text_h_caps[:300])  # only show part to keep output short
