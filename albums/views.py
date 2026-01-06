from django.shortcuts import render

def index(request):
    albums = [
        {
            "id": "album1",
            "title": "Summer 2024",
            "cover": "https://picsum.photos/seed/s1/400/260",
            "photos": [f"https://picsum.photos/seed/s1{i}/800/600" for i in range(1,7)]
        },
        {
            "id": "album2",
            "title": "Family Day",
            "cover": "https://picsum.photos/seed/f1/400/260",
            "photos": [f"https://picsum.photos/seed/f2{i}/800/600" for i in range(1,5)]
        },
        {
            "id": "album3",
            "title": "Nature Walks",
            "cover": "https://picsum.photos/seed/n1/400/260",
            "photos": [f"https://picsum.photos/seed/n3{i}/800/600" for i in range(1,6)]
        },
    ]
    return render(request, "albums/index.html", {"albums": albums})