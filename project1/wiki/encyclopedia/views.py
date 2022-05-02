from django.http import HttpResponse
from django.shortcuts import render
import markdown2
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getpage(request, pagename):
    entryname = util.get_entry(pagename)
    if entryname is None:
        return render(request, "encyclopedia/notfound.html")
    else:
        html = markdown2.markdown_path(f"entries/{pagename}.md")
        return render(request, "encyclopedia/entry.html", {
        "content": markdown2.markdown(html),
        "title": pagename
        })

def search(request):
    if request.method == "GET":
        mysearch = request.GET.get("q")
        if util.get_entry(mysearch) is None:
            return render(request, "encyclopedia/search.html",{
                "mysearch": mysearch,
                "entries": util.list_entries()
            })

        else:
            return (getpage(request, mysearch))
   
def newpage(request):
    if request.method == "POST":
        content = request.POST.get("newpagecontent")
        title = request.POST.get("pagetitle")
        if title in util.list_entries():
            return render(request, "encyclopedia/newpage.html", {
                "page": "New Page",
                "pagetitle": title,
                "pagecontent": content,
                "error": True,
                "urlpage": "newpage"
            })
        util.save_entry(title, content)
        return getpage(request, title)   
    return render(request, "encyclopedia/newpage.html", {
        "page": "New Page",
        "newpage": True
    })

def editpage(request, pagetitle):
    if request.method == "POST":
        content = request.POST.get("newpagecontent")
        title = request.POST.get("pagetitle")
        util.save_entry(title, content)
        return getpage(request, title)
    return render(request, "encyclopedia/newpage.html", {
        "page": "Edit Page",
        "pagetitle": pagetitle,
        "pagecontent": util.get_entry(pagetitle),
    }) 

def randompage(request):
    return getpage(request, random.choice(util.list_entries()))