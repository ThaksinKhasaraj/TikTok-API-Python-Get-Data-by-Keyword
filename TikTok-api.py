from TikTokApi import TikTokApi

with TikTokApi() as api:
    # get keyword by tag
    tag = api.hashtag(name="Thailand")

    print(tag.info())

    for video in tag.videos(count=10000):
        print(video.as_dict)