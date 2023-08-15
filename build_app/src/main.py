import mysql.connector as mc
from fastapi import FastAPI

app = FastAPI()
go = 0
conn = "connection"
my_cur = "mysql cursor object"
while go == 0:
    try:
        conn = mc.connect(
            host="db", user="root", password="kali", database="pyAPI_detail"
        )
        my_cur = conn.cursor()
        go = 1
    except:
        pass


@app.get("/")
def get_main(id: int):
    d = "responce var"
    try:
        id = int(id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Data")
    found = 0
    my_cur.execute(f"select * from contact where id='{id}';")
    for i in my_cur:
        d = {"success": True, "responce": {"name": i[1], "contact": i[2], "addr": i[3]}}
        found += 1
    if found != 0:
        return d
    else:
        raise HTTPException(status_code=404, detail="User Not found")


@app.post("/")
def post_main(
    name: str | None = None, phone_num: str | None = None, addr: str | None = None
):
    if name == None or phone_num == None or addr == None:
        d = {"success": False, "reason": "Field Provided Are Empty"}
        return d
    try:
        name = str(name)
        phone_num = str(phone_num)
        addr = str(addr)
    except:
        d = {"success": False, "reason": "Invalid Data"}
        return d
    my_cur.execute(
        f"insert into contact(id,name,phone_num,addr) values(DEFAULT,'{name}','{phone_num}','{addr}');"
    )
    conn.commit()
    my_cur.execute(f"select id from contact where phone_num='{phone_num}';")
    d = "result to sent"
    for r in my_cur:
        d = {"success": True, "responce": {"id": r[0]}}
    return d


@app.delete("/")
def del_main(id: int):
    try:
        id = int(id)
    except:
        d = {"success": False, "reason": "Invalid Data"}
        return d
    found = 0
    my_cur.execute(f"select id from contact where id='{id}';")
    for i in my_cur:
        found += 1
    if found != 0:
        my_cur.execute(f"DELETE FROM contact where id={id}")
        conn.commit()
        d = {"success": True, "responce": "Removed ID {}".format(id)}
        return d
    else:
        raise HTTPException(status_code=404, detail="User Not found")


@app.put("/")
def put_main(
    id: int,
    name: str | None = None,
    phone_num: str | None = None,
    addr: str | None = None,
):
    if name == None and phone_num == None and addr == None:
        d = {"success": False, "reason": "Field Empty"}
        return d
    try:
        id = int(id)
        name = str(name)
        phone_num = str(phone_num)
        addr = str(addr)
    except:
        d = {"success": False, "reason": "Invalid Data"}
        return d

    found = 0
    my_cur.execute(f"select id from contact where id='{id}';")
    for i in my_cur:
        found += 1
    if found != 0:
        update_elements = list()
        if name != None:
            # for making the parameter i.e name,phone_num,.. into string to use in query
            n = f"{name=}".split("=")[0]
            update_elements.append(f"{n}='{name}'")
        if phone_num != None:
            n = f"{phone_num=}".split("=")[0]
            update_elements.append(f"{n}='{phone_num}'")
        if addr != None:
            n = f"{addr=}".split("=")[0]
            update_elements.append(f"{n}='{addr}'")
        final_update_elements = ",".join(update_elements)
        my_cur.execute(f"UPDATE contact SET {final_update_elements} where id={id};")
        conn.commit()
        d = {"success": True, "responce": "Updated ID {}".format(id)}
        return d
    else:
        raise HTTPException(status_code=404, detail="User Not found")