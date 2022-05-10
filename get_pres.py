from ast import Interactive
from unicodedata import mirrored
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from sqlalchemy import true
from wtforms import StringField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime
from sqlalchemy import cast, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker




app = Flask(__name__)
app.config['SECRET_KEY'] = 'thequickbrownfrog'

import jinja2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thequickbrownfrog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

##*****************************************##
## Connect to your local postgres database ##
##*****************************************##

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:JimmyJohn3409!@localhost/miR.Gut'


db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class SearchButton_Form(FlaskForm):
    submit = SubmitField('Search miR.Gut')


class NameForm(FlaskForm):
    name2 = RadioField('Search By miRBase ID Or Microbiota:', choices=[('mirbase_id', 'MicroRNA'), ('microbiota', 'Microbiota')])
    name1 = StringField('Enter Keyword (Ex: hsa-mir-22 or Fusobacterium nucleatum):', validators=[DataRequired()])
    name3 = SelectField('Limit Results By:', choices=[('1','1'),('5', '5'), ('25', '25'),('100', '100'),('1000', '1000')])
    name4 = SelectField('Order results By:', choices=[('mirbase_id', 
            'MicroRNA'), ('organism_name', 'Microbiota'), ('directionality', 'Direction')])
    submit = SubmitField('Submit')


class Interactions(db.Model):
    __tablename__ = "interactions"
    interaction_id = db.Column(db.String(11),
                        primary_key=True,
                        nullable=True)
    mirbase_id = db.Column(db.String(20),
                        index=False,
                        nullable=False)
    directionality = db.Column(db.String(10),
                        index=False,
                        nullable=False)
    organism_name = db.Column(db.String(150),
                        index=False,
                        nullable=False)
    effects = db.Column(db.Text,
                        index=False,
                        nullable=False)
    disease_name = db.Column(db.String(150),
                        index=False,
                        nullable=False)
    doi_id = db.Column(db.String(512),
                        index=False,
                        nullable=False)
    pmid = db.Column(db.Integer,
                        index=False,
                        nullable=True)

    def __init__(self, interaction_id, mirbase_id, directionality, organism_name, effects, disease_name, doi_id, pmid):
        self.interaction_id = interaction_id
        self.mirbase_id = mirbase_id
        self.directionality = directionality
        self.organism_name = organism_name
        self.effects = effects
        self.disease_name = disease_name
        self.doi_id = doi_id
        self.pmid = pmid

    def __repr__(self):
        return f"<Interactions {self.interaction_id}>"

class Microrna(db.Model):
    __tablename__ = "microrna"
    mirbase_id = db.Column(db.String(20),
                        primary_key=True,
                        index=False,
                        nullable=False)
    sequence = db.Column(db.String(200),
                        index=False,
                        nullable=False)

    def __init__(self, mirbase_id, sequence):
        self.mirbase_id = mirbase_id
        self.sequence = sequence

    def __repr__(self):
        return f"<Microrna {self.mirbase_id}>"

class Microrna_disease(db.Model):
    __tablename__ = "microrna_disease"
    mirbase_id = db.Column(db.String(25),
                            index=False,
                            nullable=True)
    disease_name = db.Column(db.String(200),
                        index=False,
                        nullable=True)
    id = db.Column(db.Integer,
                        primary_key=True,
                        index=True,
                        nullable=False)

    def __init__(self, mirbase_id, disease_name, id):
        self.mirbase_id = mirbase_id
        self.disease_name = disease_name
        self.id = id

    def __repr__(self):
        return f"<Microrna_disease {self.id}>"

class Disease(db.Model):
    __tablename__ = "disease"
    do_id = db.Column(db.String(15),
                            primary_key=True,
                            nullable=False)
    disease_name = db.Column(db.String(200),
                        index=False,
                        nullable=False)

    def __init__(self, do_id, disease_name):
        self.do_id = do_id
        self.disease_name = disease_name

    def __repr__(self):
        return f"<Disease {self.do_id}>"

