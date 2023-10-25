import tkinter as tk
import feedparser

class CybersecurityNewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity News Filter")

        # User input field for filtering
        self.filter_entry = tk.Entry(root, width=40)
        self.filter_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.filter_entry.insert(0, "Enter keywords to filter news")

        # Filter button
        filter_button = tk.Button(root, text="Filter", command=self.filter_news)
        filter_button.grid(row=0, column=2, padx=10, pady=10)

        # Window to display filtered news articles
        self.news_list = tk.Listbox(root, width=60, height=15)
        self.news_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Label for the list
        label = tk.Label(root, text="Filtered News")
        label.grid(row=2, column=0, columnspan=3)

    def filter_news(self):
        keywords = self.filter_entry.get()
        self.news_list.delete(0, tk.END)
        
        # Uses feedparser to go to the RSS feed we want to get information from.
        rss_feed = feedparser.parse('https://www.cisa.gov/news.xml')

        for entry in rss_feed.entries:
            title = entry.title
            link = entry.link

            # Access the publication date
            pub_date = entry.published

            if keywords.lower() in title.lower() or keywords.lower():
                self.news_list.insert(tk.END, title)
                self.news_list.insert(tk.END, f"Published: {pub_date}")
                self.news_list.insert(tk.END, f"Link: {link}")
                self.news_list.insert(tk.END, '')

def main():
    root = tk.Tk()
    app = CybersecurityNewsApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
