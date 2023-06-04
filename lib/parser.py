import re

def GetUnreadOnly(session,url="https://mbasic.facebook.com/messages/?folder=unread"):
    html_page = session.get(url).content
    return re.findall('<a href="/messages/read/\?tid=(.*?)&amp;refid=11#fua">',html_page)


def FindLastMessages(html):
    m = re.findall('<span class="[a-z][a-z] [a-z][a-z] [a-z][a-z]">(.*?)</span>',html)
    messages = []
    for message in m:
        emoji_fiter  = re.search('(.*?)<img src="https://static.xx.fbcdn.net/images/emoji.php/.*?',message)
        emoji_fiter2 = re.search('(.*?)<i class="[a-z][a-z] [a-z][a-z]" style="background-image:url\(https://static.xx.fbcdn.net/images/emoji.php/.*?\)"',message)

        if emoji_fiter != None:
            messages.append(emoji_fiter[1])
        elif emoji_fiter2 != None:

            messages.append(emoji_fiter2[1])
        else:
            messages.append(message)

    return messages


def ParseMessages(session,url="https://mbasic.facebook.com/messages/",unread_color="#eceff5"):

    html_page =  session.get(url).content
    css_style =  re.findall('<style type="text/css">(.*?)</style>',html_page)[0].strip()
    try:
        unread_message_class = re.search(
            '.([a-zA-Z][a-zA-Z]){background-color:%s;}' % unread_color,
            css_style,
        )[1]
    except:
        unread_message_class  = "junk"

    messages_info = []
    messageUrls = re.findall('<a href="/messages/read/\?tid=(.*?)&amp;refid=11#fua">',html_page)
    tables  = re.findall('<table class="(.*?)">',html_page)
    last_messages = FindLastMessages(html_page)

    for _ in range(99):
        last_messages.append("Dev-x-padding")

    index = 0
    for i in tables:
        if 'presentation' not in i:
            if unread_message_class in i:
                messages_info.append({'url':messageUrls[index],"last_message":last_messages[index].lower(),"status":"unread"})
            else:
                messages_info.append({'url':messageUrls[index],"last_message":last_messages[index].lower(),"status":"read"})
            index+= 1
    return messages_info