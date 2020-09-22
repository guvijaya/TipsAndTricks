# Using the script
## Downloading the script
* This PowerShell scripts helps to add list of users to a Teams Group & Teams channel.
* Copy all the script to local. 
* You can navigate to https://github.com/guvijaya/TipsAndTricks and Use Download ZIP button
* <img src=Download.png height=200/>
* Make sure the download complete and you unziped the file.

## PowerShell
* There are two scripts, we need to execute one by one.
* Open PowerShell prompt as administrator
* <img src=StartPowerShell.png height=200/>
* Set the execution policy. As we are going to run the PS1 files it is required. Execute the below command and answer Y for the confirmation question.
* set-ExecutionPolicy Unrestricted 
* <img src=Policy.png width=500>
* Switch to the folder, where you downloaded the scripts.
* PS C:\Users\guvijaya> cd 'C:\Users\guvijaya\Downloads\TipsAndTricks-master\TipsAndTricks-master\Teams User Management'

## Install Required Modules
* run Install Module.ps1 from Power Shell prompt. by running below command 
* & '.\Install Module.ps1' 
* For the confirmation question answer it as R
* <img src=InstallModule.png width=600/>
* Please make sure the module install successfull, prior to the next step. 
* Run the below command to make sure the module installed properly and you could able to connect to Teams from PowerShell
* Connect-MicrosoftTeams
* The command will prompt you AAD login flow. Please complete the login.

## Adding users to Teams
* Open the emailids.txt file, add all email ids you want to add to the Teams Group.
* Make sure you got the Group Id, Channel name
* <img src=Link.png height=200/>
* The link will be in this format.  From this long string, just copy the GroupId Guid. https://teams.microsoft.com/l/team/19%3a2d0cd698e17144d8af505bfffd9bfd7e%40thread.skype/conversations?groupId=86acf58f-56d7-41b1-985d-7f296e8dec29&tenantId=0db0ed71-ff8f-4370-b899-52de0b6018c5.  For example in this link 86acf58f-56d7-41b1-985d-7f296e8dec29& is the group id.
* Execute the Load Users.ps1 by running below command 
* & '.\Load Users.ps1' 
* For the confirmation question answer it as R
* <img src=LoadUsers.png width=600/>
* Enter the Group Id, Channel name which got in previous step. 
* The file produces Execution log and error log with time stamp. Check out the file to see is your operation successful.

If you are looking for a demo. Check here https://www.youtube.com/watch?v=Vn3PfOIz_5I