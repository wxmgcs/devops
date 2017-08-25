import mysql_helper

def get_genorder_status(minute):
    sql = ''' SELECT vpn_code,count(*) as count
    FROM monitor_unicomrechargegenorder where create_time>=DATE_SUB(NOW(),INTERVAL %s MINUTE) group by vpn_code;'''%(minute)
    return mysql_helper.execute_sql(sql)