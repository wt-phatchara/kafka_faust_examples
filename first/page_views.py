import faust

# Initialize the Faust app
app = faust.App(
    'page_views',
    broker='kafka://localhost:9092',
    topic_partitions=4,
)

# Define the structure of a page view event
class PageView(faust.Record):
    id: str
    user: str

# Topics
page_view_topic = app.topic('page_views', value_type=PageView)
page_view_count_topic = app.topic('page_view_counts')

# Table to maintain the count of views per page
page_views = app.Table('page_views', default=int)

# Agent to consume and process page views
@app.agent(page_view_topic)
async def count_page_views(views):
    async for view in views.group_by(PageView.id):
        # Increment the count for the specific page ID
        page_views[view.id] += 1

        # Create a JSON-like dictionary for the count message
        count_message = {
            "id": view.id,
            "count": page_views[view.id]
        }

        # Send the JSON message to the page_view_count_topic
        await page_view_count_topic.send(value=count_message)

if __name__ == '__main__':
    app.main()