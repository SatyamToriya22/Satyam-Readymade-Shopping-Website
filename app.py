from flask import Flask,render_template,request,session,redirect
from werkzeug.datastructures import RequestCacheControl
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/satyam_readymade_db'
db=SQLAlchemy(app)
app.secret_key = 'super secret key'
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME="your-gmail-id",
    MAIL_PASSWORD="your-gmail-password")
mail = Mail(app)
Dict=[]


class home_slide_tb(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    small_heading=db.Column(db.String(100),nullable=True)
    mid_heading=db.Column(db.String(100),nullable=True)
    heading=db.Column(db.String(100),nullable=True)
    button=db.Column(db.String(30),nullable=True)
    img_file=db.Column(db.String(100),nullable=True)


class home_category_tb(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    img_file=db.Column(db.String,nullable=True)
    heading=db.Column(db.String,nullable=True)
    sub_heading=db.Column(db.String,nullable=True)
    button=db.Column(db.String,nullable=True)
    slug=db.Column(db.String,nullable=True)

class home_newarrival(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    img_file=db.Column(db.String(30),nullable=True)
    product_name=db.Column(db.String(100),nullable=True)
    price=db.Column(db.String(30),nullable=True)
    description=db.Column(db.String(1000),nullable=True)
    slug=db.Column(db.String(50),nullable=True)


class home_testimonial(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    paragraph=db.Column(db.String(1000),nullable=True)
    owner_name=db.Column(db.String(100),nullable=True)
    owner_position=db.Column(db.String(100),nullable=True)
    img_file=db.Column(db.String(50),nullable=True)

class menswear_gallery(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    img_file=db.Column(db.String(50),nullable=True)
    price=db.Column(db.String(50),nullable=True)
    product_name=db.Column(db.String(50),nullable=True)
    description=db.Column(db.String(100),nullable=True)
    slug=db.Column(db.String(50),nullable=True)


class womenswear_gallery(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    img_file=db.Column(db.String(50),nullable=True)
    price=db.Column(db.String(50),nullable=True)
    product_name=db.Column(db.String(50),nullable=True)
    description=db.Column(db.String(100),nullable=True)
    slug=db.Column(db.String(50),nullable=True)


class womenswear_recommended(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    img_file=db.Column(db.String(50),nullable=True)
    product_name=db.Column(db.String(50),nullable=True)
    price=db.Column(db.String(50),nullable=True)

class boyswear_gallery(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    img_file=db.Column(db.String(50),nullable=True)
    price=db.Column(db.String(50),nullable=True)
    product_name=db.Column(db.String(50),nullable=True)
    description=db.Column(db.String(100),nullable=True)
    slug=db.Column(db.String(50),nullable=True)

class girlswear_gallery(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    img_file=db.Column(db.String(50),nullable=True)
    price=db.Column(db.String(50),nullable=True)
    product_name=db.Column(db.String(50),nullable=True)
    description=db.Column(db.String(100),nullable=True)
    slug=db.Column(db.String(50),nullable=True)


class registered_user(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),nullable=True)
    email_id=db.Column(db.String(50),nullable=True)
    contact=db.Column(db.String(13),nullable=True)
    password=db.Column(db.String(50),nullable=True)

class checkout_tb(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    f_name=db.Column(db.String(50),nullable=True)
    l_name=db.Column(db.String(50),nullable=True)
    email=db.Column(db.String(50),nullable=True)
    state=db.Column(db.String(50),nullable=True)
    country=db.Column(db.String(50),nullable=True)
    address=db.Column(db.String(50),nullable=True)
    postcode=db.Column(db.String(50),nullable=True)
    city=db.Column(db.String(50),nullable=True)
    contact=db.Column(db.String(13),nullable=True)
    product=db.Column(db.String(30),nullable=True)
    cod=db.Column(db.String(50),nullable=True)
    terms=db.Column(db.String(50),nullable=True)
    subscribe=db.Column(db.String(50),nullable=True)

class contact_form(db.Model):
    snum=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=True)
    email=db.Column(db.String(50),nullable=True)
    city=db.Column(db.String(50),nullable=True)
    contact=db.Column(db.String(13),nullable=True)

class newlater(db.Model):
    snum=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50),nullable=True)

class offer_area(db.Model):
    snum=db.Column(db.Integer,primary_key=True)
    img_file=db.Column(db.String(50),nullable=True)
    price=db.Column(db.String(50),nullable=True)
    product_name=db.Column(db.String(50),nullable=True)
    description=db.Column(db.String(100),nullable=True)
    slug=db.Column(db.String(50),nullable=True)


@app.route('/')
def home():
    home_slide=home_slide_tb.query.all()
    home_category=home_category_tb.query.all()
    home_newarriv=home_newarrival.query.all()
    home_testimoni=home_testimonial.query.all()
    home_offer_area=offer_area.query.all()
    

    return render_template('index.html',slide=home_slide,category=home_category,newarrival=home_newarriv,testimonial=home_testimoni,offer_area=home_offer_area ,session=session)

@app.route('/menswear')
def menswear():
    
    menswear=menswear_gallery.query.all()
    recommended=womenswear_recommended.query.all()
    return render_template('menswear.html',gallery=menswear,recommended=recommended,session=session)

@app.route('/womenswear')
def womenswear():
    womenswear=womenswear_gallery.query.all()
    recommended=womenswear_recommended.query.all()
    return render_template('womenswear.html',gallery=womenswear,recommended=recommended,session=session)

@app.route('/boykids')
def boykids():
    gallery=boyswear_gallery.query.all()
    recommended=womenswear_recommended.query.all()
    return render_template('boykids.html',gallery=gallery,recommended=recommended,session=session)

@app.route('/girlkids')
def girlkids():
    gallery=girlswear_gallery.query.all()
    recommended=womenswear_recommended.query.all()
    return render_template('girlkids.html',gallery=gallery,recommended=recommended,session=session)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email_id=request.form.get('email_id')
        password=request.form.get('pass')
        info=registered_user.query.filter_by(email_id=email_id).first()
        if info:
            if info.email_id==email_id and info.password==password:
                session['user']=email_id
                return redirect('/')

    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        name=request.form.get('name')
        email_id=request.form.get('email_id')
        contact=request.form.get('contact')
        password=request.form.get('pass')

        entry=registered_user(username=name,email_id=email_id,contact=contact,password=password)
        db.session.add(entry)
        db.session.commit()
        return render_template('login.html')


    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


@app.route('/cart/<string:prod_slug>',methods=['GET'])
def cart_products(prod_slug):
    new_Arriv=home_newarrival.query.filter_by(slug=prod_slug).first()
    boys_gallery=boyswear_gallery.query.filter_by(slug=prod_slug).first()
    girls_gallery=girlswear_gallery.query.filter_by(slug=prod_slug).first()
    mens_gallery=menswear_gallery.query.filter_by(slug=prod_slug).first()
    womens_gallery=womenswear_gallery.query.filter_by(slug=prod_slug).first()
    offer=offer_area.query.filter_by(slug=prod_slug).first()
    if prod_slug=='None':
        product='None'
        return render_template('cart.html',products=product)

    else:
        if offer:
            product=offer
        elif new_Arriv:
            product=new_Arriv
        elif boys_gallery:
            product=boys_gallery
        elif girls_gallery:
            product=girls_gallery
        elif mens_gallery:
            product=mens_gallery
        elif womens_gallery:
            product=womens_gallery
        Dict.append(product)
        return render_template('cart.html',products=Dict)

@app.route('/remove/<string:slug>')
def remove(slug):
    if slug=='clearcart':
        for item in Dict:
            Dict.pop()
        return redirect('/')

    else:
        for prod in Dict:
            if prod.slug==slug:
                Dict.remove(prod)
        return redirect('/')

@app.route('/checkout',methods=['GET','POST'])
def checkout():
    
    if request.method=='POST':
        f_name=request.form.get('fname')
        l_name=request.form.get('lname')
        email=request.form.get('email')
        state=request.form.get('state')
        country=request.form.get('country')
        address=request.form.get('address')
        postcode=request.form.get('postcode')
        city=request.form.get('city')
        contact=request.form.get('contact')
        product=request.form.get('product')
        cod=request.form.get('cod')
        terms=request.form.get('terms')
        subscribe=request.form.get('subscribe')
        entry=checkout_tb(f_name=f_name,l_name=l_name,email=email,state=state,country=country,address=address,postcode=postcode,city=city,contact=contact,product=product,cod=cod,terms=terms,subscribe=subscribe)
        db.session.add(entry)
        db.session.commit()

        mail.send_message('Welcome To Satyam Readymade ', sender='Admin', recipients=[
                              email], body="Hello "+name+',\n\nThanks for Placing Order ! Your Order Comes to Your Door Soon.. \n \nThanks Regards'+'\n'+'Admin Of Satyam ReadyMade')
        return render_template('order_placed.html')


    return render_template('checkout.html',product=Dict)


@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        city=request.form.get('city')
        contact=request.form.get('contact')

        entry=contact_form(name=name,email=email,city=city,contact=contact)
        db.session.add(entry)
        db.session.commit()
        return render_template('form_submitted.html')

    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/subscribe',methods=['GET','POST'])
def subscribe():
    if request.method=='POST':
        email=request.form.get('email')

        entry=newlater(email=email)
        db.session.add(entry)
        db.session.commit()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)