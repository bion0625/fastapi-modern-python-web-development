from fastapi import FastAPI, Depends, Query

def depfunc1():
    pass

def depfunc2():
    pass

app = FastAPI(dependencies=[Depends(depfunc1), Depends(depfunc2)])

@app.get("/main")
def get_main():
    pass

# 의존성 함수
def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "valid": True}

# 경로 함수 / 웹 엔드포인트:
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

def check_dep(name: str = Query(...), gender: str = Query(...)):
    if not name:
        raise

@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True
