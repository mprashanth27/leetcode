class WebPage: #~ class ListNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = WebPage(homepage) # ~ Head in DLL
        self.currpage = self.homepage # a ptr //ar to Tail in DLL but not same

    def visit(self, url: str) -> None:
        new_webpg = WebPage(url)

        if (not self.homepage.next): # BrowserHistory empty, only initialized with homepage
            self.homepage.next = new_webpg
            new_webpg.prev = self.homepage
            self.currpage = new_webpg
        else: # BrowserHistory not empty
            new_webpg = WebPage(url) # Since, new_webpg.next = None, It clears up all the forward history.
            new_webpg.prev = self.currpage
            self.currpage = new_webpg

    def back(self, steps: int) -> str:
        if (not self.homepage.next): # BrowserHistory empty
            return self.homepage.url
        else:
            while (steps>0 and self.currpage.prev):
                self.currpage = self.currpage.prev # I'm just moving Curr pg ptr 1 step back, the fwd nodes(.next) shld still exist?
                steps -= 1
        return self.currpage.url # if steps = 0, just return currpg[nt tested here] else above while pt will takecare


    def forward(self, steps: int) -> str:
        if (not self.homepage.next): # BrowserHistory empty
            return self.homepage.url
        else:
            while (steps>0 and self.currpage.next):
                self.currpage = self.currpage.next # I'm just moving Curr pg ptr 1 step fwd, the bwd nodes(.prev) shld still exist?
                steps -= 1
        return self.currpage.url


# Your BrowserHistory object will be instantiated and called as such:
homepage = "leetcode.com"

obj = BrowserHistory(homepage)
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
obj.back(1)
obj.back(1)
obj.forward(1)
obj.visit("youtube.com")
obj.forward(1)
obj.back(1)
obj.back(1)