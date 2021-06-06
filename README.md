# osuDCBot
This a discord bot for displaying osu! scores.

**Setup:**
- Install requirements: pip install -r requirements.txt
- Put your DC API key in "dc_api_key.txt" 
- Put your osu! API key in "osu_api_key.txt" 
- Put your desired discord text channel id in "osu_text_channel_id.txt" 
- Run script with: python main.py 

**Commands:** 
*(This commands will work everywhere on the server)*

 - **!osuadd** <your_osu_profile_link>   Links your osu profile to your
   dc_id
 - **!osuremove** Removes your osu profile from your dc_id

Every **10** seconds the script will send an embed with all the score details to your desired text channel, unless there are no new scores. 
**Every day** the osu bearer token will refresh. 
Request/min = 6*users
