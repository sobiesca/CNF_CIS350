import tkinter as tk
import feedparser

class CybersecurityNewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity News Filter")

        # User input field of UI
        self.filter_entry = tk.Entry(root, width=40)
        self.filter_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.filter_entry.insert(0, "Enter keywords to filter news")

        # Filter button
        filter_button = tk.Button(root, text="Filter", command=self.filter_news)
        filter_button.grid(row=0, column=2, padx=10, pady=10)

        # Display area for RSS news information
        self.news_list = tk.Listbox(root, width=60, height=15)
        self.news_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Label for the filtered RSS news information
        label = tk.Label(root, text="Filtered News")
        label.grid(row=2, column=0, columnspan=3)

    def filter_news(self):
        keywords = self.filter_entry.get()
        self.news_list.delete(0, tk.END)
        
        # Uses feedparser to extract the data we want from the RSS feed we want to get information from
        rss_feed = feedparser.parse('https://www.cisa.gov/news.xml')

        for entry in rss_feed.entries:
            title = entry.title
            summary = entry.summary
            pub_date = entry.published
            link = entry.link

            # Adds information we wanted from the RSS feed and displays it in the UI
            if keywords.lower() in title.lower() or keywords.lower() in summary.lower():
                self.news_list.insert(tk.END, title)
                self.news_list.insert(tk.END, f"Summary: {summary}")
                self.news_list.insert(tk.END, f"Published: {pub_date}")
                self.news_list.insert(tk.END, f"Link: {link}")
                self.news_list.insert(tk.END, '')

def main():
    root = tk.Tk()
    app = CybersecurityNewsApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
