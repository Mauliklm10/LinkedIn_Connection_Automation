# LinkedIn_Connection_Automation
This is an automation Python project to send LinkedIn Connection Invites to my fellow interns of the Cigna 2021 intern class in my LinkedIn Group

Here we have imported the necessary libraries.
```
import os, random, sys, time
from selenium import webdriver
from bs4 import BeautifulSoup
```
Here we are getting the address of the Google Chrome driver. After you run this line a new Google Chrome window will open. As we have not passed any link we will get a blank window.
```
browser = webdriver.Chrome('driver/chromedriver.exe')
```
Now we will open the LinkedIn login page using browser.get().
```
browser.get('https://www.linkedin.com/uas/login')
```
We will open the config.txt file which we have created and read the username and password from the file and then direct the bot to the LinkedIn group
```
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]
```
Now we have to automate the login process. For that, we will have to check the id of the textboxes which accept the username and password on the webpage. We can do this by right-clicking anywhere on the webpage and then clicking on ‘inspect’. After doing this you will see that the id of the username textbox is username and the id of password textbox is password.

find_element_by_id() returns the first element with the id attribute value matching the location.  The send_keys() method is used to send text to any field, such as input field of a form or even to anchor tag paragraph, etc. It replaces its contents on the webpage in your browser. submit() method is used to submit a form after you have sent data to a form.

Once you pass the username and password you can see them on the webpage before submitting.

Note:- The IDs of the textboxes can change. Hence before running this code check the current ID of the textboxes by inspecting the webpage.
```
elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()
```
Now we need to create links to visit different profiles. https://www.linkedin.com remains same irrespective of whose profile we visit. The profile ID is appended after it. The profile ID is different for different profiles. The code below will open the profile whose profile ID is /in/aarya-tadvalkar-092650193/.
```
visitingProfileID = '/in/aarya-tadvalkar-092650193/'
fullLink = 'https://www.linkedin.com' + visitingProfileID
browser.get(fullLink)
```
Now we will write a function that returns the list of the profile IDs of the people which are suggested to us by LinkedIn. We will send the entire page source to this function. To get the entire source code we will use BeautifulSoup(browser.page_source). This source code will be available in the soup variable in the function. First, we will find the div with class name pv-browsemap-section. From that, we will find all the a tags with class name pv-browsemap-section__member. The href in these a tags contain the profile IDs. If the profile ID is not already there in the profilesQueued and if it is not visited i.e. it is not there in the visitedProfiles we will append it to profilesID. At the end profilesID will contain the links and it will be returned. So we want to WebScrape the members page and get all the profile names of all members.

Note:- The class names used here can change. Hence before running this code check the current class name by inspecting the webpage.
```
visitedProfiles = []
profilesQueued = []

def getNewProfileIDs(soup, profilesQueued):
    profilesID = []
    pav = soup.find('div', {'class': 'pv-browsemap-section'})
    all_links = pav.findAll('a', {'class': 'pv-browsemap-section__member'})
    for link in all_links:
        userID = link.get('href')
        if((userID not in profilesQueued) and (userID not in visitedProfiles)):
            profilesID.append(userID)
    return profilesID
```
```
getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
['/in/saransh-kotha-567a84182/',
 '/in/sonali-bedade-0519071ab/',
 '/in/shreya-mali-1a6456191/',
 '/in/advait-raut-6a060616b/',
 '/in/swati-tiwari12/',
 '/in/srishti-s-agrawal/',
 '/in/preyashgothane/',
 '/in/mohini-chaudhari-b77a74155/',
 '/in/ketan-mankar/',
 '/in/shubhra-masurkar-940a3a1a4/']
```
```
profilesQueued = getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
```
Now for each link in profilesQueued we are going to perform the following actions:-

We will append the Profile ID to the base link  https://www.linkedin.com  which is common to all. Then we will get the fullLink. We will visit the fullLink.
Now we have to send a connection request to the person. For that, we will find the class name of the button which says connect. The class name is pv-s-profile-actions. We will find the element using the class name and then click on it using .click().
After you click the connect button you will get a prompt asking if you want to add a note. We will click on the button add a note by using its class name which is mr1.
Now you will get a text area. We will select the text area using its id custom-message. We will send our message using send_keys().
After that, we will have to select the button done which has class ml1 and click it.
Then we will add the current ID to the file visitedUsers.txt.
Next, we will get the suggested profiles of the current profile using the function getNewProfileIDs(). We will add these new profile IDs to profilesQueued.
Then we have just introduced a random delay so that LinkedIn doesn’t detect a bot.

The constraints are as follows:
2nd and no level connection people have a connection button on their profile page
3rd connection level people do not have such a button, instead we have to click the 3 dots on their profile next to message and then choose the connect option.

If and else statement but dont know if we want them inside or outside the loop.
```
while profilesQueued:
    try:
        visitingProfileID = profilesQueued.pop()
        visitedProfiles.append(visitingProfileID)
        fullLink = 'https://www.linkedin.com' + visitingProfileID
        browser.get(fullLink)
   
        browser.find_element_by_class_name('pv-s-profile-actions').click()

        browser.find_element_by_class_name('mr1').click()

        customMessage = "Hello, I have found mutual interest area and I would be more than happy to connect with you. Kindly, accept my invitation. Thanks!"
        elementID = browser.find_element_by_id('custom-message')
        elementID.send_keys(customMessage)

        browser.find_element_by_class_name('ml1').click()

        # Add the ID to the visitedUsersFile
        with open('visitedUsers.txt', 'a') as visitedUsersFile:
            visitedUsersFile.write(str(visitingProfileID)+'\n')
        visitedUsersFile.close()

        # Get new profiles ID
        soup = BeautifulSoup(browser.page_source)
        try: 
            profilesQueued.extend(getNewProfileIDs(soup, profilesQueued))
        except:
            print('Continue')

        # Pause
        time.sleep(random.uniform(3, 7)) # Otherwise, sleep to make sure everything loads

        if(len(visitedProfiles)%50==0):
            print('Visited Profiles: ', len(visitedProfiles))

        if(len(profilesQueued)>100000):
            with open('profilesQueued.txt', 'a') as visitedUsersFile:
                visitedUsersFile.write(str(visitingProfileID)+'\n')
            visitedUsersFile.close()
            print('100,000 Done!!!')
            break;
    except:
        print('error')
```        
