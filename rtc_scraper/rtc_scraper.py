from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "D:\\projects\\rtc_scraper\\chrome-win64\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://landrecords.karnataka.gov.in/Service2/")
    print("Page loaded.")

    old_year_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_MainContent_Tab3"))
    )
    old_year_button.click()
    print("Clicked Old Year tab.")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_ddlODist")))
    print("Old Year section loaded.")

    # Select district
    district_dropdown = driver.find_element(By.ID, "ctl00_MainContent_ddlODist")
    district_dropdown.click()
    driver.find_element(By.XPATH, "//option[text()='BANGALORE RURAL']").click()
    print("Selected District.")

    # Taluk
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ctl00_MainContent_ddlOTaluk")))
    taluk_dropdown = driver.find_element(By.ID, "ctl00_MainContent_ddlOTaluk")
    taluk_dropdown.click()
    driver.find_element(By.XPATH, "//option[text()='DEVANAHALLI']").click()
    print("Selected Taluk.")

    # Hobli
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ctl00_MainContent_ddlOHobli")))
    hobli_dropdown = driver.find_element(By.ID, "ctl00_MainContent_ddlOHobli")
    hobli_dropdown.click()
    driver.find_element(By.XPATH, "//option[text()='KASABA']").click()
    print("Selected Hobli.")

    # Village
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ctl00_MainContent_ddlOVillage")))
    village_dropdown = driver.find_element(By.ID, "ctl00_MainContent_ddlOVillage")
    village_dropdown.click()

    village_options = village_dropdown.find_elements(By.TAG_NAME, "option")
    for option in village_options:
        if option.text.strip().upper() == "DEVANAHALLI":
            option.click()
            print("Selected Village.")
            break

    try:
        survey_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_txtOSurveyNo"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", survey_input)
        survey_input.clear()
        survey_input.send_keys("22")
        print("Entered Survey No.")
    except Exception as e:
        print("⚠️ Could not enter survey number:", e)

    # Click the 'Go' button after entering Survey No.
    try:
        go_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_btnOGO"))
        )

    # Trigger the __doPostBack manually via JavaScript (safer for ASP.NET pages)
        driver.execute_script("__doPostBack('ctl00$MainContent$btnOGO', '')")
        print("Triggered Go via JS __doPostBack.")

    # Wait for the Surnoc dropdown to be enabled after postback
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_ddlOSurnocNo"))
        )
        print("Surnoc dropdown is now enabled.")

    except Exception as e:
        print("⚠️ Could not trigger 'Go' properly:", e)



    # Wait for
    from selenium.webdriver.support.ui import Select

# Wait for the dropdown to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_MainContent_ddlOSurnocNo"))
    )

# Select the dropdown using the Select class
    surnoc_dropdown = Select(driver.find_element(By.ID, "ctl00_MainContent_ddlOSurnocNo"))

# Select '*' using visible text
    surnoc_dropdown.select_by_visible_text("*")
    print("✅ Selected Surnoc '*' via Select class.")

# Wait a bit to let any onchange event fire
    time.sleep(2)

    # Hissa
    # Wait until the Hissa dropdown is enabled
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "ctl00_MainContent_ddlOHissaNo").is_enabled()
    )
    print("✅ Hissa dropdown is now enabled.")

# Now wait until it has more than 1 option (i.e., valid data)
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_element(By.ID, "ctl00_MainContent_ddlOHissaNo").find_elements(By.TAG_NAME, "option")) > 1
    )
    print("✅ Hissa dropdown populated.")

# Select Hissa using Select class
    from selenium.webdriver.support.ui import Select

    hissa_dropdown = Select(driver.find_element(By.ID, "ctl00_MainContent_ddlOHissaNo"))
    hissa_dropdown.select_by_visible_text("1A")
    print("✅ Selected Hissa.")


    # Period
    

# Wait until the Period dropdown is clickable
    period_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_MainContent_ddlOPeriod"))
    )

# Now select the period
    select = Select(period_dropdown)

# Select the period by visible text
    select.select_by_visible_text("2020-03-10 17:17:00 To 2023-08-28 13:55:00 (2023-2024 )")

# OR Select by value (if you know the exact value)
# select.select_by_value("1-32014")

    print("Period selected.")




    # Year
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ctl00_MainContent_ddlOYear")))
    year_dropdown = driver.find_element(By.ID, "ctl00_MainContent_ddlOYear")
    year_dropdown.click()
    driver.find_element(By.XPATH, "//option[text()='2023-2024']").click()
    print("Selected Year.")

    # Fetch
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ctl00_MainContent_btnOFetchDetails")))
    driver.find_element(By.ID, "ctl00_MainContent_btnOFetchDetails").click()
    print("Clicked Fetch.")

    time.sleep(5)
    print("✅ Done. Check browser window.")

except Exception as e:
    print("❌ Error occurred:", e)
    print("Keeping browser open for debugging.")
    input("Press Enter to quit...")

finally:
    driver.quit()
