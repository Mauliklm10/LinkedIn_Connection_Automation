# LinkedIn_Connection_Automation
This is an automation Python project to send LinkedIn Connection Invites to my fellow interns of the Cigna 2021 intern class in my LinkedIn Group

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
