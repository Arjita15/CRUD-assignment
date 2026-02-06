from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

# CREATE + READ ALL
def home(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")   # refresh safely
    else:
        form = NoteForm()

    notes = Note.objects.all().order_by("-created_at")
    return render(request, "home.html", {"form": form, "data": notes})


# READ ONE
def read_one(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, "read_note.html", {"data": note})


# UPDATE
def update_one(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NoteForm(instance=note)

    return render(request, "update_note.html", {"form": form})


# DELETE
def delete_one(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == "POST":
        note.delete()
        return redirect("home")

    return render(request, "delete_note.html", {"data": note})