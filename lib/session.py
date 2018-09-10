import requests
import pyquery


def login(email,password,ua="Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0"):

    session = requests.session()
    session.headers.update({
        'User-Agent': ua
    })

    response = session.get('https://m.facebook.com')
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass':  password
    }, allow_redirects=False)

    if 'c_user' in response.cookies:
        homepage_resp = session.get('https://m.facebook.com/profile.php')
        dom = pyquery.PyQuery(homepage_resp.text.encode('utf8'))
        fb_dtsg = dom('input[name="fb_dtsg"]').val()
        return {"session":session,"fb_dtsg":fb_dtsg,"id":response.cookies['c_user'], "cookies":response.cookies}
    else:
        return {"session":"","fb_dtsg":"","id":"", "cookies":""}
