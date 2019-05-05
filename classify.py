import re
from textstat.textstat import easy_word_set

def song_id(filename):
    pattern = re.compile(r'(\S+)~(\S+)~(\S+)[.]')
    match = pattern.match(filename)
    song_id = int(match.group(1))
    return song_id

def song_artist(filename):
    pattern = re.compile(r'(\S+)~(\S+)~(\S+)[.]')
    match = pattern.match(filename)
    artist_raw = match.group(2)
    artist = artist_raw.replace('-', ' ')
    return artist

def song_title(filename):
    pattern = re.compile(r'(\S+)~(\S+)~(\S+)[.]')
    match = pattern.match(filename)
    title_raw = match.group(3)
    title = title_raw.replace('-', ' ')
    return title

def kid_safe(lyrics):
    if lyrics == '[Instrumental]':
        return 0.5
    kid_count = 0
    bad_words = ['***', '****', '*****', 'a**', 'ass', 'asshole', 'b****', 'bitch', 'boner', 'boob', 'boobs', 'booty', 'butt', 'butthole', 'clit', 'clitoris', 'cock', 'cocks', 'cum', 'cumming', 'cunt', 'dick', 'erotic', 'fag', 'faggot', 'fingering', 'f***', 'fuck', 'fucked', 'fucker', 'fucking', 'fucks', 'genitals', 'hooker', 'jizz', 'juggs', 'kike', 'kill', 'killer', 'killers', 'killing', 'kink', 'kinky', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafuckin', 'negro', 'n****', 'nigga', 'nigger', 'nipple', 'nipples', 'nude', 'nudity', 'orgasm', 'orgy', 'paedophile', 'panties', 'panty', 'pedophile', 'penis', 'pissing', 'playboy', 'porn', 'porno', 'pornography', 'pubes', 'pussy', 'rape', 'raping', 'rapist','ruined', 'semen', 'sex', 'sexy', 's***', 'shit', 'slave', 'slaves', 'slut', 'tit', 'tits', 'titties', 'titty', 'topless', 'twat', 'vagina', 'whore', 'whores']
    for word in lyrics.split():
        if word.lower() in bad_words:
            kid_count += 1
    if kid_count == 0:
        return 1
    elif kid_count >= 10:
        return 0
    else:
        return 1 - kid_count / 10

def love(lyrics):
    if lyrics == '[Instrumental]':
        return 0.5
    love_count = 0
    love_words = ['adorable', 'adore', 'affection', 'amour', 'angel', 'bliss', 'caring', 'chocolate', 'companion', 'compassion', 'darling', 'dear', 'desire', 'fond', 'forever','habibi', 'heart', 'husband', 'intimacy', 'intimate', 'kiss', 'kisses', 'kissing', 'love', 'lover', 'loving', 'marriage', 'married', 'marry', 'passion', 'relationship', 'romance', 'romantic', 'sex', 'sweetheart', 'tender', 'warmth', 'wife']
    for word in lyrics.split():
        if word.lower() in love_words:
            love_count += 1
    if love_count == 0:
        return 0
    elif love_count >= 10:
        return 1
    else:
        return love_count / 10

def mood(lyrics):
    if lyrics == '[Instrumental]':
        return 0.5
    mood_count = 5 # Mood count initialized to neutral state
    positive_words = ['amazing', 'awesome', 'angelic', 'admire', 'appealing', 'attractive', 'beaming', 'brilliant', 'beautiful', 'bliss', 'bubbly', 'bravo', 'calm', 'cheery', 'cool', 'cute', 'celebrate', 'celebrated', 'charming', 'commend', 'dazzling', 'delight', 'divine', 'delightful', 'enchant', 'enchanting', 'easy', 'ecstatic', 'electric', 'elegant', 'energy', 'energetic', 'energized', 'exciting', 'excitement', 'enthusiastic', 'exquisite', 'fabulous', 'fantastic', 'flourish', 'flourishing', 'fortunate', 'fresh', 'friend', 'friends', 'friendly', 'fun', 'funny', 'generous', 'genuine', 'giving', 'glamorous', 'glowing', 'good', 'gorgeous', 'great', 'handsome', 'happy', 'heaven', 'heavenly', 'hug', 'ideal', 'impressive', 'jovial', 'joy', 'joyful', 'kind', 'laugh', 'light', 'lively', 'love', 'lovely', 'loving', 'lover', 'marvelous', 'nice', 'optimistic', 'optimism', 'paradise', 'perfect', 'perfection', 'positive', 'smile', 'sparkling', 'sunny', 'terrific', 'upbeat', 'vibrant', 'victory', 'wow', 'wonderful', 'zeal']
    negative_words = ['abysmal', 'angry', 'apathy', 'annoy', 'annoying', 'awful', 'bad', 'badly', 'boring', 'cold', 'collapse', 'cruel', 'damage', 'damaging', 'disease', 'dishonest', 'dirty', 'dead', 'deadly', 'disgusting', 'evil', 'fail', 'failure', 'failing', 'grim', 'hate', 'hatred', 'mean', 'malicious', 'monstrous', 'nasty', 'negative', 'pain', 'reject', 'sad', 'vicious', 'worthless']
    for word in lyrics.split():
        if word.lower() in positive_words:
            mood_count += 1
        elif word.lower() in negative_words:
            mood_count -= 1
    if mood_count >= 10:
        return 1
    elif mood_count <= 0:
        return 0
    else:
        return mood_count / 10

def length(lyrics):
    if lyrics == '[Instrumental]':
        return 0.5
    length_count = 0
    for word in lyrics.split():
        length_count += 1
    if length_count >= 475:
        return 1
    elif length_count <= 50:
        return 0
    else:
        return round(length_count / 500, 1)
        
def complexity(lyrics):
    if lyrics == '[Instrumental]':
        return 0.5
    complexity_set = set()
    for word in lyrics.split():
        if word.lower() not in easy_word_set:
            complexity_set.add(word)
    complexity_count = len(complexity_set)
    if complexity_count >= 95:
        return 1
    elif complexity_count <= 10:
        return 0
    else:
        return round(complexity_count / 100, 1)