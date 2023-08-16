from simple_image_download import simple_image_download as simp

response = simp.simple_image_download()

keywords = ["uppercut", "jab"]
# fighters =  ["MMA Fighter", "UFC Fighter", "Bellator Fighter"]

# for fighter in fighters:
#     for keyword in keywords:
#         response.download(f"{fighter} {keyword}", 15)

for keyword in keywords:
    response.download(keyword, 30)

# l = [f +" "+ k for f in fighters for k in keywords]

# response.download(l, 15)