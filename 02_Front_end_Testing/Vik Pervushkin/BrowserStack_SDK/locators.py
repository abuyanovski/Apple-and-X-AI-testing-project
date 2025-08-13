from selenium.webdriver.common.by import By
#URLs
apple_url="https://www.apple.com/"
support_url="https://support.apple.com/"
repair_url="https://support.apple.com/iphone/repair"
utube_url="https://www.youtube.com/applesupport"
mac_url ="https://support.apple.com/mac/imac"
apple_sign_in_ur = "https://account.apple.com/sign-in"

#submenu urls
iphone_sup_url ="https://support.apple.com/iphone"
mac_sup_url = "https://support.apple.com/mac"
ipad_sup_url = "https://support.apple.com/ipad"
watch_sup_url = "https://support.apple.com/watch"
appleVisPro_sup_url= "https://support.apple.com/apple-vision-pro"
airPods_sup_url = "https://support.apple.com/airpods"
music_sup_url = "https://support.apple.com/music?cid=gn-ols-music-psp-explore"
tv_sup_url = "https://support.apple.com/tv"


#Locators
forgot_passw = "(//div[@class='as-tile-content as-center'])[1]"
play_button = "//span[@class='thumbnail-button']"
full_screen = "(//button[@type='button'])[8]"
sup_search = "//input[@id='as-search-input']"
sup_locator = "//a[contains(@data-globalnav-item-name,'support')]"
imac_sup_img = "(//img[@width='60'])[1]"
mac_sup_img ="(//img[contains(@src,'2x.png')])[2]"
feedback_no = "(//button[@class='button button-reduced button-secondary'])[2]"
text_area = "//textarea[@type='text']"
submit_but= "//textarea[@type='text']"
vid_but = "//button[contains(@class, 'controls-play-pause-button')]"
vidBut_loc = "//button[contains(@class, 'controls-play-pause-button') and @role='button']"
apple_sup_on_utube = "(//img[contains(@src,'2x.png')])[8]"
find_store = "(//a[@href='/retail/'])[2]"

start_cancel = "(//a[contains(@data-analytics-event,'click')])[1]"
apple_account_wind_url ="https://account.apple.com/sign-in?returnUrl=https%3A%2F%2Faccount.apple.com%2Faccount%2Fmanage%2Fsection%2Fsubscriptions"

email_sign_in_form = "(//button[@type='button'])[2]"
password_ID = "//input[@id='password_text_field']"
billing_subs ="//p[contains(.,'Billing and subscriptions')]"

#locators of explore panel
iphone_loc = "//span[@aria-label='iPhone Support'][contains(.,'iPhone')]"
mac_loc = "//span[@aria-label='Mac Support'][contains(.,'Mac')]"
ipad_loc = "//span[@aria-label='iPad Support'][contains(.,'iPad')]"
watch_loc = "//span[@aria-label='Apple Watch Support'][contains(.,'Watch')]"
appleVisPro_loc = "//span[@aria-label='Vision Support'][contains(.,'Vision')]"
airPods_loc = "//span[@aria-label='AirPods Support'][contains(.,'AirPods')]"
tv_loc = "//span[@aria-label='TV Support'][contains(.,'TV')]"

appleLogoHomeBut = "//a[@href='/'][contains(.,'Apple')]"
access_loc = "//a[text()='Accessibility']"
subMenu_loc = "//a[contains(@data-globalnav-item-name,'support')]"



#the repair form
service_dropdown ="(//select[@data-ignore-tracking='true'])[1]"
product_dropdown ="(//select[@data-ignore-tracking='true'])[2]"
model_dropdown ="(//select[@data-ignore-tracking='true'])[3]"
utube_link="(//span[@class='icon-copy'])[1]"
searchBar = "(//a[contains(@role,'button')])[1]"
searchBar1 = "//input[@placeholder='Search apple.com']"




