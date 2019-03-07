# test_jublia
test backend engineering jublia

### send_email.py
has 2 modes: pusher and worker  
parameter  
- \-m: mode [pusher, worker] (required)  
- \-c: config file (default config.conf)

#### pusher

used to push job to queue. ran using cron every minute.  
`python send_mail.py -m pusher -c config.conf` 

#### worker

used to process job in the queue  
`python send_mail.py -m worker -c config.conf`

### flask_app.py

#### /save_emails
used to input scheduled emails