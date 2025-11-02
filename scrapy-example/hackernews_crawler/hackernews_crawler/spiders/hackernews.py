import scrapy
from urllib.parse import urljoin


class HackernewsSpider(scrapy.Spider):
    name = "andyscrawler"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com"]

    max_listing_pages = 2
    max_threads_to_follow = 6

    listing_pages_seen = 0
    threads_followed = 0

    def parse(self, response):
        self.listing_pages_seen += 1

        for row in response.css("tr.athing"):
            story_id = row.attrib.get("id")

            title_node = row.css(".titleline a:first-child")
            title = title_node.css("::text").get(default="").strip()
            url = title_node.attrib.get("href", "").strip()

            subtext_row = row.xpath("following-sibling::tr[1]")
            comments_rel = subtext_row.css("a[href^='item?id=']::attr(href)").get()

            if story_id and title and url:
                yield {
                    "type": "story",
                    "story_id": story_id,
                    "title": title,
                    "url": url,
                    "source": "hackernews",
                }

            if (
                comments_rel
                and self.threads_followed < self.max_threads_to_follow
            ):
                self.threads_followed += 1

                yield response.follow(
                    comments_rel,
                    callback=self.parse_discussion,
                    cb_kwargs={
                        "story_id": story_id,
                        "story_title": title,
                        "story_url": url,
                    },
                )

        if self.listing_pages_seen < self.max_listing_pages:
            more_link = response.css("a.morelink::attr(href)").get()
            if more_link:
                yield response.follow(more_link, callback=self.parse)

    def parse_discussion(self, response, story_id, story_title, story_url):
        comment_nodes = response.css(".commtext")
        comment_count = len(comment_nodes)

        yield {
            "type": "discussion",
            "story_id": story_id,
            "story_title": story_title,
            "story_url": story_url,
            "discussion_url": response.url,
            "comment_count": comment_count,
        }
