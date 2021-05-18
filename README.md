# LinkedIn_Connection_Automation
This is an automation Python project to send LinkedIn Connection Invites to my fellow interns of the Cigna 2021 class in my LinkedIn Group

We begin by installing selenium and beautifulsoup

We use the webdriver of selenium to open a remote google chrome page for the automation process to take place within.

Using beautifulsoup we webscrape all the usernames of the people in the LinkedIn group and store it within a list.

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
2nd and 3rd level connection people have a connection button on their profile page and its more or less in the same location or class so its alright
No level connection people do not have such a button, instead we have to click the 3 dots on their profile next to message and then choose the connect option.

If and else statement but dont know if we want them inside or outside the loop.

We could make the if statements dependent on their connection level or make them dependent on their ability to find the connect buton and if they do not find the connect button they search of the 3 dots on the side of the profile and try connecting from there.

