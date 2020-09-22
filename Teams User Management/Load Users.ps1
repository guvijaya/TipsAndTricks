# https://docs.microsoft.com/en-us/powershell/module/teams/add-teamuser?view=teams-ps

# Load Module
# Get-Module -Name MicrosoftTeams

# Sign-in
#Connect-MicrosoftTeams

# Get params
Write-Host "Goto to teams, right click on team name, Click on ... select Get team link"
Write-Host "Grap the groupId from the URL"
Write-Host ""
$GroupId = Read-Host -Prompt 'Enter the Teams Group Id Guid'

# Define verification regex
[regex]$guidRegex = '(?im)^[{(]?[0-9A-F]{8}[-]?(?:[0-9A-F]{4}[-]?){3}[0-9A-F]{12}[)}]?$'

# Check guid against regex
if ($GroupId -notmatch $guidRegex) {
    Write-Host 'Invalid guid. Please enter valid Group Id'
    return
}

Write-Host ""
Write-Host "Open the channel and copy the channel name"
$ChannelName = Read-Host -Prompt 'Enter the Teams Channel Name'

Write-Host $GroupId
Write-Host $ChannelName

$runfilename = "Log" + $(((get-date).ToUniversalTime()).ToString("yyyyMMddTHHmmssZ")) + ".log"
$runErrorfilename = "Log" + $(((get-date).ToUniversalTime()).ToString("yyyyMMddTHHmmssZ")) + "_Error.log"

# Add user to Group and Channel
foreach($email in Get-Content .\emailids.txt) {
    try{
		Write-Host "$email geting added to the team"
        Add-TeamUser -GroupId $GroupId -User $email
        Add-Content -Path $runfilename -Value ($email + ",Added To Group")
        Add-TeamChannelUser -GroupId $GroupId -DisplayName $ChannelName -User  $email

        Add-Content -Path $runfilename -Value ($email + ",Added To Channel")
    }catch{
        $_.Exception | Out-File $runErrorfilename -Append
        Add-Content -Path $runfilename -Value ($email + ",Error")
		
		Write-Host "Failed to add users to the group.  Please see the $runErrorfilename file for more info"
    }
}