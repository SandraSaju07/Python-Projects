import wikipedia as wiki

def search_topic(topic):
    """Search for a topic on Wikipedia"""
    try:
        return wiki.search(topic)
    except Exception as e:
        return f"Error searching topic: {e}"

def suggest_topic(phrase):
    """Search topics related to a phrase"""
    try:
        return wiki.suggest(phrase)
    except Exception as e:
        return f"Error suggesting topic: {e}"
    
def get_summary(topic, lang = 'en'):
    """Get the summary of a topic in a language"""
    try:
        wiki.set_lang(lang)
        return wiki.summary(topic)
    except Exception as e:
        return f"Error fetching summary: {e}"
    
def get_page_details(topic, lang = 'en'):
    """Retrieve details of a Wikipedia page"""
    try:
        wiki.set_lang(lang)
        page = wiki.page(topic)
        return {
            'title': page.title,
            'url': page.url,
            'content': page.content[:500], # Limiting content size
            'images': page.images[:5], # Limiting images to first 5
            'links': page.links[:10] # Limiting links to first 10
        }
    except Exception as e:
        return f"Error fetching page details: {e}"
    
if __name__ == "__main__":
    topic = "Python (programming language)"
    phrase = 'Pytho'
    lang = 'fr'

    print(f"\nSearching for {topic}: {search_topic(topic)}")
    print(f"\nSuggestion for {phrase}: {suggest_topic(phrase)}")

    print(f"\nSummary for {topic} in English: {get_summary(topic)}")
    print(f"\nSummary for {topic} in French: {get_summary(topic,lang)}")

    page_details = get_page_details(topic)
    print(f"\nPage Details")
    print(f"\nURL: {page_details['url']}")
    print(f"\nContent: {page_details['content']}")
    print(f"\nImages: {page_details['images']}")
    print(f"\nLinks: {page_details['links']}\n")