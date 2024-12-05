from bs4 import BeautifulSoup
from project import get_wikipedia_url, fetch_page_content, extract_table_data

def test_get_wikipedia_url(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'https://en.wikipedia.org/wiki/Python_(programming_language)')
    assert get_wikipedia_url() == 'https://en.wikipedia.org/wiki/Python_(programming_language)'

def test_fetch_page_content():
    url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    content = fetch_page_content(url)
    assert content is not None

def test_extract_table_data():
    # Assuming you have a sample HTML table to use for testing
    sample_html = '''
    <table class="wikitable">
        <tr><th>Header1</th><th>Header2</th></tr>
        <tr><td>Data1</td><td>Data2</td></tr>
    </table>
    '''
    soup = BeautifulSoup(sample_html, "html.parser")
    table = soup.find("table", {"class": "wikitable"})
    df = extract_table_data(table)
    assert not df.empty
    assert df.columns.tolist() == ['Header1', 'Header2']
    assert df.iloc[0].tolist() == ['Data1', 'Data2']