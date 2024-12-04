#Imports
import asyncio
import roblox
from roblox import Client

#Set
roclient = Client("")

#Funcs
async def checktheguy(artthousname):
    checkperson = await roclient.get_user_by_username(artthousname)
    thousgroups = [role.group.name for role in await checkperson.get_group_roles()]
    thousgroupsroles = [role for role in await checkperson.get_group_roles()]
    if "Tom's Takeout" in thousgroups:
        whichnombre = thousgroups.index("Tom's Takeout")
        sirsrole = thousgroupsroles[whichnombre].name
        if sirsrole in ["Suspended", "Trainee", "Employee", "Senior Employee", "Supervisor", "Head Supervisors", "Manager", "Vice Chairman", "Chairman"]:
            print(f"In group as {sirsrole}")
        else:
            print("In group not as employee")
    else:
        print("Not in group")

#Program
checkpersonname = input("Name:")
asyncio.run(checktheguy(checkpersonname))
ag = input("Close")