class Taxonomy(db.Model):
    __tablename__ = "taxonomy"
    organism_name = db.Column(db.String(110),
                        index=False,
                        nullable=False)
    node_rank = db.Column(db.String(18),
                        index=False,
                        nullable=True)
    ncbi_taxon_id = db.Column(db.Integer,
                        primary_key=True,
                        nullable=False)
    taxon_id = db.Column(db.Integer,
                        index=False,
                        nullable=True)
    parent_taxon_id = db.Column(db.Integer,
                        index=False,
                        nullable=True)
    superkingdom = db.Column(db.String(15),
                        index=False,
                        nullable=True)

    def __init__(self, organism_name, node_rank, ncbi_taxon_id, taxon_id, parent_taxon_id, superkingdom):
        self.organism_name = organism_name
        self.node_rank = node_rank
        self.ncbi_taxon_id = ncbi_taxon_id
        self.taxon_id = taxon_id
        self.parent_taxon_id = parent_taxon_id
        self.superkingdom = superkingdom

    def __repr__(self):
        return f"<Taxonomy {self.ncbi_taxon_id}>"


class Microbiota(db.Model):
    __tablename__ = "microbiota"
    ncbi_taxon_id = db.Column(db.Integer,
                        index=False,
                        nullable=True)
    organism_name = db.Column(db.String(100),
                        index=False,
                        nullable=False)
    entry_id = db.Column(db.Integer,
                        primary_key=True,
                        nullable=False)
    
    def __init__(self, ncbi_taxon_id, organism_name, entry_id):
        self.organism_name = organism_name
        self.ncbi_taxon_id = ncbi_taxon_id
        self.entry_id = entry_id

    def __repr__(self):
        return f"<Microbiota {self.entry_id}>"
        
class Disease_microbiota(db.Model):
    __tablename__ = "disease_microbiota"
    experiment_id = db.Column(db.Integer,
                        primary_key=True,
                        index=False,
                        nullable=False)
    disease_name = db.Column(db.String(200),
                        index=False,
                        nullable=False)                    
    organism_name = db.Column(db.String(100),
                        index=False,
                        nullable=False)
    organism_ncbi_id = db.Column(db.Integer,
                        index=False,
                        nullable=True)
    
    
    def __init__(self, experiment_id, disease_name, organism_name, organism_ncbi_id):
        self.organism_name = organism_name
        self.organism_ncbi_id = organism_ncbi_id
        self.disease_name = disease_name
        self.experiment_id = experiment_id

    def __repr__(self):
        return f"<Disease_microbiota {self.experiment_id}>"



@app.route("/", methods =['GET','POST'])
def index():
    form2 = SearchButton_Form()
    if request.method == 'POST':
        return redirect('/search')
    return render_template("index.html", form2=form2)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ref')
def ref():
    return render_template('ref.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')

##*****************************************##
## This is what the expansion should of looked like  ##
##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv##
##*****************************************##
@app.route('/vis_extension')
def vis_extension():
    return render_template('vis_extension.html')
##*****************************************##
## ##
##*****************************************##

@app.route('/statistics')
def statistics():
    some_engine = create_engine('postgresql://postgres:JimmyJohn3409!@localhost/miR.Gut')
    Session = sessionmaker(bind=some_engine)
    session = Session()
    s1 = session.query(Interactions).count()
    s2 = session.query(Microrna).count()
    s3 = session.query(Microbiota).count()
    s4 = session.query(Microrna_disease).count()
    s5 = session.query(Disease_microbiota).count()
    s6 = session.query(Disease).count()
    return render_template('statistics.html', s1=s1, s2=s2, s3=s3,s4=s4,s5=s5,s6=s6)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route("/results", methods = ['GET', 'POST'])
