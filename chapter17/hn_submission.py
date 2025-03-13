from operator import itemgetter

import requests


# Make an API call and check the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")


# from operator import itemgetter
# import requests
# import matplotlib.pyplot as plt

# # Make an API call and check the response.
# url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# r = requests.get(url)
# print(f"Status code: {r.status_code}")

# # Process information about each submission.
# submission_ids = r.json()
# submission_dicts = []

# for submission_id in submission_ids[:10]:  # Fetch top 10 stories
#     # Make a new API call for each submission.
#     url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
#     r = requests.get(url)
#     print(f"id: {submission_id}\tstatus: {r.status_code}")
#     response_dict = r.json()
    
#     # Build a dictionary for each article.
#     submission_dict = {
#         'title': response_dict['title'],
#         'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
#         'comments': response_dict.get('descendants', 0),  # Handle missing comments
#     }
#     submission_dicts.append(submission_dict)

# # Sort the stories by number of comments.
# submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# # Prepare data for visualization.
# titles = [sub['title'] for sub in submission_dicts]
# comments = [sub['comments'] for sub in submission_dicts]

# # Plot the data.
# plt.figure(figsize=(10, 6))
# plt.barh(titles, comments, color='orange')
# plt.xlabel("Number of Comments")
# plt.ylabel("Article Title")
# plt.title("Top 10 Hacker News Stories by Comments")
# plt.gca().invert_yaxis()  # Highest values on top

# # Show the graph.
# plt.show()