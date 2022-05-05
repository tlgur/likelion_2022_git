from pydoc_data.topics import topics
from urllib import response
from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics=[
    {'id': 1, 'title' : 'routing', 'body':'Routing is ...'},
    {'id': 2, 'title' : 'view', 'body':'View is ...'},
    {'id': 3, 'title' : 'Model', 'body':'Model is ...'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f"<li><a href =\"/read/{topic['id']}\">{topic['title']}</a></li>"
    return f"""
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
    </body>
    </html>
    """

def index(request):
    article = """
    <h2>Welcome</h2>
    Hello, Django
    <ul>
        <li><a href = "/create/">create</a></li>
    """
    print("response : " + str(response))
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(req):
    if(req.method == "GET"):
        article="""
        <h2>Create</h2>
        <form action = "/create/" method="post">
            <p><input type="text" placehold="title" name="title"></p>
            <p><input type="textarea" placehold="body" name="body"></p>
            <button type="submit">제출</button>
        </form>
        """
        return HttpResponse(HTMLTemplate(article))
    elif(req.method == "POST"):
        global nextId
        newTopic = {"id":nextId, "title": req.POST['title'], "body" : req.POST['body']}
        topics.append(newTopic)
        url = "/read/" + str(nextId) +"/"
        nextId+=1
        response = HttpResponse(status=302)
        response['Location'] = url
        return response

        
def read(req, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f"<h2>{topic['title']}</h2>{topic['body']}"
    return HttpResponse(HTMLTemplate(article))