def presults():
    name1 = session.get('name1')
    name2 = session.get('name2')
    name3 = session.get('name3')
    name4 = session.get('name4')
    form3 = SearchButton_Form()

    searchterm = "%{}%".format(name1) ## adds % wildcards to front & back of search term
    displayorder = eval('Interactions.{}'.format(name4))

    if name2 == 'mirbase_id':
        presults = Interactions.query.filter(Interactions.mirbase_id.like(searchterm)).order_by(displayorder).limit(name3).all()
        mirseq = Microrna.query.filter(Microrna.mirbase_id.like(searchterm)).limit(name3).all()
        if mirseq == []:
                return redirect('/search')
        else:
            mirdis = Microrna_disease.query.filter(Microrna_disease.mirbase_id.like(searchterm)).limit(name3).all()
        ## need to convert all the mirBase_Id to lowercase
        ##mirseq = Microrna.query.filter(Microrna.mirbase_id.like(searchterm)).order_by(displayorder).limit(name3).all()
        ##mirdis = Microrna_disease.query.filter(Microrna_disease.mirbase_id.like(searchterm)).order_by(displayorder).limit(name3).all()

    else:  ##  if not last_name defaults to first_name

        if name1.isdigit() == True:
            temporary = int(name1)
            mic_entry = Microbiota.query.filter(Microbiota.ncbi_taxon_id == temporary).limit(name3).all()
            micdis = Disease_microbiota.query.filter(Disease_microbiota.organism_ncbi_id == temporary).limit(name3).all()
            if mic_entry == []:
                return redirect('/search')
            else:
                if hasattr(mic_entry, 'organism_name') == True:
                    temp = mic_entry.organism_name
                    new_search_term = "%{}%".format(temp)
                    presults = Interactions.query.filter(Interactions.organism_name.like(new_search_term)).order_by(displayorder).limit(name3).all()
                else:
                    return redirect('/search')
        else: 
            presults = Interactions.query.filter(Interactions.organism_name.like(searchterm)).order_by(displayorder).limit(name3).all()
            mic_entry = Microbiota.query.filter(Microbiota.organism_name.like(searchterm)).limit(name3).all()
            micdis = Disease_microbiota.query.filter(Disease_microbiota.organism_name.like(searchterm)).limit(name3).all()

    #presults = Data.query.all()
    #presults = Data.query.order_by(Data.first_name).all()
    #presults = Data.query.filter(Data.last_name == name1).order_by(Data.last_name).all()
    #presults = Data.query.filter_by(Data.last_name.like(searchterm)).order_by(displayorder).all()

    if request.method == 'POST':
        return redirect('/search')
    
    if name2 == 'mirbase_id':
        return render_template('microrna_results.html', presults=presults,
        name1=name1,name2=name2,name3=name3,name4=name4,form3=form3, mirseq=mirseq, mirdis=mirdis)
    else:
        return render_template('microbiota_results.html', presults=presults,
        name1=name1,name2=name2,name3=name3,name4=name4,form3=form3, micdis=micdis, mic_entry=mic_entry)



@app.route('/search', methods=['GET', 'POST'])
def search():
    name1 = None
    name2 = None
    name3 = None
    name4 = None
    form = NameForm()
    if form.validate_on_submit():
        if request.method == 'POST':
           session['name1']  = form.name1.data		# name1 is search term entered in first text box on form
           session['name2']  = form.name2.data		# name2 is to specify first or last name in search query
           session['name3']  = form.name3.data		# name3 is to limit the number of results displayed in table
           session['name4']  = form.name4.data		# name4 is to specify the order of the search results
#          return '''<h1>The name1 value is: {}</h1>
#                  <h1>The name2  value is: {}</h1>'''.format(name1, name2)
           return redirect('/results')

        form.name1.data = ''	## Reset form values
        form.name2.data = ''
        form.name3.data = ''
        form.name4.data = ''
    return render_template('search.html', form=form) 

if __name__ == "__main__":
    app.run(debug=True)

