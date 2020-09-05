import http.cookiejar
import urllib.request
import requests
import bs4
import pandas as pd
from secret import username,password

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

urllib.request.install_opener(opener)

authentication_url = "https://mbasic.facebook.com/login.php"
payload = {

    'email':username,
    'pass':password
}
data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
contents = resp.read()
#print(contents)

url='https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=1000&reaction_type=1&total_count=162341&ft_ent_identifier=1903182866490987'

data=requests.get(url,cookies=cj)

soup=bs4.BeautifulSoup(data.content,'html.parser')
#print(soup.prettify())

names=soup.find_all('h3',class_='be')
people_who_liked = []
for i in names[0:10]:
    people_who_liked.append(i.text)

##########################################################################################

url2='https://m.facebook.com/browse/shares?id=1903182866490987'

data2=requests.get(url2,cookies=cj)

soup2=bs4.BeautifulSoup(data2.content,'html.parser')

shares=soup2.find_all('span')
people_who_share=[]
for i in shares[1:]:
    people_who_share.append(i.text)

#print(people_who_share)

###########################################################################################

url3="https://m.facebook.com/story.php?story_fbid=1903182866490987&id=552465834896037&p=0&av=100003187091492&eav=AfbDLZZ2XHV7wXaQTEoSV2fsfh5wwZFk-542yWQKm-Dgtca_A9D6E0eGWD-o4ws0Dsc&refid=52&_ft_=qid.6868326991614836593%3Amf_story_key.-8453028648201440336%3Atop_level_post_id.1903182866490987%3Acontent_owner_id_new.552465834896037%3Apage_id.552465834896037%3Asrc.22%3Aphoto_id.1903182789824328%3Astory_location.5%3Astory_attachment_style.photo%3Aview_time.1599156950%3Afilter.h_nor%3Atds_flgs.3%3Apage_insights.%7B%22552465834896037%22%3A%7B%22page_id%22%3A552465834896037%2C%22page_id_type%22%3A%22page%22%2C%22actor_id%22%3A552465834896037%2C%22dm%22%3A%7B%22isShare%22%3A0%2C%22originalPostOwnerID%22%3A0%7D%2C%22psn%22%3A%22EntStatusCreationStory%22%2C%22post_context%22%3A%7B%22object_fbtype%22%3A266%2C%22publish_time%22%3A1598984541%2C%22story_name%22%3A%22EntStatusCreationStory%22%2C%22story_fbid%22%3A%5B1903182866490987%5D%7D%2C%22role%22%3A1%2C%22sl%22%3A5%2C%22targets%22%3A%5B%7B%22actor_id%22%3A552465834896037%2C%22page_id%22%3A552465834896037%2C%22post_id%22%3A1903182866490987%2C%22role%22%3A1%2C%22share_id%22%3A0%7D%5D%7D%7D"

data3=requests.get(url3,cookies=cj)

soup3=bs4.BeautifulSoup(data3.content,'html.parser')

comments=soup3.find_all('h3')
comments_name=[]
for i in comments[1:]:
    comments_name.append(i.text)

#print(comments_name)


    
##########################################################################################

post_details=pd.DataFrame({
    'Likes':people_who_liked,
    'Shares':people_who_share,
    'Comments':comments_name
    })

print(post_details)

post_details.to_csv('fbpostdetails .csv')