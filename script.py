from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(
    format="[%(levelname)s] copilot-history-wipe: %(message)s", level=logging.INFO
)

logging.info("Script started")
try:
    driver = webdriver.Edge()
    logging.info("Opened Edge browser")
    driver.get("https://www.bing.com/chat?form=NTPCHB")
    logging.info("Opened Bing Chat")
    while (
        not input(
            "Sign into your Microsoft account before proceeding. Proceed? (y/n) "
        ).lower()
        == "y"
    ):
        pass
    while (
        not input(
            "Make sure the 'Recents' panel containing your recent chats is visible. You can reload the page if it's not there. Proceed? (y/n) "
        ).lower()
        == "y"
    ):
        pass
    first_run = True
    while (
        True
        if first_run
        or input(
            "DONE. Reload the page to see if there's more and press ENTER to run the script once more.\nTo quit, interrupt python (Ctrl+C)"
        )
        else True
    ):
        side_panel_shadow_root = (
            driver.find_element(By.CSS_SELECTOR, ".cib-serp-main")
            .shadow_root.find_element(By.CSS_SELECTOR, "cib-side-panel")
            .shadow_root
        )
        try:
            show_recent_btn = side_panel_shadow_root.find_element(
                By.CSS_SELECTOR, ".show-recent"
            )
            if show_recent_btn.text == "See all recent chats":
                show_recent_btn.click()
                logging.info("Clicked 'See all recent chats' button")
            else:
                logging.warning(
                    "Assume 'See all recent chats' button is already clicked"
                )
        except:
            raise Exception("'See all recent chats' button not found")
        cib_thread_hosts = side_panel_shadow_root.find_elements(
            By.CSS_SELECTOR, "cib-thread"
        )
        count = 0
        for th in cib_thread_hosts:
            driver.execute_script(
                "arguments[0].click();",
                th.shadow_root.find_element(By.CSS_SELECTOR, ".delete.icon-button"),
            )
            count += 1
            logging.info(f"Deleted a chat (Total: {count})")
        first_run = False
except KeyboardInterrupt:
    logging.info("Quitting on keyboard interrupt...")
    driver.quit()
except Exception as e:
    logging.exception(e)
    logging.info("Quitting on error...")
