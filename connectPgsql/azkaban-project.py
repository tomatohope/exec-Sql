# coding: utf-8
import os

# get session id, notice: account pass info read from config file
# getSessinId = str("curl -k -X POST --data \"action=login&username=azkaban&password=azkaban\" http://192.168.43.63:8081/")
# print("getSessinIdCmd:", getSessinId)
# os.system(getSessinId)
sessionId = "510532ed-0df1-4a2f-a475-0c1547e788b8"

for i in range(31, 61):
    print("i: ", i)

    # # createProject
    # createProject = str("curl -k -X POST --data \"session.id="）+ str(sessionId) + str("&name=aaaa  ") + str(i) + str("&description=test\" http://192.168.43.63:8081/manager?action=create")
    # print("createProjectCmd: ", createProject)
    # os.system(createProject)
    #
    # # uploadfile
    # uploadfile = str("curl -k -i -X POST --form 'session.id=") + str(sessionId) + str("' --form 'ajax=upload' --form 'file=@flow1.zip;type=application/zip' --form 'project=aaaa") + str(i) + str("' http://192.168.43.63:8081/manager")
    # print("uploadfileCmd: ", uploadfile)
    # os.system(uploadfile)

    #deleteProject
    # deleteProject = str("curl -k --get --data \"session.id=") + str(sessionId) + str("&delete=true&project=aaaa") + str(i) + str("\" http://192.168.43.63:8081/manager")
    # print("deleteProjectCmd: ", deleteProject)
    # os.system(deleteProject)

    #schedule parameter projects
    projectId = int(i)
    schedule = str("curl -k http://192.168.43.63:8081/schedule -d \"ajax=scheduleFlow&is_recurring=on&period=1m&flowOverride[database]=dev_jing_dw&flowOverride[user]=postgres&flowOverride[password]=postgres&flowOverride[host]=192.168.43.63&flowOverride[port]=5432&flowOverride[sqlfile]=/tmp/3.sql&projectName=aaaa") + str(i) + str("&flow=flow1&projectId=") + str(projectId) + str("&scheduleTime=16,59,pm,PDT&scheduleDate=02/12/2020\" -b azkaban.browser.session.id=") + str(sessionId)
    print("scheduleCmd:", schedule)
    os.system(schedule)

    #unschedule parameter projects
    # scheduleId = int(i) + 520
    # unschedule = str("curl -k http://192.168.43.63:8081/schedule -d \"action=removeSched&scheduleId=") + str(scheduleId) + str("\" -b azkaban.browser.session.id=") + str(sessionId)
    # print("unscheduleCmd:", unschedule)
    # os.system(unschedule)