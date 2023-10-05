import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Function to download a file from a given URL
def download_file(url):
    # Navigate to the URL
    driver.get(url)
  # Find the download link element using its attributes (you may need to inspect the webpage source)
    download_link = driver.find_element(By.XPATH, "//*[@id='download']")
    # Click the download link
    download_link.click()
        # Wait for the download to complete (you can set a timeout)
    time.sleep(25)  # Adjust the sleep time as needed


# Define the URL of the webpage you want to visit
url = "https://nitroflare.com/login"
# url = "https://nitroflare.com/view/5035E098F87D7B1/Verifications.io_Database_Leaked_February_2019.part011.rar"

# Specify the path to your web driver (e.g., ChromeDriver)


# Set the path to Chromedriver as a system property
chromedriver_path = "C:/chromedriver/chromedriver.exe"
webdriver.chrome.driver = chromedriver_path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Initialize the web driver (in this example, we use Chrome)

try:
    # Navigate to the URL
    driver.get(url)

    # Find and fill in the login form (replace with the actual form fields)
    username_field = driver.find_element(By.XPATH, "//*[@id='login']/div[1]/input")
    password_field = driver.find_element(By.XPATH, "//*[@id='login']/div[2]/input")

    username_field.send_keys("van.tram@protexxa.com")
    password_field.send_keys("5TV2MlbwRHFh")
    password_field.send_keys(Keys.RETURN)

    # Define a list of URLs to download from
    download_links = [
       "https://nitroflare.com/view/05A7F13B8CE68E3/Verifications.io_Database_Leaked_February_2019.part031.rar",
       "https://nitroflare.com/view/BEBEAB6A2D028CE/Verifications.io_Database_Leaked_February_2019.part032.rar",
       "https://nitroflare.com/view/620DC8D3ADD2736/Verifications.io_Database_Leaked_February_2019.part033.rar",
       "https://nitroflare.com/view/9C8DB646C24F4CA/Verifications.io_Database_Leaked_February_2019.part034.rar",
       "https://nitroflare.com/view/50D3A9E2FAFA62F/Verifications.io_Database_Leaked_February_2019.part035.rar",
       "https://nitroflare.com/view/7E599B74BF87150/Verifications.io_Database_Leaked_February_2019.part036.rar",
       "https://nitroflare.com/view/48CF5553F005826/Verifications.io_Database_Leaked_February_2019.part037.rar",
       "https://nitroflare.com/view/10A1645DBF71507/Verifications.io_Database_Leaked_February_2019.part038.rar",
       "https://nitroflare.com/view/B96FD810CD98F9A/Verifications.io_Database_Leaked_February_2019.part039.rar",
       "https://nitroflare.com/view/E82ED21B919B8E5/Verifications.io_Database_Leaked_February_2019.part040.rar",
       "https://nitroflare.com/view/9E1CB6DD13CACFD/Verifications.io_Database_Leaked_February_2019.part041.rar",
       "https://nitroflare.com/view/3E614D80B5CDF0C/Verifications.io_Database_Leaked_February_2019.part042.rar",
       "https://nitroflare.com/view/5805725D63A77F1/Verifications.io_Database_Leaked_February_2019.part043.rar",
       "https://nitroflare.com/view/BDCF4A75440B37F/Verifications.io_Database_Leaked_February_2019.part044.rar",
       "https://nitroflare.com/view/3D9069E2E8B1778/Verifications.io_Database_Leaked_February_2019.part045.rar",
       "https://nitroflare.com/view/B65A0DA2DEB813F/Verifications.io_Database_Leaked_February_2019.part046.rar",
       "https://nitroflare.com/view/2370E692837980A/Verifications.io_Database_Leaked_February_2019.part047.rar",
       "https://nitroflare.com/view/F8291AB4BDAFF52/Verifications.io_Database_Leaked_February_2019.part048.rar",
       "https://nitroflare.com/view/5DE82C8B8FEDBB1/Verifications.io_Database_Leaked_February_2019.part049.rar",
       "https://nitroflare.com/view/24C14E04055F29C/Verifications.io_Database_Leaked_February_2019.part050.rar",
       "https://nitroflare.com/view/DAA252D20A61FB2/Verifications.io_Database_Leaked_February_2019.part051.rar",
       "https://nitroflare.com/view/EB73FFC138C91BD/Verifications.io_Database_Leaked_February_2019.part052.rar",
       "https://nitroflare.com/view/BBEBE1681614430/Verifications.io_Database_Leaked_February_2019.part053.rar",
       "https://nitroflare.com/view/F26B945846C1F33/Verifications.io_Database_Leaked_February_2019.part054.rar",
       "https://nitroflare.com/view/D29E558E262C4BA/Verifications.io_Database_Leaked_February_2019.part055.rar",
       "https://nitroflare.com/view/6A99FA0F628EF79/Verifications.io_Database_Leaked_February_2019.part056.rar",
       "https://nitroflare.com/view/ABF3523664103AE/Verifications.io_Database_Leaked_February_2019.part057.rar",
       "https://nitroflare.com/view/E941A9A7A2F5315/Verifications.io_Database_Leaked_February_2019.part058.rar",
       "https://nitroflare.com/view/01DED508D958A75/Verifications.io_Database_Leaked_February_2019.part059.rar",
       "https://nitroflare.com/view/780A0F36A5E6261/Verifications.io_Database_Leaked_February_2019.part060.rar",
       "https://nitroflare.com/view/C8A40D902FC502C/Verifications.io_Database_Leaked_February_2019.part061.rar",
       "https://nitroflare.com/view/ECBE017D98BC3FD/Verifications.io_Database_Leaked_February_2019.part062.rar",
       "https://nitroflare.com/view/6C2A411D068F2AF/Verifications.io_Database_Leaked_February_2019.part063.rar",
       "https://nitroflare.com/view/162678813217563/Verifications.io_Database_Leaked_February_2019.part064.rar",
       "https://nitroflare.com/view/D610A35DF1EF868/Verifications.io_Database_Leaked_February_2019.part065.rar",
       "https://nitroflare.com/view/BC6F3D3808FC70A/Verifications.io_Database_Leaked_February_2019.part066.rar",
       "https://nitroflare.com/view/CB242BE8B27FA4B/Verifications.io_Database_Leaked_February_2019.part067.rar",
       "https://nitroflare.com/view/2953EAB10A37678/Verifications.io_Database_Leaked_February_2019.part068.rar",
       "https://nitroflare.com/view/4D61F909AAA86AD/Verifications.io_Database_Leaked_February_2019.part069.rar",
       "https://nitroflare.com/view/7B6555CA3168009/Verifications.io_Database_Leaked_February_2019.part070.rar",
       "https://nitroflare.com/view/13E33AB4FAB7199/Verifications.io_Database_Leaked_February_2019.part071.rar",
       "https://nitroflare.com/view/4AE78A00622784D/Verifications.io_Database_Leaked_February_2019.part072.rar",
       "https://nitroflare.com/view/0DE8C670CEC2B6E/Verifications.io_Database_Leaked_February_2019.part073.rar",
       "https://nitroflare.com/view/27DE9A424A04956/Verifications.io_Database_Leaked_February_2019.part074.rar",
       "https://nitroflare.com/view/D3400C28E89ACF2/Verifications.io_Database_Leaked_February_2019.part075.rar",
       "https://nitroflare.com/view/B2C24E2A8D7ACA6/Verifications.io_Database_Leaked_February_2019.part076.rar",
       "https://nitroflare.com/view/080DC40DAEAC96D/Verifications.io_Database_Leaked_February_2019.part077.rar",
       "https://nitroflare.com/view/D7AD3B7A8F805DF/Verifications.io_Database_Leaked_February_2019.part078.rar",
       "https://nitroflare.com/view/7DD43D6C5774767/Verifications.io_Database_Leaked_February_2019.part079.rar",
       "https://nitroflare.com/view/5100BB4E023611F/Verifications.io_Database_Leaked_February_2019.part080.rar",
       "https://nitroflare.com/view/2852CFE6C4E96ED/Verifications.io_Database_Leaked_February_2019.part081.rar",
       "https://nitroflare.com/view/E3E513739AC1675/Verifications.io_Database_Leaked_February_2019.part082.rar",
       "https://nitroflare.com/view/D18EA81FFB967BD/Verifications.io_Database_Leaked_February_2019.part083.rar",
       "https://nitroflare.com/view/068D51508B02C7F/Verifications.io_Database_Leaked_February_2019.part084.rar",
       "https://nitroflare.com/view/6F5E465B4670EED/Verifications.io_Database_Leaked_February_2019.part085.rar",
       "https://nitroflare.com/view/860F4DE9F7F8C57/Verifications.io_Database_Leaked_February_2019.part086.rar",
       "https://nitroflare.com/view/6DBAD9452ABF36C/Verifications.io_Database_Leaked_February_2019.part087.rar",
       "https://nitroflare.com/view/54528D8F0AA88A6/Verifications.io_Database_Leaked_February_2019.part088.rar",
       "https://nitroflare.com/view/CE4ABC3F70228FD/Verifications.io_Database_Leaked_February_2019.part089.rar",
       "https://nitroflare.com/view/FE59E837BAB8544/Verifications.io_Database_Leaked_February_2019.part090.rar",
       "https://nitroflare.com/view/F335E93C3D19D46/Verifications.io_Database_Leaked_February_2019.part091.rar",
       "https://nitroflare.com/view/C304BCF0344D980/Verifications.io_Database_Leaked_February_2019.part092.rar",
       "https://nitroflare.com/view/7D3AAC477E24C5E/Verifications.io_Database_Leaked_February_2019.part093.rar",
       "https://nitroflare.com/view/C6DE181C34A70B7/Verifications.io_Database_Leaked_February_2019.part094.rar",
       "https://nitroflare.com/view/774888E0F137C33/Verifications.io_Database_Leaked_February_2019.part095.rar",
       "https://nitroflare.com/view/1D3395FB33DF3E0/Verifications.io_Database_Leaked_February_2019.part096.rar",
       "https://nitroflare.com/view/8ADFD5D08878418/Verifications.io_Database_Leaked_February_2019.part097.rar",
       "https://nitroflare.com/view/C7E06573F1829B4/Verifications.io_Database_Leaked_February_2019.part098.rar",
       "https://nitroflare.com/view/00F401B6E4622F4/Verifications.io_Database_Leaked_February_2019.part099.rar",
       "https://nitroflare.com/view/5A134C4C065BDD0/Verifications.io_Database_Leaked_February_2019.part100.rar",
       "https://nitroflare.com/view/8F8514186CC248D/Verifications.io_Database_Leaked_February_2019.part101.rar",
       "https://nitroflare.com/view/09972B735D23BB8/Verifications.io_Database_Leaked_February_2019.part102.rar",
       "https://nitroflare.com/view/599D889CBF77064/Verifications.io_Database_Leaked_February_2019.part103.rar",
       "https://nitroflare.com/view/B91003CF64EBDE7/Verifications.io_Database_Leaked_February_2019.part104.rar",
       "https://nitroflare.com/view/41F8C102E3EE290/Verifications.io_Database_Leaked_February_2019.part105.rar",
       "https://nitroflare.com/view/15BBDBB79B91B4A/Verifications.io_Database_Leaked_February_2019.part106.rar",
       "https://nitroflare.com/view/B27A1AA263817D4/Verifications.io_Database_Leaked_February_2019.part107.rar",
       "https://nitroflare.com/view/DAFA1806D4B24B1/Verifications.io_Database_Leaked_February_2019.part108.rar",
       "https://nitroflare.com/view/948E6C76C3168C1/Verifications.io_Database_Leaked_February_2019.part109.rar",
       "https://nitroflare.com/view/14E00B9589E6755/Verifications.io_Database_Leaked_February_2019.part110.rar",
       "https://nitroflare.com/view/B4ACDBB41EB54E1/Verifications.io_Database_Leaked_February_2019.part111.rar",
       "https://nitroflare.com/view/5861D3674E6006C/Verifications.io_Database_Leaked_February_2019.part112.rar",
       "https://nitroflare.com/view/15D0BB38B2A76D3/Verifications.io_Database_Leaked_February_2019.part113.rar",
       "https://nitroflare.com/view/4027AA7B1405D4F/Verifications.io_Database_Leaked_February_2019.part114.rar",
       "https://nitroflare.com/view/11A5BB93BEF84A4/Verifications.io_Database_Leaked_February_2019.part115.rar",
       "https://nitroflare.com/view/44B61B8109EC966/Verifications.io_Database_Leaked_February_2019.part116.rar",
       "https://nitroflare.com/view/9BB1835C71D2970/Verifications.io_Database_Leaked_February_2019.part117.rar",
       "https://nitroflare.com/view/5F9CF74C2E7995D/Verifications.io_Database_Leaked_February_2019.part118.rar",
       "https://nitroflare.com/view/E16C9EAD0B4C78B/Verifications.io_Database_Leaked_February_2019.part119.rar",
       "https://nitroflare.com/view/4DBD0EC518C7566/Verifications.io_Database_Leaked_February_2019.part120.rar",
       "https://nitroflare.com/view/09737BA866C63C8/Verifications.io_Database_Leaked_February_2019.part121.rar",
       "https://nitroflare.com/view/8A2D9D3E1EF1607/Verifications.io_Database_Leaked_February_2019.part122.rar",
       "https://nitroflare.com/view/772CA4FA5DC2F2D/Verifications.io_Database_Leaked_February_2019.part123.rar",
       "https://nitroflare.com/view/9ACC868BB619090/Verifications.io_Database_Leaked_February_2019.part124.rar",
       "https://nitroflare.com/view/970BD34E72993DF/Verifications.io_Database_Leaked_February_2019.part125.rar",
       "https://nitroflare.com/view/4D2789744C3489D/Verifications.io_Database_Leaked_February_2019.part126.rar",
       "https://nitroflare.com/view/F5EA5E15187D7A2/Verifications.io_Database_Leaked_February_2019.part127.rar",
       "https://nitroflare.com/view/0F6A49669DD92E7/Verifications.io_Database_Leaked_February_2019.part128.rar",
       "https://nitroflare.com/view/BE30180C207D3E4/Verifications.io_Database_Leaked_February_2019.part129.rar",
       "https://nitroflare.com/view/F1955D858C809FB/Verifications.io_Database_Leaked_February_2019.part130.rar",
       "https://nitroflare.com/view/E1BCD90953AC107/Verifications.io_Database_Leaked_February_2019.part131.rar",
       "https://nitroflare.com/view/1B1E860F4760BF7/Verifications.io_Database_Leaked_February_2019.part132.rar",
       "https://nitroflare.com/view/C6189D75EFF612E/Verifications.io_Database_Leaked_February_2019.part133.rar",
       "https://nitroflare.com/view/BEF58503E45BDFE/Verifications.io_Database_Leaked_February_2019.part134.rar",
       "https://nitroflare.com/view/A5AC89C53A5E387/Verifications.io_Database_Leaked_February_2019.part135.rar",
       "https://nitroflare.com/view/2D58BFE3B32179B/Verifications.io_Database_Leaked_February_2019.part136.rar",
       "https://nitroflare.com/view/F763ADCA2929A27/Verifications.io_Database_Leaked_February_2019.part137.rar",
       "https://nitroflare.com/view/6B4D8600FD78054/Verifications.io_Database_Leaked_February_2019.part138.rar",
       "https://nitroflare.com/view/6FF0FFA234D3423/Verifications.io_Database_Leaked_February_2019.part139.rar",
       "https://nitroflare.com/view/8EBABF12C677165/Verifications.io_Database_Leaked_February_2019.part140.rar",
       "https://nitroflare.com/view/1438FA9350CD945/Verifications.io_Database_Leaked_February_2019.part141.rar",
       "https://nitroflare.com/view/88E6595AC67568C/Verifications.io_Database_Leaked_February_2019.part142.rar",
       "https://nitroflare.com/view/EEF5CD689BB26E2/Verifications.io_Database_Leaked_February_2019.part143.rar",
       "https://nitroflare.com/view/F1567E8A99B75BA/Verifications.io_Database_Leaked_February_2019.part144.rar",
       "https://nitroflare.com/view/1F89C1F7F06C11D/Verifications.io_Database_Leaked_February_2019.part145.rar",
       "https://nitroflare.com/view/0941322611794FC/Verifications.io_Database_Leaked_February_2019.part146.rar",
       "https://nitroflare.com/view/34ECF067C1F0235/Verifications.io_Database_Leaked_February_2019.part147.rar",
       "https://nitroflare.com/view/8ADDD31910FDA9A/Verifications.io_Database_Leaked_February_2019.part148.rar",
       "https://nitroflare.com/view/0905F3FA3739292/Verifications.io_Database_Leaked_February_2019.part149.rar",
       "https://nitroflare.com/view/986BC2C28A53F02/Verifications.io_Database_Leaked_February_2019.part150.rar",
       "https://nitroflare.com/view/4D1F05A9D694E62/Verifications.io_Database_Leaked_February_2019.part151.rar",
       "https://nitroflare.com/view/A533A47F6E2A87F/Verifications.io_Database_Leaked_February_2019.part152.rar",
       "https://nitroflare.com/view/025860737FB97B6/Verifications.io_Database_Leaked_February_2019.part153.rar",
       "https://nitroflare.com/view/93A1681EB66F6B8/Verifications.io_Database_Leaked_February_2019.part154.rar",
       "https://nitroflare.com/view/081AD24A0986E70/Verifications.io_Database_Leaked_February_2019.part155.rar",
       "https://nitroflare.com/view/07F122DAEA9CA8B/Verifications.io_Database_Leaked_February_2019.part156.rar",
       "https://nitroflare.com/view/428DFF9F2A7C76E/Verifications.io_Database_Leaked_February_2019.part157.rar",
       "https://nitroflare.com/view/B7768402FA2A173/Verifications.io_Database_Leaked_February_2019.part158.rar",
       "https://nitroflare.com/view/DF45AE41EEA5283/Verifications.io_Database_Leaked_February_2019.part159.rar",
       "https://nitroflare.com/view/22EE58D55BC897C/Verifications.io_Database_Leaked_February_2019.part160.rar",
       "https://nitroflare.com/view/F65B3C8B143E7BC/Verifications.io_Database_Leaked_February_2019.part161.rar",
       "https://nitroflare.com/view/2B8AB29DD3F8ECF/Verifications.io_Database_Leaked_February_2019.part162.rar",
       "https://nitroflare.com/view/FDEF3446A14E7F3/Verifications.io_Database_Leaked_February_2019.part163.rar",
       "https://nitroflare.com/view/4E9C7E5647C380B/Verifications.io_Database_Leaked_February_2019.part164.rar",
       "https://nitroflare.com/view/A8C697373497D13/Verifications.io_Database_Leaked_February_2019.part165.rar"
    ]

    # Loop through the list of URLs and download files
    for link in download_links:
        download_file(link)

    # # Once logged in, navigate to the page with the download link
    # driver.get("https://nitroflare.com/view/E21FA2E7C23B13A/Verifications.io_Database_Leaked_February_2019.part013.rar")

    # # Find the download link element using its attributes (you may need to inspect the webpage source)
    # download_link = driver.find_element(By.XPATH, "//*[@id='download']")

    # # Click the download link
    # download_link.click()

    #     # Wait for the download to complete (you can set a timeout)
    # time.sleep(30)  # Adjust the sleep time as needed

    # timeout = 60  # Set a reasonable timeout in seconds
    # try:
    #     WebDriverWait(driver, timeout).until(
    #         lambda x: "complete" in x.execute_script("return document.readyState")
    #     )
    #     print("File download completed.")
    # except TimeoutError:
    #     print("File download timed out.")

finally:
    # Close the web browser when done
    driver.quit()


