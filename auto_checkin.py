import requests
import os

url = "https://api.duoduo.link/api"
tokens = os.getenv('DDTK_TOKEN').split('&')

for token in tokens:
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Ddtk": f"Bearer {token}"  # 使用当前循环的token
    }
    
    data = {
        "params": "uyn50u+n1wUDDZA0UEfe681RIK3Wnss6l9wiY4R61wNTII6K/mKoI6p/Idm93Pp8QIKOeFt57sSDxw==",
        "key": "DkwyBJfInVKK7L8ZNqN1GHkZUb9KpHCSbguHalx61tuOaTBc6Y9zX251nbdaG54Wdz1CGfm7TNmJkwF+gWWt4Ya5RB8YpdBdExZ28E43L53pgNOYnaygJyIicB8TdaHQZm3UDKCSx/EZnnHfxTI9ebDtCeAMBGjJ7G6tkDLHnqO1Ss/nKzCWDxLdO2izMxXiA5eXx0vdlq9qJSSn6Eqjc9pcgCCWDTvRovYJrCu3dHOWWwtZBP8bJ4Ncbj0013TJD2vsskvwxc/lqraCwoCn+KFtEwMcuBNIO3/LFIRkF6dbMwPqtwTmcdOh6yUztpaPFK5lQ/tlf82EAwduenbXJdGLHuSNf+hZpRIDru/YPzM2ETyy7qEkpVH23V4/+oyNovVjYk4axfiAgrF+qm9DxLJQGJ61ANk85Ox08JuRPVxIBkU=="
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"Token {token[:5]}...签到成功")
        else:
            print(f"Token {token[:5]}...签到失败:", response.status_code, response.text)
    except Exception as e:
        print(f"Token {token[:5]}...请求异常:", str(e))
