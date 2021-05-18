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

#yes


