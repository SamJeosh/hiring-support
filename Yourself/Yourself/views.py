from flask import Blueprint, render_template, flash, request, redirect, url_for
from . import db
from .models import Note
from flask_login import login_required, current_user
import json

views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
	return render_template("home.html", user=current_user)

@views.route('/new_log', methods=['GET','POST'])
@login_required
def new_log():
	if request.method == "POST":
		c_firstName = request.form.get('c_firstName')
		c_email = request.form.get('c_email')
		c_final_score = request.form.get('c_final_score')
		note = request.form.get('note')
		c_Comm = request.form.get('c_Comm')
		c_Con = request.form.get('c_Con')
		c_Tech = request.form.get('c_Tech')
		c_Employ = request.form.get('c_Employ')

		cand = Note.query.filter_by(c_email = c_email).first()
		if cand:
			flash("Duplicate candidate entries not allowed!", category='error')
		else:
			new_entry = Note(data=note, c_firstName=c_firstName, c_email = c_email, user_id=current_user.id,	 c_Comm = c_Comm, c_Con=c_Con, c_Tech=c_Tech, c_Employ=c_Employ, c_final_score=c_final_score)
			db.session.add(new_entry)
			print(new_entry)
			db.session.commit()
			flash('Candidate Accepted for Assessment', category='Success')
			return redirect(url_for("views.home"))
			
	return render_template("new_log.html", user = current_user)
	

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/displayNote', methods=['GET','POST'])
def displayNote():
	res = {}
	note = json.loads(request.data)
	noteId = note['noteId']
	note = Note.query.get(noteId)
	return note