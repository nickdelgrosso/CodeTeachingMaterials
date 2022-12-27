from datetime import datetime

today = datetime.today()


rule all:
    input:  
        "requirements.txt",
        today.strftime("data/access_dates/zoom_meetings_downloaded_%Y-%m-%d.flag"),
        today.strftime("data/access_dates/all_registrations_downloaded_%Y-%m-%d.flag")
    run: 
        print("Done!")


rule download_meeting_list_from_zoom:
    output:
        today.strftime("data/access_dates/zoom_meetings_downloaded_%Y-%m-%d.flag")
    notebook:
        "scripts/get_meeting_info.py.ipynb"
        
    
rule download_registrations_for_each_meeting:
    output:
        today.strftime("data/access_dates/all_registrations_downloaded_%Y-%m-%d.flag")
    notebook:
        "scripts/download_all_registrations.py.ipynb"
        

rule extract_registrant_emails:
    output:
        today.strftime("data/registrant_emails/extracted_emails_%Y-%m-%d.flag")
    notebook:
        "scripts/extract_registrant_emails.py.ipynb"


rule download_participants_for_each_session:
    output:
        "data/downloaded_participants.flag"
    notebook:
        "scripts/download_participants.py.ipynb"