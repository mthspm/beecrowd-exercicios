import os as os

#set the path using this formatting to the workshop content folder. this is the default
path = 'D:/SteamLibrary/steamapps/workshop/content/108600'

#initialize variables
WorkshopItemList = (os.listdir(path))
WorkshopItems = ""
ModIds = ""
Maplist: str = ""

#make the workshop list
for i in range(len(WorkshopItemList)):
    WorkshopItems += WorkshopItemList[i]
    WorkshopItems += ";"

#make the modlist and maplist
for i in range(len(WorkshopItemList)):
    subdir = (os.listdir(path + "/" + WorkshopItemList[i] + "/mods"))
    for j in range(len(subdir)):
        modinfopath = (path + "/" + WorkshopItemList[i] + "/mods/" + subdir[j] + "/mod.info")
        modinfo = open(modinfopath, 'r', encoding="utf8")
        lines = modinfo.readlines()
        for k in lines:
            if k.startswith("id="):
                ModIds += k.removeprefix("id=").strip()
                ModIds += ";"
        check_file = os.path.exists(path + "/" + WorkshopItemList[i] + "/mods/" + subdir[j] + "/media/maps")
        if check_file:
            maps = (os.listdir(path + "/" + WorkshopItemList[i] + "/mods/" + subdir[j] + "/media/maps"))
            for l in maps:
                Maplist += l
                Maplist += ';'

        modinfo.close()

#console out
mods_ids = ModIds.split(";")
map_list = Maplist.split(";")
