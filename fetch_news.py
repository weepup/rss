import feedparser
import requests

# 1. 抓取 Google News 的 QQQ 资讯
rss_url = "https://news.google.com/rss/search?q=%28%22QQQ%22+OR+%22Invesco+QQQ%22+OR+%22Nasdaq+100%22%29+ETF&hl=en-US&gl=US&ceid=US:en"
feed = feedparser.parse(rss_url)

if feed.entries:
    latest = feed.entries[0]
    title = latest.title
    link = latest.link

    # 2. 组装发往 Server酱的内容
    title_msg = "🚨 QQQ 财经快讯"
    desp_msg = f"**标题**: {title}\n\n[点击查看原文链接]({link})"

    # 3. 将你的 Server酱 SendKey 填在下方双引号内
    send_key = "SCT427439TtPBYqnM16986TLMZq30QGCIt"

    if send_key and send_key != "请把你的Server酱SendKey粘贴到这里":
        url = f"https://sctapi.ftqq.com/{send_key}.send"
        payload = {
            "title": title_msg,
            "desp": desp_msg
        }
        response = requests.post(url, data=payload)
        print("发送结果:", response.text)
    else:
        print("错误：请先填入你的 Server酱 SendKey")
else:
    print("暂时没有抓取到新闻")