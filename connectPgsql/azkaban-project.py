# coding: utf-8
import os

# get session id, notice: account pass info read from config file
# getSessinId = str("curl -k -X POST --data \"action=login&username=azkaban&password=azkaban\" http://192.168.43.63:8081/")
# print("getSessinIdCmd:", getSessinId)
# os.system(getSessinId)
sessionId = "32869fd5-b3b9-485b-96db-b026643b6ffe"

for i in range(1, 101):
    print("i: ", i)
    #
    # # createProject
    # createProject = str("curl -k -X POST --data \"session.id=") + str(sessionId) + str("&name=aaaa") + str(i) + str("&description=test\" http://10.80.0.231:8081/manager?action=create")
    # print("createProjectCmd:", createProject)
    # os.system(createProject)
    #
    # # uploadfile
    # uploadfile = str("curl -k -i -X POST --form 'session.id=") + str(sessionId) + str("' --form 'ajax=upload' --form 'file=@test-flow-mysql.zip;type=application/zip' --form 'project=aaaa") + str(i) + str("' http://10.80.0.231:8081/manager")
    # print("uploadfileCmd: ", uploadfile)
    # os.system(uploadfile)

    #deleteProject
    # deleteProject = str("curl -k --get --data \"session.id=") + str(sessionId) + str("&delete=true&project=aaaa") + str(i) + str("\" http://10.80.0.231:8081/manager")
    # print("deleteProjectCmd: ", deleteProject)
    # os.system(deleteProject)

    #schedule parameter projects Pgsql
    # projectId = int(i) + 2
    # schedule = str("curl -k http://10.80.0.231:8081/schedule -d \"ajax=scheduleFlow&is_recurring=on&period=1h&flowOverride[database]=dev_jms_dw&flowOverride[user]=dev_jms_dw_owner&flowOverride[password]=C#UzrAyBstcV6Dpp&flowOverride[host]=gp-uf6fw1e6xv35ikrj9.gpdb.rds.aliyuncs.com&flowOverride[port]=3432&flowOverride[sqlfile]=/opt/services/azkaban/azkaban-exec-server/build/install/azkaban-exec-server/bin/sql/test-sql.sql&projectName=aaaa") + str(i) + str("&flow=test-flow&projectId=") + str(projectId) + str("&scheduleTime=02,42,am,PDT&scheduleDate=02/21/2020\" -b azkaban.browser.session.id=") + str(sessionId)
    # print("scheduleCmd:", schedule)
    # os.system(schedule)

    #schedule parameter projects Mysql
    # projectId = int(i) + 104
    # schedule = str("curl -k http://10.80.0.231:8081/schedule -d \"ajax=scheduleFlow&is_recurring=on&period=1h&flowOverride[database]=dev_dw&flowOverride[user]=dev_ads_mysql&flowOverride[password]=gAwEb178XHc3Ir8L&flowOverride[host]=am-uf68cpts08jf19trn131910.ads.aliyuncs.com&flowOverride[sqlfile]=/opt/services/azkaban/azkaban-exec-server/build/install/azkaban-exec-server/bin/sql/Mysql-test-sql.sql&projectName=aaaa") + str(i) + str("&flow=test-flow&projectId=") + str(projectId) + str("&scheduleTime=19,34,pm,PDT&scheduleDate=02/21/2020\" -b azkaban.browser.session.id=") + str(sessionId)
    # print("scheduleCmd:", schedule)
    # os.system(schedule)

    #unschedule parameter projects
    scheduleId = int(i) + 464
    unschedule = str("curl -k http://10.80.0.231:8081/schedule -d \"action=removeSched&scheduleId=") + str(scheduleId) + str("\" -b azkaban.browser.session.id=") + str(sessionId)
    print("unscheduleCmd:", unschedule)
    os.system(unschedule)
