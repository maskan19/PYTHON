# DB에 저장되어 있는 값을 불러오기
import pymysql


class MyEmpDao: 

    def __init__(self):
        pass
    def getEmp(self):
        ret=[]
        conn = pymysql.connect(
            user='root', 
            passwd='python', 
            host='127.0.0.1', 
            db='python', 
            charset='utf8'
        )
        cursor = conn.cursor()
        
        sql = "SELECT sabun, name, dept, mobile FROM emp"
        cursor.execute(sql)
        result = cursor.fetchall()
        for e in result:
            temp = {'sabun' : e[0], 'name' : e[1], 'dept' : e[2], 'mobile' : e[3]}
            ret.append(temp)
        conn.close()
        return ret
    
    def insEmp(self, sabun, name, dept, mobile):
        conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
        curs = conn.cursor()
        sql = "insert into emp(sabun, name, dept, mobile) values (%s, %s, %s, %s)"
        cnt = curs.execute(sql, (sabun, name, dept, mobile))
        conn.commit()
        conn.close()
        return cnt
    
    def updEmp(self, sabun, name, dept, mobile):
        conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
        curs = conn.cursor()
        sql = "update emp set name=%s, dept=%s, mobile=%s where sabun=%s"
        cnt = curs.execute(sql, (name, dept, mobile,sabun))
        conn.commit()
        conn.close()
        return cnt
    
    def delEmp(self, sabun):
        conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
        curs = conn.cursor()
        sql = "delete from emp where sabun=%s"
        cnt = curs.execute(sql, (sabun))
        conn.commit()
        conn.close()
        return cnt

if __name__ == '__main__':
    list = MyEmpDao().getEmp()
    print(list)
    # inscnt = MyEmpDao().insEmp('2', '2','22','2')
    # print(inscnt)
    updcnt = MyEmpDao().updEmp('2', '5','5','2')
    print(updcnt)
    # delcnt = MyEmpDao().delEmp('3')
    # print(delcnt)
