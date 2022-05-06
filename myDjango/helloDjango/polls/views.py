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

@csrf_exempt
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
        <form action = "/create/save" method="get">
            <p><input type="text" placehold="title" name="title"></p>
            <p><input type="textarea" placehold="body" name="body"></p>
            <button type="submit">제출</button>
        </form>
        """
        return HttpResponse(HTMLTemplate(article))
    elif(req.method == "POST"):
        global nextId
        print(req.POST['title'], req.POST['body'])
        newTopic = {"id":nextId, "title": req.POST['title'], "body" : req.POST['body']}
        topics.append(newTopic)
        url = "/read/" + str(nextId) +"/"
        nextId+=1
    # redirect X
        # return HttpResponse()
    # redirect 상태 코드 301
        return redirect(url)
    # redirect 상태 코드 변경
        # response = HttpResponse(status=302)
        # response['Location'] = url
        # return response

# Get방식으로도 redirect만 제대로 해주면 상관없음
# def save(req):
#         global nextId
#         print(req.GET['title'], req.GET['body'])
#         newTopic = {"id":nextId, "title": req.GET['title'], "body" : req.GET['body']}
#         topics.append(newTopic)
#         url = "/read/" + str(nextId) +"/"
#         nextId+=1
#         response = HttpResponse(status=302)
#         response['Location'] = url
#         return response
        
def read(req, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f"<h2>{topic['title']}</h2>{topic['body']}"
    return HttpResponse(HTMLTemplate(article))
