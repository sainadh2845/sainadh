import streamlit as st
import requests

def get_wikipedia_search_results(search_term):
    endpoint = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': search_term,
        'format': 'json'
    }
    response = requests.get(endpoint, params=params)
    return response.json()['query']['search'][:3]

st.title('Wikipedia Search App')


search_term = st.text_input('Enter a search element:', '')
if st.button('Enter'):
    if search_term:

        results = get_wikipedia_search_results(search_term)

        for result in results:
            title = result['title']
            snippet = result['snippet']
            url = f"https://en.wikipedia.org/?curid={result['pageid']}"

    
            st.markdown(f"### {title}")
            st.markdown(snippet)
    else:
        st.error('Please enter a search element.')
