# Register Repo
Register-PSRepository -Name PSGalleryInt -SourceLocation https://www.poshtestgallery.com/ -InstallationPolicy Trusted

# Install Teams Module
Install-Module -Name MicrosoftTeams -Repository PSGalleryInt -Force
