clientId = input("Enter client ID for the bot: ")
try:
    clientId = int(clientId)
except:
    print ("Invalid client ID!")


print("[0] No permissions, just an invite link")
print("[1] All permissions")
print("[2] Music bot permissions")
print("[3] Moderation bot permissions")

permLevel = input("Select permission level: ")
try:
    permLevel = int(permLevel)
except:
    print("Invalid permission level")

clientId = str(clientId)

if permLevel == 0:
    inviteLink = "https://discord.com/oauth2/authorize?client_id="+clientId+"&scope=bot&permissions=0"
    print("Invite link: ", inviteLink)
elif permLevel == 1:
    inviteLink = "https://discord.com/oauth2/authorize?client_id="+clientId+"&scope=bot&permissions=8589934591"
    print("Invite link: ", inviteLink)
elif permLevel == 2:
    inviteLink = "https://discord.com/oauth2/authorize?client_id="+clientId+"&scope=bot&permissions=2196835648"
    print("Invite link: ", inviteLink)
elif permLevel == 3:
    inviteLink = "https://discord.com/oauth2/authorize?client_id="+clientId+"&scope=bot&permissions=2926800326"
    print("Invite link: ", inviteLink)

customScope = input("Would you like to add a custom scope?[y/n]: ")
if customScope.lower()[0] == "y":
    scopeValue = input("Enter scope: ")
    inviteLink = inviteLink.replace("bot", scopeValue)
    print("New invite link: ", inviteLink)
else:
    print("No custom scope will be used.")

redirectURI = input("Would you like to use a redirect URI?[y/n]: ")
if redirectURI.lower()[0] == "y":
    redirectURIValue = input("Enter redirect URI: ")
    inviteLink = inviteLink + "&redirect_uri=" + redirectURIValue
    print("New invite link: ", inviteLink)
else:
    print("No redirect URI will be used.")

codeGrant = input("Would you like to require a code grant?[y/n]: ")
if codeGrant.lower()[0] == "y":
    inviteLink = inviteLink + "&response_type=code"
    print("New invite link: ", inviteLink)
else:
    print("No code grant will be used.")

print("Calculator complete, the final invite link is: ", inviteLink)


