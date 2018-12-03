from flask import Flask, render_template, url_for
import requests
from secrets import *
import json
from datetime import datetime

##### get the top 5 stories and save as a list #######
CACHE_NYCT = 'cache_nyct.json'

try:
    cache_nyct_file = open(CACHE_NYCT, "r")
    cache_nyct_contents = cache_nyct_file.read()
    NYCT_DICTION = json.loads(cache_nyct_contents)
    cache_nyct_file.close()
except:
    NYCT_DICTION = {}

def params_unique_combination(baseurl, params):
    alphabetized_keys = sorted(params.keys())
    res = []
    for k in alphabetized_keys:
        res.append("{}-{}".format(k, params[k]))
    return baseurl + "_".join(res)

def get_stories(section):
    base_url = "https://api.nytimes.com/svc/topstories/v2/"
    extendedurl = base_url + section + '.json'
    parameters = {'api-key':nyt_key}
    unique_id = params_unique_combination(extendedurl,parameters)
    if unique_id in NYCT_DICTION:
        return NYCT_DICTION[unique_id]
    else:
        response = requests.get(extendedurl, params=parameters)
        NYCT_DICTION[unique_id]=json.loads(response.text)
        write_file = open(CACHE_NYCT,"w+")
        write_file.write(json.dumps(NYCT_DICTION,indent=4))
        write_file.close()
        return NYCT_DICTION[unique_id]

def get_list(section):
    nyc_top5 = get_stories(section)['results'][:5]
    results = []

    for i in nyc_top5:
        results.append('{} ({})'.format(i['title'],i['url']))
    return results
    


app = Flask(__name__)

@app.route('/')
def home_page():
    html = '''
        <h1>Welcome!</h1>
    '''
    return html

@app.route('/user/<user>')
def user_name(user):
    t = datetime.now().time()
    t = str(t).split(':')[0]
    morning = ['00','01','02','03','04','05','06','07','08','09','10','11','12']
    afternoon = ['13','14','15','16']
    evening = ['17','18','19','20']
    night = ['21','22','23','24']
    if t in morning:
        greet = "morning"
    elif t in afternoon:
        greet = "afternoon"
    elif t in evening:
        greet = "evening"
    elif t in night:
        greet = "night"

    return render_template('user.html', greeting=greet ,name=user, my_list=get_list('technology'))

@app.route('/user/<user>/home')
def section(user):
    return render_template('section.html', title="Hello," + user + "!", name=user, my_list=get_list('home'))

@app.route('/user/<user>/opinion')
def section1(user):
    return render_template('section1.html', title="Hello," + user + "!", name=user, my_list=get_list('opinion'))

@app.route('/user/<user>/world')
def section2(user):
    return render_template('section2.html', title="Hello," + user + "!", name=user, my_list=get_list('world'))

@app.route('/user/<user>/national')
def section3(user):
    return render_template('section3.html', title="Hello," + user + "!", name=user, my_list=get_list('national'))

@app.route('/user/<user>/politics')
def section4(user):
    return render_template('section4.html', title="Hello," + user + "!", name=user, my_list=get_list('politics'))

@app.route('/user/<user>/upshot')
def section5(user):
    return render_template('section5.html', title="Hello," + user + "!", name=user, my_list=get_list('upshot'))

@app.route('/user/<user>/nyregion')
def section6(user):
    return render_template('section6.html', title="Hello," + user + "!", name=user, my_list=get_list('nyregion'))

@app.route('/user/<user>/business')
def section7(user):
    return render_template('section7.html', title="Hello," + user + "!", name=user, my_list=get_list('business'))

@app.route('/user/<user>/technology')
def section8(user):
    return render_template('section8.html', title="Hello," + user + "!", name=user, my_list=get_list('technology'))

@app.route('/user/<user>/science')
def section9(user):
    return render_template('section9.html', title="Hello," + user + "!", name=user, my_list=get_list('science'))

@app.route('/user/<user>/health')
def section10(user):
    return render_template('section10.html', title="Hello," + user + "!", name=user, my_list=get_list('health'))

@app.route('/user/<user>/sports')
def section11(user):
    return render_template('section11.html', title="Hello," + user + "!", name=user, my_list=get_list('sports'))

@app.route('/user/<user>/arts')
def section12(user):
    return render_template('section12.html', title="Hello," + user + "!", name=user, my_list=get_list('arts'))

@app.route('/user/<user>/books')
def section13(user):
    return render_template('section13.html', title="Hello," + user + "!", name=user, my_list=get_list('books'))

@app.route('/user/<user>/movies')
def section14(user):
    return render_template('section14.html', title="Hello," + user + "!", name=user, my_list=get_list('movies'))

@app.route('/user/<user>/theater')
def section15(user):
    return render_template('section15.html', title="Hello," + user + "!", name=user, my_list=get_list('theater'))

@app.route('/user/<user>/sundayreview')
def section16(user):
    return render_template('section16.html', title="Hello," + user + "!", name=user, my_list=get_list('sundayreview'))

@app.route('/user/<user>/fashion')
def section17(user):
    return render_template('section17.html', title="Hello," + user + "!", name=user, my_list=get_list('fanshion'))

@app.route('/user/<user>/travel')
def section18(user):
    return render_template('section18.html', title="Hello," + user + "!", name=user, my_list=get_list('travel'))

@app.route('/user/<user>/magazine')
def section19(user):
    return render_template('section19.html', title="Hello," + user + "!", name=user, my_list=get_list('magazine'))

@app.route('/user/<user>/realestate')
def section20(user):
    return render_template('section20.html', title="Hello," + user + "!", name=user, my_list=get_list('realestate'))

@app.route('/user/<user>/automobiles')
def section21(user):
    return render_template('section21.html', title="Hello," + user + "!", name=user, my_list=get_list('automobiles'))

@app.route('/user/<user>/obituaries')
def section22(user):
    return render_template('section22.html', title="Hello," + user + "!", name=user, my_list=get_list('obituaries'))

@app.route('/user/<user>/insider')
def section23(user):
    return render_template('section23.html', title="Hello," + user + "!", name=user, my_list=get_list('insider'))




if __name__ == '__main__':
    app.run(debug=True)