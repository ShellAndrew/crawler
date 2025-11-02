# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from urllib import urljoin
from scrapy.exceptions import DropItem


class HackernewsCrawlerPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        title = adapter.get("title")
        if not title:
            raise DropItem(f"Missing title for story {adapter.get('story_id')}")
        adapter["title"] = title.strip()

        raw_url = adapter.get("url", "")
        if raw_url:
            adapter["url"] = urljoin("https://news.ycombinator.com/", raw_url)

        discussion_url = adapter.get("discussion_url")
        if discussion_url:
            adapter["discussion_url"] = urljoin(
                "https://news.ycombinator.com/",
                discussion_url,
            )

        count_val = adapter.get("comment_count", 0)
        try:
            adapter["comment_count"] = int(count_val)
        except (TypeError, ValueError):
            adapter["comment_count"] = 0

        
        return item
