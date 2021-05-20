import os, random, sys, time
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome('chromedriver.exe')

browser.get('https://www.linkedin.com/uas/login')

file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

browser.get('https://www.linkedin.com/groups/12508395/members/')
'''
visitingProfileID = '/in/laxmimerit/'
fullLink = 'https://www.linkedin.com' + visitingProfileID
browser.get(fullLink)
'''
visitedProfiles = []
profilesQueued = []

def getNewProfileIDs(soup, profilesQueued):
    profilesID = []
    pav = soup.find('div', {'class': 'artdeco-typeahead ember-view groups-members-list'})
    all_links = pav.findAll('a', {'class': 'ember-view ui-conditional-link-wrapper ui-entity-action-row__link'})
    for link in all_links:
        userID = link.get('href')
        if((userID not in profilesQueued) and (userID not in visitedProfiles)):
            profilesID.append(userID)
    return profilesID

getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)

profilesQueued = getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)

while profilesQueued:
    try:
        visitingProfileID = profilesQueued.pop()
        visitedProfiles.append(visitingProfileID)
        fullLink = 'https://www.linkedin.com' + visitingProfileID
        browser.get(fullLink)

# an if statement here to find if the element exists on the profile

        browser.find_element_by_class_name('pv-s-profile-actions').click()

        browser.find_element_by_class_name('mr1').click()

        customMessage = "Hello, this is Maulik from your LinkedIn group for the Cigna 2021 interns. Hopefully we can connect!"
        elementID = browser.find_element_by_id('custom-message')
        elementID.send_keys(customMessage)

        browser.find_element_by_class_name('ml1').click()

        # The time taken for the process to run
        time.sleep(random.uniform(5, 15))

    except:
        print('error')


