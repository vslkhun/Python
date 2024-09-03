import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import customtkinter as ctk

global CONFIRM_FLAG, DELAY
CONFIRM_FLAG = False
DELAY = 6
# Function to send WhatsApp message
def send_whatsapp_message(driver,name, phone_number, message):
    try:
        # Navigate to WhatsApp Web
        driver.get("https://web.whatsapp.com/")
        
        # Wait for the user to scan the QR code
        # confirm_send(message)
        input(f'Scan QR and Confirm msg and press Enter : \n{message} : ')
        # Construct the WhatsApp URL with the phone number
        url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"
        
        # Open the URL
        driver.get(url)
        
        # Wait for the send button to appear
        send_button_xpath = '//span[@data-icon="send"]'
        send_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, send_button_xpath)))
        
        # Click the send button using JavaScript
        driver.execute_script("arguments[0].click();", send_button)
        
        print(f"Message sent to {name} {phone_number}")
        return True
    
    except Exception as e:
        print(f"Error sending message to {phone_number}: {str(e)}")
        return False

# Function to confirm scanning QR code
# def confirm_scan():
#     root = ctk.TopCTk()
#     root.withdraw()
#     messagebox.showinfo("WhatsApp Web", "Please scan the QR code and click OK to continue.")
#     root.destroy()
#for pop up msg for info
def popup(msg):
    popup_win =ctk.CTkToplevel()
    popup_win.attributes('-topmost', 'true')
    popup_win.wm_title("Info")
    label= ctk.CTkLabel(popup_win, text=msg)
    label.grid(row=0, column=0,padx=20,pady=10)
    button = ctk.CTkButton(popup_win, text="Okay", command=popup_win.destroy)
    button.grid(row=1, column=0,padx=20,pady=10)    
def confirm_send(msg):
    popup_win =ctk.CTkToplevel()
    popup_win.attributes('-topmost', 'true')
    popup_win.wm_title("Scan QR and confrim message")
    label= ctk.CTkLabel(popup_win, text=msg)
    label.grid(row=0, column=0,padx=20,pady=10)
    def okay_clicked():
        global CONFIRM_FLAG
        CONFIRM_FLAG = True
        popup_win.destroy()
    button = ctk.CTkButton(popup_win, text="Okay", command=okay_clicked)
    button.grid(row=1, column=0,padx=20,pady=10)        
# Main function to read CSV and send messages
def main(csv_file,  delay_seconds, msg):
    # Read CSV file into pandas DataFrame
    
    # Initialize Chrome WebDriver
    driver = webdriver.Edge()  # Change to webdriver.Chrome() or your preferred WebDriver
    if not  csv_file.empty:
        # Iterate through each row in the DataFrame
        for index, row in csv_file.iterrows():
            contact_name = row['Name']
            phone_number = row['Phone']  # Assuming 'Phone' column contains phone numbers
            greeting_message = f"""Hi {contact_name.capitalize()}, {msg}                                                                   Thanks & regards                                         NIELIT Imphal.Akampat"""
            print(greeting_message)
            # Send WhatsApp message
            if send_whatsapp_message(driver,contact_name, phone_number, greeting_message):
                time.sleep(delay_seconds)  # Delay between messages
        
        # Close the WebDriver
        driver.quit()
def load_csv(text):
    global CSV_FILE
    filename = ctk.filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")], title="Select CSV File")
    if filename:
        csv_file = pd.read_csv(filename)
        msg = text.get("1.0", "end-1c")
        if len(msg)>0:
            main(csv_file,DELAY,msg)
        else:
            popup('Empty message.')
    else:
        popup('No valid file selected.')
if __name__ == "__main__":
    window=ctk.CTk()
    window.geometry('750x430')
    window.title("Send Whatsapp message using CSV contacts.")
    ctk.set_appearance_mode('Light')
    l=ctk.CTkLabel(window, text = 'Send Whatsapp message using CSV contacts.', font=('Impact',30))
    l.grid(row = 0, column = 0, columnspan = 3,padx = 10,pady = 40)
    lt=ctk.CTkLabel(window, text = 'Enter your message here.', font=('Verdana',17))
    lt.grid(row = 1, column = 0,padx = 10,pady = 10)
    text = ctk.CTkTextbox(window, width=400,height = 200, corner_radius=10)
    text.grid(row=1, column=1, padx=10, columnspan =2, pady=10,sticky="w")
    l2 = ctk.CTkLabel(window, text = 'Select your Contact file in csv : ', font=('Verdana',17))
    l2.grid(row = 2, column =0, padx = 20, pady = 20)
    btn = ctk.CTkButton(window, text = 'open', command = lambda : load_csv(text))
    btn.grid(row = 2, column = 1, padx = 10, pady = 10)
    window.mainloop()

