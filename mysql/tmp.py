# -*- coding:utf8 -*-
a = (('information_schema',), ('activemq',), ('activemq_yacht',), ('activiti',), ('activity',), ('agent',),
     ('announcement',), ('arrow',), ('callcenter',), ('captain',), ('cc_service',), ('classroom_data',),
     ('curriculum',), ('customer_service',), ('flow',), ('goblin',), ('homework',), ('leads',), ('learning',),
     ('lingobus',), ('manager_clt',), ('manager_service',), ('manager_work',), ('message_center',),
     ('mgt_announcement',), ('mgt_tmk',), ('mysql',), ('mysqlslap',), ('occamy',), ('parent_rest',), ('payroll',),
     ('performance_schema',), ('qa_base',), ('qos',), ('retrench',), ('salesreport',), ('sayabc_crm',),
     ('sayabc_crm_processor',), ('sso',), ('student_behavior',), ('teacher',), ('teacher_activity',),
     ('teacher_evaluation',), ('teacher_payroll',), ('teacher_recruitment',), ('test',), ('uc_event',), ('uc_rom',),
     ('usercenter',), ('vipkid',), ('vipkid_class',), ('vipkid_followup',), ('vipkid_mail',), ('vschedule',),
     ('vschedule_new',), ('wb',), ('wechat',), ('yacht',))
print list(a)

provinces = [u'山东省', u'山西省',u'北京市']
for i in provinces:
    print '%s' % (i.replace(u'省', '').replace(u'市', ''))
print u'\u5c71\u897f\u7701'