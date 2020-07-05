  # Intelligent Post-Lock Down Management System for Public Transportation
- Post-Lockdown, it will be risky to allow the public transportation without proper mechanism to maintain the social distancing, especially the frequency of buses, trains and     metros shall be managed properly to utilize the capacity with social distancing criteria. The transport authorities must integrate together to maintain the system properly.

  ## Tools Used
- IBM Watson Assistant, Python 2 or 3, IBM Watson Studio, IBM Cloud for Deployment, Any Web / Mobile app frameworks
  ## Structure and Implimentation-
   ![Image of System-1](https://github.com/deathook007/Covid-19_ChainBreakers-CoronaBot/blob/master/images/Capture-2.PNG)
   ![Image of System-2](https://github.com/deathook007/Covid-19_ChainBreakers-CoronaBot/blob/master/images/Capture-1.PNG)

  ## Features
- This Bot is designed to provide the coronavirus updates and works as a post lockdown management system in whole.
- Too many updates? Don't worry! Subscribe only to the states that you want only
- Reliablity- The source of data is official Government site ([here](https://mohfw.gov.in/))
- Its ROBUST and QUICK!
  - What if script fails? What if the Govt website changes format?
  -- You get Slack notifications about the exceptions too.
  -- You have log files (check `bot.log`) too, to evaluate what went wrong
  
# Get Slack notifications
  -  Notify whenever there are new cases in India
  -  How many Indian nationals have Corona Virus per State?
  -  How many deaths happened per State?
  -  The new States entering the corona zone like Chattisgarh (As per recorded data)
    ![Image of Slack](https://github.com/deathook007/Covid-19_ChainBreakers-CoronaBot/blob/master/images/Capture-01.png)
    ![Image of Slack](https://github.com/deathook007/Covid-19_ChainBreakers-CoronaBot/blob/master/images/Capture-03.png)
    ![Image of Slack](https://github.com/deathook007/Covid-19_ChainBreakers-CoronaBot/blob/master/images/Capture-02.png)  
  
  ## Installation
- You need Python
- You need a Slack account + Slack Webhook to send slack notifications to your account
- Install dependencies by running
```bash
pip install tabulate
pip install requests
pip install beautifulsoup4
```
- Clone this repo and create auth.py
- Write your Slack Webhook into auth.py

- Setup the cron job to receive updates whenever something changes
```bash
crontab -e # opens an editor like vim or nano
# now write the following to run the bot every 5 mins
*/5 * * * * cd $PATH_TO_CLONE_DIR; python3 corona_bot.py --states 'haryana,maharashtra'
# to receive updates for all states, ignore the --states flag
```

## Reference
- https://www.transformative-mobility.org/news/the-covid-19-outbreak-and-implications-to-public-transport-some-observations
- https://www.teriin.org/article/effects-covid-19-transportation-demand
- https://www.uitp.org/public-transport-and-covid-19
- https://www.uitp.org/management-covid-19-guidelines-public-transport-operators

