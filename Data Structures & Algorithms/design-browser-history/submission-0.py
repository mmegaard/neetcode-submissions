class Page:
    def __init__(self, url="", back=None, forward=None):
        self.url = url
        self.back = back
        self.forward = forward

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Page(homepage)
        self.current_page = self.homepage

    def visit(self, url: str) -> None:
        new_url = Page(url)
        new_url.back = self.current_page
        self.current_page.forward = new_url
        self.current_page = new_url

    def back(self, steps: int) -> str:
        current_page = self.current_page
        while steps > 0 and current_page.back != None:
            steps -= 1
            current_page = current_page.back
        self.current_page = current_page
        return self.current_page.url
    
    def forward(self, steps: int) -> str:
        current_page = self.current_page
        while steps > 0 and current_page.forward != None:
            steps -= 1
            current_page = current_page.forward
        self.current_page = current_page
        return self.current_page.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)