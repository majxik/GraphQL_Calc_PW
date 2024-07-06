#Author: Martin Maiksnar
#This is the page object for the query page

class QueryPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("http://localhost:4000/")

    def perform_query(self, query):
        response = self.page.evaluate(f"""() => {{
            return fetch("http://localhost:4000/", {{
                method: "POST",
                headers: {{ "Content-Type": "application/json" }},
                body: JSON.stringify({{ query: "{query}" }})
            }}).then(response => response.json().then(json => ({{
                status: response.status,
                data: json
            }})));
        }}""")
        return response