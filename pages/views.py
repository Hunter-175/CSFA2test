from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

#MySQL
import pymysql
mydb = pymysql.connect(host="localhost",
                       user="root",
                       password="Ninjamonkey123",
                       database= "restaurant"
                       )

curs = mydb.cursor()

mysql= {}

def CallDB():
    curs.execute("SELECT Name FROM items WHERE Type = 'Food'")
    elements = curs.fetchall()
    mysql.update({"food":elements})
    curs.execute("SELECT Name FROM items WHERE Type = 'Drink'")
    elements = curs.fetchall()
    mysql.update({"drink":elements})
    curs.execute("SELECT Rate FROM items WHERE Type = 'Food'")
    elements = curs.fetchall()
    mysql.update({"food_rate":elements})
    curs.execute("SELECT Rate FROM items WHERE Type = 'Drink'")
    elements = curs.fetchall()
    mysql.update({"drink_rate":elements})
    curs.execute("SELECT countnumber FROM record WHERE x = 'OrderNo'")
    elements = curs.fetchone()
    mysql.update({"orderno":elements})
    curs.execute("SELECT countnumber FROM record WHERE x ='count'")
    elements = curs.fetchone()
    mysql.update({"unique_count":elements})
    curs.execute("SELECT Number FROM tables WHERE Status='v'")
    elements= curs.fetchall()
    mysql.update({"table_num":elements})
    curs.execute("SELECT Type FROM tables WHERE Status='v'")
    elements= curs.fetchall()
    mysql.update({"table_type":elements})
    curs.execute("SELECT orderno FROM bill")
    elements= curs.fetchall()
    mysql.update({"bill_no":elements})
    curs.execute("SELECT item FROM bill")
    elements= curs.fetchall()
    mysql.update({"bill_item":elements})
    curs.execute("SELECT qty FROM bill")
    elements= curs.fetchall()
    mysql.update({"bill_qty":elements})
    
    

global amount, n, quanti
amount=0
n='s'
quanti=0

# Create your views here.

#ADMIN STUFF
def home_view(request): #done
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html",{})

def admin_view(request):#done
    return render(request, "admin.html",{})

def table_stat_view(request):#done
    CallDB

    def change():
        curs.execute("""
            UPDATE tables
            SET Status = %s
            WHERE Number = %s
        """, (TV, TN))
        mydb.commit()


    TN= request.POST.get("t_num")
    TV= request.POST.get("t_stat")
    value=str(request.POST.get("function"))
    if value=="Change":
        change()

    return render(request, "table_status.html",mysql)


def change_menu_view(request):#done
    CallDB()

    def deletion():
        t = (name)
        formula = "DELETE FROM items WHERE Name = %s"
        curs.execute(formula, t)
        mydb.commit()
    def updation():
        t = (new_name, price, ty, name)
        curs.execute("""
            UPDATE items
            SET ItemNumber=ItemNumber, Name=%s, Type=%s, Rate=%s
            WHERE Name=%s
        """, (new_name, ty, price, name))
        mydb.commit()
    def add():
        t = (item_num, name, ty, price)
        formula = "INSERT INTO `restaurant`.`items` (`ItemNumber`, `Name`, `Type`, `Rate`) VALUES (%s, %s, %s, %s)"
        curs.execute(formula, t)
        mydb.commit()


    name = request.POST.get('item')
    price = request.POST.get('price')
    ty = request.POST.get('type')
    item_num = request.POST.get('nit')
    new_name = request.POST.get('nname')
    value = str(request.POST.get('function'))

    if value == "Add Item":
        add()
    if value == "Update Item":
        updation()
    if value == "Delete Item":
        deletion()

    return render(request, "change_menu.html", mysql)


def all_bill_view(request):#done
    CallDB()
    return render(request, "a_bills.html", mysql)



#CUSTOMER STUFF
def customer_view(request):#done
    return render(request, "customer.html",{})

def menu_view(request):#done
    CallDB()
    return render(request, "menu.html", mysql)

def order_view(request):#done(!!!!first break then use!!!!)
    CallDB()
    
    def placeorder():
        curs.execute("UPDATE record SET countnumber = (countnumber + 1) WHERE x = 'OrderNo'")
        mydb.commit()    #ONLY ONE ITEM AT IN ONE ORDER NO!!!
        formula="UPDATE record SET countnumber = (countnumber + 1) WHERE x='count'"
        curs.execute(formula)
        mydb.commit()
        val = (uc, o, name, quantity)
        formula = "INSERT INTO `restaurant`.`bill` (`number`, `orderno`, `item`, `qty`) VALUES (%s, %s, %s, %s)"
        curs.execute(formula, val)
        mydb.commit()


        


    name= request.POST.get("item")
    mysql.update({"n":name})
    quantity= request.POST.get("qty")
    mysql.update({"q":quantity})
    price= (curs.fetchone())
    mysql.update({"a":amount})
    value = str(request.POST.get("function1"))
    print(name,quantity,value)
    o = mysql['orderno']
    uc = mysql['unique_count']
    
    if value == "placeorder":
        placeorder()
        return HttpResponseRedirect('/customer/bill/billresult/')

    

    return render(request, "order.html", mysql)


def table_view(request):#done
    CallDB()

    def BK():
        formula="UPDATE tables SET Status = 'nv' WHERE Number=%s" #nv= not vacant
        curs.execute(formula, TN)
        mydb.commit()

    TN= request.POST.get("table_num")
    value=str(request.POST.get("function"))
    if value=="Booktable":
        BK()

    return render(request, "c_table.html", mysql)



def bill1_view(request):#not done
    CallDB()

    def get_bill():
        global n, quanti, amount
        formula= "SELECT item FROM bill WHERE orderno =%s"
        curs.execute(formula, o)
        n=curs.fetchone()
        formula="SELECT qty FROM bill WHERE orderno=%s"
        curs.execute(formula, o)
        quanti= (curs.fetchone())[0]
        formula= "SELECT Rate FROM items WHERE Name=%s"
        curs.execute(formula, n)
        price= (curs.fetchone())[0]
        amount= quanti*price
        print (amount)


    o= request.POST.get('orderno')
    value= str(request.POST.get('function'))

    if value == "Get Bill":
        get_bill()

    return render(request, "bill.html", mysql)

def b1_view(request):#not done
    mysql.update({"n":'Pizza'})
    mysql.update({"q":3})
    mysql.update({"a":36})
    return render(request, "bill_result.html", mysql)