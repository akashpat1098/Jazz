# Jazz
Steps to run this program
1. Downlaod a repository 
2. Run the requirement.txt  file and downlaod all the required modules
3. make ".env "file and add foolowing data into it:<!-- naming file :-<no name>.env .You dont have to give name of the file just make file with name of ".env" -->
    <!-- name of the user -->
    USER=Akash
    <!-- name of the bot -->
    BOTNAME=Jazz
    <!-- your email through which you have to send the mail -->
    EMAIL=akashpatel1098@gmail.com
    <!-- password of the your email -->
    PASSWORD=1098akash
    <!-- API KEYS -->
    <!-- news api key from Newsapi.org  website -->
    NEWS_API_KEY=ca62a849cde14140a6769c45be203483
    <!-- weather report API from openweathermap.org -->
    OPENWEATHERMAP_API_KEY=b36c0985595ccdf6a3a0517de977caac
    <!-- trending movies API from themoviedb.org -->
    TMDB_USER_API_KEY=fb87fea78adfb2c5414eaae680e2a862

4. Add your emails data of others if you have, to whom you want to send email to them in emails.json or you can dump the emails with dictionary of name:emails as  key value with following code 
<!-- run this code in separte file and then you can delete it -->
<!-- dictionary of email should be in this format -->
email={"name1":"email1","name2":"email2","name3":"email3","name4":"email4","name5":"email5"}
<!-- run this code name of the dict should be email -->
with open("emails.json","w")  as f:
    json.dump(email,f,indent=4)
--> You have to make 2 file:
    1->.env where passwords and API key will be there
    2->emails.json file where emails in format of json strings will be there
5. change the paths of directory of dictionary in utils.py 
6. You have to turn on the less secure app in of logined account
7. Lastly,Run the Jazz.py file 

