from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from app.models.schemas import WorldBankItem, WorldBankResponse
from app.models.value_objects import IneligibilityPeriod

def search(input: str):
    driver = webdriver.Chrome()
    URL = "https://projects.worldbank.org/en/projects-operations/procurement/debarred-firms"
    driver.get(URL)

    time.sleep(4)

    search_input = driver.find_element(By.ID, "category")
    search_input.send_keys(input)

    time.sleep(1)

    table = driver.find_element(By.ID, "k-debarred-firms")
    table_body = table.find_element(By.TAG_NAME, "tbody")
    rows = table_body.find_elements(By.TAG_NAME, "tr")

    worldBankItems = []

    for row in rows:
        result = []
        columns = row.find_elements(By.TAG_NAME, "td")

        for column in columns:
            result.append(column.text)

        ineligibilityPeriod = IneligibilityPeriod(fromDate= result[4], toDate=result[5])
        worldBankItem = WorldBankItem(firmName=result[0], address=result[2], country=result[3], ineligibilityPeriod=ineligibilityPeriod, grounds=result[6])
        worldBankItems.append(worldBankItem) 

    worldBankResponse = WorldBankResponse(size=len(worldBankItems), worldBankItems=worldBankItems)

    return worldBankResponse